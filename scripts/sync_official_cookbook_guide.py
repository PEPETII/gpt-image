"""Sync the official GPT Image Cookbook guide into the repository.

This script keeps the Cookbook page as the canonical source for section text,
code snippets, prompts, and image assets. Chinese translations and local role
indexes are generated from the same chapter and case mapping.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup, Tag
from markdownify import markdownify


ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = (
    "https://developers.openai.com/cookbook/examples/multimodal/"
    "image-gen-models-prompting-guide"
)
ASSET_ROOT = ROOT / "docs" / "assets" / "official-cookbook"

MAIN_CHAPTERS = [
    ("01-introduction", "1. Introduction"),
    ("02-prompting-fundamentals", "2. Prompting Fundamentals"),
    ("03-setup", "3. Setup"),
    ("04-generate", "4. Use Cases"),
    ("05-edit", "5. Use cases"),
    ("06-additional-use-cases", "6. Additional High-Value Use Cases"),
]

CASE_CHAPTERS = [
    ("04-generate", "4.1 Infographics", "01-infographics"),
    ("04-generate", "4.2 Translation in Images", "02-translation-in-images"),
    ("04-generate", "4.3 Photorealistic Images", "03-photorealistic"),
    ("04-generate", "4.4 World knowledge", "04-world-knowledge"),
    ("04-generate", "4.5 Logo Generation", "05-logo-generation"),
    ("04-generate", "4.6 Ads Generation", "06-ads-generation"),
    ("04-generate", "4.7 Story-to-Comic Strip", "07-story-to-comic"),
    ("04-generate", "4.8 UI Mockups", "08-ui-mockups"),
    ("04-generate", "4.9 Scientific / Educational Visuals", "09-scientific-educational"),
    ("04-generate", "4.10 Slides, Diagrams, Charts, and Productivity Images", "10-slides-charts"),
    ("05-edit", "5.1 Style Transfer", "01-style-transfer"),
    ("05-edit", "5.2 Virtual Clothing Try-On", "02-virtual-try-on"),
    ("05-edit", "5.3 Drawing → Image (Rendering)", "03-drawing-to-image"),
    ("05-edit", "5.4 Product Mockups", "04-product-mockups"),
    ("05-edit", "5.5 Marketing Creatives with Real Text In-Image", "05-marketing-creatives"),
    ("05-edit", "5.6 Lighting and Weather Transformation", "06-lighting-weather"),
    ("05-edit", "5.7 Object Removal", "07-object-removal"),
    ("05-edit", "5.8 Insert the Person Into a Scene", "08-insert-person-scene"),
    ("05-edit", "5.9 Multi-Image Referencing and Compositing", "09-multi-image-compositing"),
    ("06-additional-use-cases", "6.1 Interior design", "01-interior-design-swap"),
    ("06-additional-use-cases", "6.2 3D pop-up holiday card", "02-holiday-card"),
    ("06-additional-use-cases", "6.3 Collectible Action Figure", "03-collectible-figure"),
    ("06-additional-use-cases", "6.4 Children’s Book Art", "04-childrens-book-art"),
]

ASSET_USAGE = {
    "infographic_coffee_machine_gpt-image-2.png": [
        {"chapter": "4.1", "role": "output"},
        {"chapter": "4.2", "role": "input"},
    ],
    "infographic_coffee_machine_sp_gpt-image-2.png": [{"chapter": "4.2", "role": "output"}],
    "photorealism-gpt-image-2.png": [{"chapter": "4.3", "role": "output"}],
    "world_knowledge-gpt-image-2.png": [{"chapter": "4.4", "role": "output"}],
    "logo_generation_1_gpt-image-2.png": [{"chapter": "4.5", "role": "output"}],
    "logo_generation_2_gpt-image-2.png": [{"chapter": "4.5", "role": "output"}],
    "logo_generation_3_gpt-image-2.png": [{"chapter": "4.5", "role": "output"}],
    "logo_generation_4_gpt-image-2.png": [{"chapter": "4.5", "role": "output"}],
    "thread_ad_gpt-image-2.png": [{"chapter": "4.6", "role": "output"}],
    "comic_reel-gpt-image-2.png": [{"chapter": "4.7", "role": "output"}],
    "ui_farmers_market_gpt-image-2.png": [{"chapter": "4.8", "role": "output"}],
    "scientific_educational_cellular_respiration_gpt-image-2.png": [
        {"chapter": "4.9", "role": "output"}
    ],
    "market_opportunity_slide_gpt-image-2.png": [{"chapter": "4.10", "role": "output"}],
    "pixels.png": [{"chapter": "5.1", "role": "input"}],
    "motorcycle_gpt-image-2.png": [{"chapter": "5.1", "role": "output"}],
    "woman_in_museum.png": [
        {"chapter": "5.2", "role": "input: person"},
        {"chapter": "5.8", "role": "input: person"},
    ],
    "tank_top.png": [{"chapter": "5.2", "role": "input: clothing"}],
    "jacket.png": [{"chapter": "5.2", "role": "input: clothing"}],
    "boots.png": [{"chapter": "5.2", "role": "input: clothing"}],
    "outfit_gpt-image-2.png": [{"chapter": "5.2", "role": "output"}],
    "drawings.png": [{"chapter": "5.3", "role": "input"}],
    "realistic_valley_gpt-image-2.png": [{"chapter": "5.3", "role": "output"}],
    "shampoo.png": [
        {"chapter": "5.4", "role": "input: product"},
        {"chapter": "5.5", "role": "input: product"},
    ],
    "extract_product_gpt-image-2.png": [{"chapter": "5.4", "role": "output"}],
    "billboard_gpt-image-2.png": [
        {"chapter": "5.5", "role": "output"},
        {"chapter": "5.6", "role": "input"},
    ],
    "billboard_winter_gpt-image-2.png": [{"chapter": "5.6", "role": "output"}],
    "man_with_blue_hat.png": [{"chapter": "5.7", "role": "input"}],
    "man_with_no_flower_gpt-image-2.png": [{"chapter": "5.7", "role": "output"}],
    "test_woman.png": [{"chapter": "5.9", "role": "input: target scene"}],
    "test_woman_2.png": [{"chapter": "5.9", "role": "input: dog reference"}],
    "test_woman_with_dog_gpt-image-2.png": [{"chapter": "5.9", "role": "output"}],
    "kitchen.jpeg": [{"chapter": "6.1", "role": "input"}],
    "kitchen-chairs_gpt-image-2.png": [{"chapter": "6.1", "role": "output"}],
    "christmas_holiday_card_teddy_gpt-image-2.png": [{"chapter": "6.2", "role": "output"}],
    "christmas_collectible_toy_airplane_gpt-image-2.png": [{"chapter": "6.3", "role": "output"}],
    "childrens_book_illustration_1_gpt-image-2.png": [
        {"chapter": "6.4", "role": "output and next-step input"}
    ],
    "childrens_book_illustration_2_gpt-image-2.png": [{"chapter": "6.4", "role": "output"}],
}

MAIN_CHINESE = {
    "01-introduction": """## 中文翻译

OpenAI 的 GPT Image 图像生成模型面向生产级视觉内容和可控的创作工作流，既适合专业设计，也适合反复迭代的内容制作。核心能力包括：

- 高保真的照片级渲染，包括自然光线、准确材质和丰富色彩；
- 在质量与延迟之间提供可控的取舍；
- 支持编辑、角色一致性和多步骤流程中的人脸与身份保持；
- 在图像内生成清晰、可读、布局稳定的文字；
- 生成信息图、图表和多面板等复杂结构化视觉内容；
- 通过较短的提示词完成风格控制和风格迁移；
- 利用现实世界知识生成可信的对象、环境和场景。

本指南的默认目标模型是 `gpt-image-2`。`low` 适合延迟敏感的批量或探索任务；需要更高保真度、密集文字、照片级细节或复杂编辑时，再比较 `medium` 和 `high`。

### 1.1 模型与参数要点

本文只提供当前 `gpt-image-2` 的调用示例。官方页面中列出的其他模型仅用于迁移背景，不是本项目的推荐目标。

| 项目 | `gpt-image-2` 当前规则 |
|---|---|
| 输出质量 | `low`、`medium`、`high` |
| 图片输入保真度 | 自动按高保真处理；不要传入 `input_fidelity` 覆盖字段 |
| 尺寸 | 满足官方像素、倍数和长宽比约束的自定义尺寸 |
| 典型用途 | 生成、编辑、文字密集画面、照片级渲染、多图合成和身份敏感编辑 |

`gpt-image-2` 的尺寸约束是：最大边长必须小于 `3840px`；宽高都必须是 `16` 的倍数；长边与短边的比例不能超过 `3:1`；总像素数不能超过 `8,294,400`，也不能低于 `655,360`。超过 `2560x1440` 的输出应视为实验性尺寸，结果波动可能更大。

常用参考尺寸包括 `1024x1024`（正方形）、`1024x1536`（竖版）、`1536x1024`（横版）和 `2560x1440`（2K 宽屏）。页面还把 4K/UHD 列为实验性目标；如果严格执行最大边小于 `3840` 的约束，应使用满足倍数要求的略小尺寸。

### 1.2 模型选择与迁移

新项目默认使用 `gpt-image-2`。速度和成本优先时先尝试 `quality="low"`；客户可见资产、照片级生成、编辑密集工作流、品牌敏感内容和图像内文字优先使用更高质量设置。迁移旧工作流时，先保持提示词不变，再根据真实业务中的质量、延迟和重试率进行小步调整。
""",
    "02-prompting-fundamentals": """## 中文翻译

以下原则来自生成、编辑、信息图、广告、人物、UI 和合成等生产场景的反复验证。

1. **结构与目标**：按“背景/场景 → 主体 → 关键细节 → 约束”的顺序组织内容，并说明用途，例如广告、UI 模型或信息图。复杂请求使用短标题或换行，便于扫描和维护。
2. **提示词形式**：最小提示词、描述性段落、类 JSON 结构、指令式文本和标签式文本都可以使用。生产系统应优先选择清晰、可维护的模板，而不是追求特殊语法。
3. **具体描述与质量线索**：明确材质、形状、纹理和媒介。照片级任务直接写 `photorealistic`；“real photograph”“professional photography”等表达也可帮助模型进入相应视觉方向，但不要把精确相机参数当作物理模拟保证。
4. **延迟与保真度**：高并发或对延迟敏感时从 `quality="low"` 开始；小文字、密集信息图、特写肖像、身份敏感编辑和高分辨率输出应比较 `medium` 或 `high`。
5. **构图**：写明景别、视角、透视、角度、光线和情绪；布局重要时指出主体、Logo 或留白的位置。宽幅、电影感、低光、雨景和霓虹场景还需要补充尺度、空气感和色彩关系。
6. **人物、姿势与动作**：描述人物在画面中的比例、身体取景、视线和与物体的互动，例如“全身可见并包含脚部”或“看向打开的书而不是镜头”。
7. **约束与保持项**：明确什么要排除、什么必须保持。编辑任务使用“只改变 X”“保持其他内容不变”，并在每轮迭代中重复身份、几何、布局、标签和相机角度等不变量。
8. **图像文字**：将原文放进引号或使用大写，并指定字体特征、字号关系、颜色、位置和对比度。品牌名或生僻词可逐字拼写；小文字和密集版面应比较 `medium` 或 `high`。
9. **多图输入**：用编号和角色引用每张图，例如“Image 1: 产品图；Image 2: 风格参考”，再说明元素如何从一张图进入另一张图。
10. **逐步迭代**：先生成干净的基础版本，再用一次只改变一个变量的后续请求修正光线、文字、对象或背景。关键约束如果开始漂移，应在后续请求中重新写明。
""",
    "03-setup": """## 中文翻译

第 3 章的初始化代码只需要运行一次：创建 OpenAI 客户端、创建输入和输出图片目录，并提供一个把 base64 结果保存为文件的 helper。编辑用的参考图片放到 `input_images/`，或按实际路径修改示例。

官方示例使用 Python SDK 和 `gpt-image-2`。仓库中的每个用例示例已将 notebook 的相对路径改为 `docs/assets/official-cookbook/` 下的本地资源；运行前请设置 `OPENAI_API_KEY`。生成使用 `client.images.generate`，编辑使用 `client.images.edit`。

`gpt-image-2` 的图片输入自动按高保真处理，因此编辑和参考图工作流不需要、也不应添加 `input_fidelity`。输出数据从 `result.data[0].b64_json` 解码后保存。第 3 章的官方 helper 只是文件保存工具，不代表项目覆盖 Responses API。
""",
    "04-generate": """## 中文翻译

第 4 章覆盖从文本生成图像的十类生产场景。每个场景的完整英文说明、提示词、Python 示例、本地官方图片和输入/输出角色表位于对应子目录：

| 章节 | 中文要点 |
|---|---|
| [4.1 信息图](./01-infographics/README.md) | 面向明确受众解释流程、结构和关系；密集文字需要清晰层级。 |
| [4.2 图像文字翻译](./02-translation-in-images/README.md) | 只改变图中文字，保持对象、构图、颜色和视觉风格。 |
| [4.3 自然的照片级图像](./03-photorealistic/README.md) | 描述人物、材质、镜头感、光线和真实的不完美细节。 |
| [4.4 世界知识](./04-world-knowledge/README.md) | 使用地点、日期和时代细节生成可信的历史或现实场景。 |
| [4.5 Logo 生成](./05-logo-generation/README.md) | 强调原创、清晰轮廓、负空间和大小尺寸下的可读性。 |
| [4.6 广告生成](./06-ads-generation/README.md) | 同时说明品牌、受众、视觉钩子、版式和精确文案。 |
| [4.7 故事转漫画](./07-story-to-comic/README.md) | 逐面板描述动作与情绪，保持角色、画风和叙事连续。 |
| [4.8 UI 模型](./08-ui-mockups/README.md) | 描述真实产品中的内容、导航、操作和可读排版。 |
| [4.9 科学/教育视觉](./09-scientific-educational/README.md) | 用标题、组件、箭头和精确标签构建易读的教学图。 |
| [4.10 幻灯片与图表](./10-slides-charts/README.md) | 说明信息层级、数据、图表、脚注和可比较的标签。 |

生成任务应先描述想要的完整画面，再补充文字、布局和排除项。Logo、广告、信息图、科学图表和幻灯片等文字密集场景尤其需要逐字指定文字、出现次数和位置。
""",
    "05-edit": """## 中文翻译

第 5 章覆盖“文本 + 图片 → 图片”的九类编辑场景。编辑提示词的核心是把改变范围写窄，把必须保持的内容写全。`gpt-image-2` 自动按高保真处理输入图片，不应使用 `input_fidelity`。

| 章节 | 中文要点 |
|---|---|
| [5.1 风格迁移](./01-style-transfer/README.md) | 使用输入图作为风格参考，只替换主体内容。 |
| [5.2 虚拟试穿](./02-virtual-try-on/README.md) | 锁定人物脸部、身份、体型、姿势、发型、背景和光线，只替换衣物。 |
| [5.3 草图转图像](./03-drawing-to-image/README.md) | 保持草图布局、比例、透视和主体位置，再补足真实材质与光线。 |
| [5.4 产品模型](./04-product-mockups/README.md) | 抠出产品并保持几何形状、材质、颜色和标签完整。 |
| [5.5 带真实文字的营销创意](./05-marketing-creatives/README.md) | 让产品自然进入环境，并逐字渲染唯一的广告文案。 |
| [5.6 光照与天气](./06-lighting-weather/README.md) | 只改变环境条件，同时保持主体、构图、服装和无关物体。 |
| [5.7 物体移除](./07-object-removal/README.md) | 移除指定对象并自然重建背景，不改变其他细节。 |
| [5.8 插入人物](./08-insert-person-scene/README.md) | 将人物放入新场景，匹配尺度、透视、光线和阴影。 |
| [5.9 多图引用与合成](./09-multi-image-compositing/README.md) | 明确每张图的来源角色、目标位置和不变元素。 |

推荐的编辑结构是：`Change` 写唯一要改变的对象；`Preserve` 写身份、几何、姿势、构图、标签和背景；`Do not change` 作为兜底禁止额外修改。多轮编辑中重复这些不变量，可以降低前一步结果发生漂移的概率。
""",
    "06-additional-use-cases": """## 中文翻译

第 6 章展示四个更复杂的高级工作流：精确室内替换、立体节日贺卡、收藏品概念图，以及利用角色锚点保持跨页面一致性的儿童绘本流程。

| 章节 | 中文要点 |
|---|---|
| [6.1 室内设计替换](./01-interior-design-swap/README.md) | 只替换目标家具，保持相机角度、房间光线、地面阴影和周围对象。 |
| [6.2 3D 立体节日贺卡](./02-holiday-card/README.md) | 用 Scene、Mood、Style、Constraints 描述纸张层次、纤维、深度和实体感。 |
| [6.3 收藏级手办/毛绒钥匙扣](./03-collectible-figure/README.md) | 用 Concept、Style、Constraints 控制材质、包装、摄影光线和原创限制。 |
| [6.4 儿童绘本角色一致性](./04-childrens-book-art/README.md) | 先生成角色锚点，再把第一步输出作为下一步编辑输入，推进故事场景。 |

### 角色锚点工作流

第一步锁定角色外观、比例、服装、表情、色彩和画风；第二步引用同一张锚点图，只改变场景和动作，同时重复角色一致性约束。锚点图在本地资源中只保存一次，manifest 标记它既是第一步输出，也是下一步输入。

高级场景仍然遵循同一原则：明确变化、列出不变量、描述可观察的材质和光线，并通过小步编辑逐步推进。所有案例都使用 `gpt-image-2` Image API 的 `generate` 或 `edit`。
""",
}

CASE_PROMPT_ZH = {
    "4.1": "创建一张详细的信息图，解释类似 Jura 的全自动咖啡机的工作功能和流程。从豆仓、研磨、秤、水箱到锅炉等部件都要展示出来，让读者从技术和视觉上理解整个流程。",
    "4.2": "将信息图中的文字翻译成西班牙语。不要改变图片的任何其他部分。",
    "4.3": "创建一张照片级写实的抓拍照片：一位年长的水手站在小渔船上，皮肤有风吹日晒的纹理和皱纹，手臂上有褪色的传统水手纹身。他正在平静地整理渔网，旁边的甲板上坐着他的狗。画面像 35mm 胶片照片，以平视中近景和 50mm 镜头拍摄；使用柔和的海岸日光、浅景深、轻微胶片颗粒和自然色彩。画面应真实、不摆拍，不要过度美化或重度修图。",
    "4.4": "创建一幅写实的户外人群场景：地点是纽约州贝瑟尔，时间是 1969 年 8 月 16 日。服装、现场安排和环境都要符合时代，整体采用照片级写实风格。",
    "4.5": "为名为 Field & Flour 的本地面包店创建原创且不侵权的 Logo。Logo 应温暖、简洁、历久弥新，使用干净的矢量感形状、清晰轮廓和平衡的负空间；细节要足够少，使其在大小尺寸下都清晰可读。使用扁平设计和极少描边，置于纯色背景中央并留出充足边距，不要水印。",
    "4.6": "为名为 Thread 的年轻街头品牌创作一张文化/时尚广告图。画面是一群朋友一起消磨时光，带有标语“Yours to Create.”。面向年轻街头服饰受众，整体要时髦、当代、有活力且得体；使用干净构图、明确色彩方向、自然姿势和高端时尚摄影语言。标语只出现一次，清晰可读并融入版式，不添加其他文字、水印或无关 Logo。",
    "4.7": "创建一条短的竖版漫画风视频缩略图，包含 4 个大小相同的面板。第 1 格：主人从前门离开，宠物被框在身后的窗户里，眼睛睁大、爪子高高贴在玻璃上。第 2 格：门咔哒一声关上，宠物转身面对空房子，眼神逐渐变得精明。第 3 格：房子已经变样，宠物像房子的主人一样摊在沙发上，旁边有碎屑，阳光像聚光灯一样穿过房间。第 4 格：门打开，宠物端坐在入口处，仿佛什么也没有发生。",
    "4.8": "创建一个真实的本地农贸市场移动应用 UI 模型。展示今日市场、简洁的标题栏、带小照片和分类的供应商列表、Today’s specials 区域，以及地点和营业时间等基本信息。设计要实用、易用、漂亮；使用白色背景、低调自然的强调色、清晰排版和极少装饰，并把 UI 放在 iPhone 外框中。",
    "4.9": "为高中生创建一张标题为“Cellular Respiration at a Glance”的简洁生物学图表。展示细胞内葡萄糖如何转化为能量，包括糖酵解、克雷布斯循环和电子传递链；用箭头连接步骤，并标注 glucose、pyruvate、ATP、NADH、FADH2、CO2、O2 和 H2O。画面像干净的课堂讲义或幻灯片，白色背景、简单图标、清晰且易读的文字，不要小字、额外装饰或难以理解的内容。",
    "4.10": "创建一张标题为“Market Opportunity”的融资演示幻灯片，像真正的 YC 支持的初创公司 Series A 融资页。使用白色背景、现代无衬线字体和清晰极简布局；包含 TAM/SAM/SOM 同心圆图、TAM $42B、SAM $8.7B、SOM $340M 的市场规模数据、2021 至 2026 年的增长柱状图、脚注“AGI Research, 2024”和“Internal analysis”，以及右下角的公司 Logo 占位符。要求文字高度可读、数据层级清晰、间距专业；不要剪贴画、图库照片、渐变、阴影或装饰性元素。",
    "5.1": "使用输入图片的相同风格，在白色背景上生成一个骑摩托车的男人。",
    "5.2": "使用提供的服装图片为女性换装。不要改变她的脸、五官、肤色、体型、姿势或身份；保持她的相貌、表情、发型和比例完全一致。只替换服装，使其自然贴合现有姿势和身体几何，呈现真实的面料行为；匹配原图的光线、阴影和色温，让服装照片级融合而不是像贴上去的。不要改变背景、相机角度、构图或图像质量，也不要添加配饰、文字、Logo 或水印。",
    "5.3": "将这幅图画转换成照片级写实图像。保持准确的布局、比例和透视；根据草图意图选择真实材质和光线；不要添加新的元素或文字。",
    "5.4": "从输入图片中提取产品并放到纯白不透明背景上。输出应是居中的产品、干净的轮廓且没有光晕或边缘残留；精确保留产品几何形状和标签可读性。只做轻微润色和自然接触阴影，不要重新设计、改变风格或扭曲产品。",
    "5.5": "创建一张真实的洗发水广告牌模型：产品位于日落时分的高速公路场景中。广告牌文字必须逐字为“Fresh and clean”，只出现一次；使用高对比、居中的粗体无衬线字体和干净字距，确保清晰可读。不要水印或 Logo。",
    "5.6": "让画面看起来像一个有降雪的冬季夜晚。",
    "5.7": "移除男人手中的花朵，不要改变任何其他内容。",
    "5.8": "生成一个高度写实的动作场景：图中人物正在逃离一只攻击露营地的大型写实棕熊。画面像真实照片，而不是过度增强或电影海报；她位于画面中央但看向远处，穿户外露营服，脸上有泥土、衣服有撕裂，既害怕又专注于逃跑。露营地位于约塞米蒂国家公园，背景有可信的自然细节；时间是黄昏，使用自然光和真实色彩。整体要朴素、真实、没有风格化处理，不要电影式灯光、戏剧化调色或过度设计的构图。",
    "5.9": "将第二张图片中的狗放入第一张图片的场景中，紧挨着女性；使用与第一张图相同的光线、构图和背景风格。不要改变任何其他内容。",
    "6.1": "在这张房间照片中，只把白色椅子替换成木质椅子。保持相机角度、房间光线、地面阴影和周围物体不变；其他所有方面都保持不变，并生成真实的接触阴影和材质纹理。",
    "6.2": "创建一张圣诞节日贺卡插画：温馨的圣诞场景中，一只略有磨损、带柔软修补针脚的旧泰迪熊坐在纪念盒里，窗外正在下雪，暗示孩子已经长大但记忆仍在。氛围温暖、怀旧、柔和而感人；采用高端节日卡片摄影、柔和电影感灯光、真实纹理、浅景深、得体的散景灯光和适合印刷的构图。只使用原创艺术，不要商标、水印或 Logo；只加入文字“Merry Christmas — some memories never fade.”。",
    "6.3": "创建一个放在泡罩包装中的复古螺旋桨玩具飞机收藏手办。飞机有圆形机翼、前置旋转螺旋桨、略有磨损的油漆边缘和经典的童年玩具比例，作为怀旧节日收藏品。包装概念唤起冬日玩具、温暖、想象力和童真；使用高端玩具摄影、真实塑料和涂漆金属材质、影棚灯光、浅景深、清晰标签印刷和高端零售展示。只做原创设计，不要商标、水印或 Logo；只加入文字“Christmas Memories Edition”。",
    "6.4": "第一步：创建一张儿童绘本插画来介绍主角。主角是受森林小侠启发的年轻绘本英雄，穿绿色连帽上衣、柔软棕色靴子并带小腰包，表情善良、眼神温和，勇敢但亲切，携带只用于帮助而不伤害他人的小木弓。主题是保护和救助松鼠、鸟和兔子等小动物；使用手绘水彩、柔和轮廓、温暖土色和友善奇幻的绘本风格，背景保持简单的森林。第二步：继续同一个儿童故事，让同一位英雄在暴风雪后的倒树旁温柔地帮助受惊的松鼠；保持同样的绿色上衣、面部特征、比例、色彩和性格，不要重新设计角色、文字或水印。",
}

CASE_VARIABLES = {
    "4.1": "可替换 `[TOPIC]`、`[AUDIENCE]`、流程组件和标签；密集文字保持短、清晰并明确层级。",
    "4.2": "可替换 `[TARGET_LANGUAGE]`；保留“只改变文字”的限制。",
    "4.3": "可替换人物、年龄、地点、动作、景别、镜头感、光线和情绪。",
    "4.4": "可替换 `[EVENT]`、地点、日期/时代和对应的历史细节。",
    "4.5": "可替换品牌名、业务类型、品牌气质、色彩系统和 Logo 概念。",
    "4.6": "可替换品牌、受众、场景、视觉钩子和 `[EXACT_TAGLINE]`。",
    "4.7": "可替换画面方向、面板数量、每格动作、角色和叙事节奏。",
    "4.8": "可替换产品、受众、信息模块、导航、设备外框和配色。",
    "4.9": "可替换图表标题、受众、概念、组件、精确标签和箭头关系。",
    "4.10": "可替换标题、受众、关键数据、图表类型、脚注和版式。",
    "5.1": "可替换风格参考图、目标主体、背景和需要保持的媒介特征。",
    "5.2": "可替换人物图、服装图和衣物目标；人物身份、体型、姿势和背景属于保持项。",
    "5.3": "可替换草图、目标媒介、材质和光线；布局、比例和透视属于保持项。",
    "5.4": "可替换产品图和背景；几何形状、材质、颜色、标签和轮廓属于保持项。",
    "5.5": "可替换产品、广告环境、时间、字体描述和唯一精确文案。",
    "5.6": "可替换天气、时间和光照条件；主体、构图和无关物体属于保持项。",
    "5.7": "可替换待移除对象和所在位置；背景结构、光线和所有无关细节属于保持项。",
    "5.8": "可替换人物参考图、目标场景、动作、尺度、光线和环境。",
    "5.9": "可替换 Image 1/2 的角色、要移动的对象和目标位置；明确每张图的来源关系。",
    "6.1": "可替换房间图、原对象、新对象和必须保持的相机/光照/阴影条件。",
    "6.2": "可替换节日、场景描述、氛围、纸张/材质风格和 `[SHORT_COPY]`。",
    "6.3": "可替换收藏品描述、包装概念、材质、摄影方向和 `[SHORT_COPY]`。",
    "6.4": "可替换角色锚点、场景、动作、角色一致性清单和绘本风格。",
}


def fetch(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "gpt-image-cookbook-sync"})
    with urlopen(request, timeout=60) as response:
        return response.read()


def heading_text(tag: Tag) -> str:
    return " ".join(tag.get_text(" ", strip=True).split())


def find_heading(soup: BeautifulSoup, title: str) -> Tag:
    for heading in soup.find_all("h2"):
        if heading_text(heading).lower().startswith(title.lower()):
            return heading
    raise ValueError(f"Official heading not found: {title}")


def collect_until_heading(heading: Tag, stop_on_any_h2: bool = True) -> list[Tag | str]:
    nodes: list[Tag | str] = [heading]
    for sibling in heading.next_siblings:
        if isinstance(sibling, Tag) and sibling.name == "h2" and stop_on_any_h2:
            break
        nodes.append(sibling)
    return nodes


def collect_main_chapter(heading: Tag) -> list[Tag | str]:
    nodes: list[Tag | str] = [heading]
    for sibling in heading.next_siblings:
        if isinstance(sibling, Tag) and sibling.name == "h2":
            text = heading_text(sibling)
            if re.match(r"^\d+\.\s", text):
                break
        nodes.append(sibling)
    return nodes


def to_markdown(
    nodes: list[Tag | str],
    asset_links: dict[str, str] | None = None,
    from_dir: Path | None = None,
) -> str:
    html = "".join(str(node) for node in nodes)
    result = markdownify(html, heading_style="ATX", bullets="-")
    result = re.sub(r"\n{3,}", "\n\n", result).strip()
    if asset_links:
        asset_dir = Path(os.path.relpath(ASSET_ROOT, from_dir or ROOT)).as_posix()
        legacy_image_root = Path("..", "..", "images").as_posix()
        for source, local in asset_links.items():
            result = result.replace(source, f"{asset_dir}/{Path(local).name}")
        for local in {Path(value).name for value in asset_links.values()}:
            local_link = f"{asset_dir}/{local}"
            result = result.replace(f"{legacy_image_root}/input_images/{local}", local_link)
            result = result.replace(f"{legacy_image_root}/output_images/{local}", local_link)
        result = result.replace(f"{legacy_image_root}/input_images", "input_images")
        result = result.replace(f"{legacy_image_root}/output_images", "output_images")
        result = re.sub(
            r'(?m)^(\s*open\([^\n]*tank_top\.png[^\n]*\r?\n\s*open\([^\n]*jacket\.png[^\n]*\r?\n)\s*open\([^\n]*tank_top\.png[^\n]*\r?\n',
            r'\1',
            result,
        )
    result = result.replace("outputQuality", "quality").replace("recommedned", "recommended")
    # The Cookbook page still contains this field in a few legacy snippets.
    # The current gpt-image-2 API rejects it, so local runnable examples omit it.
    result = re.sub(r"(?m)^\s*input_fidelity\s*=.*\n", "", result)
    result = re.sub(r"(?m)^from IPython\.display.*\n", "", result)
    result = re.sub(r"(?m)^\s*display\(Image\(.*(?:\n|\Z)", "", result)
    result = "\n".join(line.rstrip() for line in result.splitlines())
    return result + "\n"


def extract_code(nodes: list[Tag | str]) -> list[tuple[str, str]]:
    html = "".join(str(node) for node in nodes)
    soup = BeautifulSoup(html, "html.parser")
    blocks: list[tuple[str, str]] = []
    for pre in soup.find_all("pre"):
        language = pre.get("data-language") or "text"
        code = pre.find("code")
        if code:
            lines = code.select("span.line")
            text = "\n".join(line.get_text("", strip=False) for line in lines)
            if not text.strip():
                text = code.get_text("", strip=False)
        else:
            text = pre.get_text("\n", strip=False)
        blocks.append((language, text.strip()))
    return blocks


def extract_prompts(code_blocks: list[tuple[str, str]]) -> list[str]:
    prompts: list[str] = []
    pattern = re.compile(
        r"\bprompt\s*=\s*(?:[furbFURB]+)?(?P<quote>\"\"\"|'''|\"|')(?P<body>.*?)(?P=quote)",
        re.DOTALL,
    )
    for language, code in code_blocks:
        if language.lower() not in {"python", "py"}:
            continue
        prompts.extend(
            "\n".join(line.rstrip() for line in match.group("body").splitlines()).strip()
            for match in pattern.finditer(code)
        )
    return prompts


def extract_prompt_reference(title: str) -> str:
    chapter_number = title.split(maxsplit=1)[0]
    return CASE_PROMPT_ZH.get(chapter_number, "请根据官方 prompt 代码块替换主体、场景和限制条件。")


def relative_asset_links(asset_names: list[str], from_dir: Path) -> list[str]:
    asset_dir = Path(os.path.relpath(ASSET_ROOT, from_dir)).as_posix()
    return [f"{asset_dir}/{name}" for name in asset_names]


def find_assets(nodes: list[Tag | str], all_assets: dict[str, str]) -> list[str]:
    html = "".join(str(node) for node in nodes)
    text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)
    found = []
    for name in all_assets:
        if name in html or name in text:
            found.append(name)
    return sorted(found)


def download_assets(
    soup: BeautifulSoup,
    dry_run: bool,
    reuse_assets: bool = False,
) -> tuple[dict[str, dict], dict[str, str]]:
    source_paths = sorted(
        {
            value
            for image in soup.find_all("img")
            for value in [image.get("src") or image.get("data-src")]
            if value and "/cookbook/assets/images/" in value
        }
    )
    manifest: dict[str, dict] = {}
    links: dict[str, str] = {}
    for source_path in source_paths:
        name = Path(source_path).name
        source_url = urljoin("https://developers.openai.com", source_path)
        target = ASSET_ROOT / name
        if dry_run:
            payload = b""
        elif reuse_assets and target.exists():
            payload = target.read_bytes()
        else:
            payload = fetch(source_url)
        digest = hashlib.sha256(payload).hexdigest() if payload else None
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            current_digest = None
            if target.exists():
                current_digest = hashlib.sha256(target.read_bytes()).hexdigest()
            if current_digest != digest:
                target.write_bytes(payload)
        manifest[name] = {
            "source_url": source_url,
            "local_path": target.relative_to(ROOT).as_posix(),
            "usages": ASSET_USAGE.get(name, []),
            "chapters": sorted({usage["chapter"] for usage in ASSET_USAGE.get(name, [])}),
            "sha256": digest,
            "size_bytes": len(payload) if payload else None,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
        }
        links[source_path] = target.relative_to(ROOT).as_posix()
        links[source_url] = target.relative_to(ROOT).as_posix()
    return manifest, links


def normalize_python_code(code: str) -> str:
    """Make an official notebook excerpt runnable with repository-local assets."""
    code = re.sub(r"(?m)^\s*input_fidelity\s*=.*\n", "", code)
    code = re.sub(
        r'open\("\.\./\.\./images/(?:input_images|output_images)/([^\"]+)",\s*"rb"\)',
        r'open(ASSET_ROOT / "\1", "rb")',
        code,
    )
    code = re.sub(
        r'with open\(f"\.\./\.\./images/output_images/([^\"]+)",\s*"wb"\) as f:',
        r'with (OUTPUT_DIR / f"\1").open("wb") as f:',
        code,
    )
    code = re.sub(r"(?m)^from IPython\.display.*\n", "", code)
    code = re.sub(r"(?m)^display\(Image\(.*(?:\n|\Z)", "", code)
    duplicate = (
        '        open(ASSET_ROOT / "tank_top.png", "rb"),\n'
        '        open(ASSET_ROOT / "jacket.png", "rb"),\n'
        '        open(ASSET_ROOT / "tank_top.png", "rb"),\n'
        '        open(ASSET_ROOT / "boots.png", "rb"),'
    )
    code = code.replace(
        duplicate,
        '        open(ASSET_ROOT / "tank_top.png", "rb"),\n'
        '        open(ASSET_ROOT / "jacket.png", "rb"),\n'
        '        open(ASSET_ROOT / "boots.png", "rb"),',
    )
    return "\n".join(line.rstrip() for line in code.splitlines()).strip()


def build_python_example(code_blocks: list[tuple[str, str]]) -> str:
    header = "\n".join(
        [
            '\"\"\"Official Python example adapted for repository-local Cookbook assets.\"\"\"',
            "",
            "import base64",
            "from pathlib import Path",
            "",
            "from openai import OpenAI",
            "",
            "",
            'ASSET_ROOT = Path(__file__).resolve().parents[2] / "assets" / "official-cookbook"',
            'OUTPUT_DIR = Path(__file__).resolve().parent / "output_images"',
            "OUTPUT_DIR.mkdir(parents=True, exist_ok=True)",
            "client = OpenAI()",
            "",
            "",
            "def save_image(result, filename: str) -> None:",
            '    \"\"\"Save the first returned image next to this example.\"\"\"',
            "    image_bytes = base64.b64decode(result.data[0].b64_json)",
            "    (OUTPUT_DIR / filename).write_bytes(image_bytes)",
            "",
            "",
        ]
    )
    blocks = [
        normalize_python_code(code)
        for language, code in code_blocks
        if language.lower() in {"python", "py"}
    ]
    blocks = [code for code in blocks if code]
    return header + "\n\n".join(blocks) + "\n"


def write_case(
    soup: BeautifulSoup,
    main_dir: Path,
    title: str,
    slug: str,
    asset_links: dict[str, str],
    all_assets: dict[str, str],
    dry_run: bool,
) -> None:
    heading = find_heading(soup, title)
    nodes = collect_until_heading(heading)
    code_blocks = extract_code(nodes)
    prompts = extract_prompts(code_blocks)
    case_dir = ROOT / "docs" / main_dir / slug
    assets = find_assets(nodes, all_assets)
    source_md = to_markdown(nodes, asset_links, case_dir)
    local_links = relative_asset_links(assets, case_dir)
    prompt_translation = extract_prompt_reference(title)

    if dry_run:
        return
    case_dir.mkdir(parents=True, exist_ok=True)
    readme = [
        f"# {title}",
        "",
        f"> 官方来源：[{SOURCE_URL}]({SOURCE_URL})",
        "",
        "## Official content",
        "",
        source_md,
        "## 中文整理",
        "",
        prompt_translation,
        "",
        "## 本地图片",
        "",
    ]
    if local_links:
        readme.extend(f"- ![{Path(link).stem}]({link})" for link in local_links)
    else:
        readme.append("本节没有官方图片资源。")
    chapter_number = title.split(maxsplit=1)[0]
    relevant_usage = [
        (name, usage["role"])
        for name in assets
        for usage in ASSET_USAGE.get(name, [])
        if usage["chapter"] == chapter_number
    ]
    readme.extend(["", "## 输入/输出角色", "", "| 文件 | 角色 |", "|---|---|"])
    if relevant_usage:
        readme.extend(f"| `{name}` | {role} |" for name, role in relevant_usage)
    else:
        readme.append("| 无 | 本节没有图片输入或输出 |")
    readme.extend(
        [
            "",
            "## 复现说明",
            "",
            "本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。",
            "",
        ]
    )
    (case_dir / "README.md").write_text("\n".join(readme), encoding="utf-8")

    prompt_lines = [f"# {title} Prompt", "", f"Source: {SOURCE_URL}", ""]
    if prompts:
        for index, prompt in enumerate(prompts, 1):
            prompt_lines.extend([f"## Official prompt {index}", "", "```text", prompt, "```", ""])
    else:
        prompt_lines.extend(["官方页面没有独立 prompt 变量；请参考 README 中的完整代码块。", ""])
    chapter_number = title.split(maxsplit=1)[0]
    prompt_lines.extend(
        [
            "## 中文翻译",
            "",
            prompt_translation,
            "",
            "## 可替换变量",
            "",
            CASE_VARIABLES.get(chapter_number, "替换主体、场景、风格、文字和限制条件。"),
            "",
        ]
    )
    (case_dir / "prompt.md").write_text("\n".join(prompt_lines), encoding="utf-8")

    python_blocks = [code for language, code in code_blocks if language.lower() in {"python", "py"}]
    if python_blocks:
        (case_dir / "example.py").write_text(build_python_example(code_blocks), encoding="utf-8")


def write_main_chapter(
    soup: BeautifulSoup,
    slug: str,
    title: str,
    asset_links: dict[str, str],
    all_assets: dict[str, str],
    dry_run: bool,
) -> None:
    heading = find_heading(soup, title)
    nodes = collect_main_chapter(heading)
    chapter_dir = ROOT / "docs" / slug
    source_md = to_markdown(nodes, asset_links, chapter_dir)
    assets = find_assets(nodes, all_assets)
    case_links = [
        (case_slug, case_title)
        for parent, case_title, case_slug in CASE_CHAPTERS
        if parent == slug
    ]
    if dry_run:
        return
    chapter_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {title}",
        "",
        f"> 官方来源：[{SOURCE_URL}]({SOURCE_URL})",
        "",
        "## 章节目录",
        "",
    ]
    if case_links:
        lines.extend(f"- [{case_title}](./{case_slug}/README.md)" for case_slug, case_title in case_links)
    else:
        lines.append("本章没有独立用例子章节。")
    chinese = MAIN_CHINESE.get(slug, "本章中文翻译待补充。")
    lines.extend(["", "## Official content", "", source_md, chinese, ""])
    if assets:
        lines.extend(["## 本章图片", ""])
        lines.extend(f"- [{name}](../assets/official-cookbook/{name})" for name in assets)
        lines.append("")
    (chapter_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--reuse-assets",
        action="store_true",
        help="Reuse existing local assets and only fetch missing files.",
    )
    args = parser.parse_args()

    raw = fetch(SOURCE_URL)
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    manifest, asset_links = download_assets(soup, args.dry_run, args.reuse_assets)
    all_assets = {name: meta["source_url"] for name, meta in manifest.items()}

    for slug, title in MAIN_CHAPTERS:
        write_main_chapter(soup, slug, title, asset_links, all_assets, args.dry_run)

    for main_dir, title, case_slug in CASE_CHAPTERS:
        write_case(soup, main_dir, title, case_slug, asset_links, all_assets, args.dry_run)

    if not args.dry_run:
        manifest_path = ASSET_ROOT / "manifest.json"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(
            json.dumps(
                {
                    "source_url": SOURCE_URL,
                    "retrieved_at": datetime.now(timezone.utc).isoformat(),
                    "asset_count": len(manifest),
                    "assets": manifest,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    print(f"official_source={SOURCE_URL}")
    print(f"assets={len(manifest)}")
    print(f"cases={len(CASE_CHAPTERS)}")
    print(f"dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
