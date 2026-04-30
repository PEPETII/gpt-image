# 提示词速查表 | Prompt Cheatsheet

按场景分类的 GPT Image 2 提示词模板速查，涵盖全部 23 个案例。

## 生成模式 (Generate)

| 场景 | 模式 | 提示词模板（精简版） | 关键参数 |
|------|------|---------------------|---------|
| 信息图表 Infographic | 生成 | Create a detailed Infographic of [主题]. From [步骤1], to [步骤2], etc. | quality="high" |
| 图片翻译 Translation | 生成 | Translate the text in the image to [目标语言]. Do not change any other aspect. | input_fidelity="high" |
| 照片级写实 Photorealistic | 生成 | Create a photorealistic [场景]. [人物细节]. Shot like a [相机参数]. | quality="high" |
| 世界知识 World Knowledge | 生成 | Create a realistic [场景] in [地点] on [日期]. Photorealistic, period-accurate. | quality="high" |
| Logo 生成 Logo Generation | 生成 | Create an original, non-infringing logo for [品牌]. [风格描述]. Flat design. | n=4, background="opaque" |
| 广告生成 Ad Generation | 生成 | Give me a [风格] ad for [品牌]. Tagline: "[标语]". [受众和氛围描述]. | quality="high" |
| 故事转漫画 Story to Comic | 生成 | Create a [面板数] comic-style reel with [面板数] panels. Panel 1: [场景]... | - |
| UI 模型 UI Mockup | 生成 | Create a realistic mobile app UI mockup for [产品]. [界面元素描述]. Place in [设备框架]. | quality="high" |
| 科学/教育 Scientific/Educational | 生成 | Create a [学科] diagram titled "[标题]" for [受众]. [内容要求]. Avoid tiny text. | quality="high" |
| 幻灯片/图表 Slides/Charts | 生成 | Create one [类型] slide titled "[标题]". [内容要求]. Avoid [避免的设计元素]. | quality="high" |
| 节日贺卡 Holiday Card | 生成 | Create a [节日] card illustration. Scene: [场景]. Mood: [氛围]. Style: [风格]. Constraints: [约束]. | quality="high" |
| 收藏手办 Collectible Figure | 生成 | Create a collectible [类型] of [描述]. Concept: [概念]. Style: [风格]. Constraints: [约束]. | quality="high" |

## 编辑模式 (Edit)

| 场景 | 模式 | 提示词模板（精简版） | 关键参数 |
|------|------|---------------------|---------|
| 风格迁移 Style Transfer | 编辑 | Use the same style from the input image and generate [新内容]. | - |
| 虚拟试穿 Virtual Try-On | 编辑 | Edit the image to dress the person using the provided clothing. Do not change [锁定特征]. | input_fidelity="high" |
| 素描转图像 Sketch to Image | 编辑 | Turn this drawing into a photorealistic image. Preserve [保持要素]. Do not add new elements. | input_fidelity="high", quality="high" |
| 产品模型 Product Mockup | 编辑 | Extract the product and place on a plain white opaque background. Preserve [保持要素]. | background="opaque", input_fidelity="high" |
| 营销创意 Marketing Creative | 编辑 | Create a realistic [广告类型] of [产品] on [场景]. Text (EXACT): "[文案]". | quality="high" |
| 光照天气 Lighting/Weather | 编辑 | Make it look like a [天气/时间] with [效果]. | input_fidelity="high" |
| 物品移除 Object Removal | 编辑 | Remove [物体] from [位置]. Do not change anything else. | input_fidelity="high" |
| 人物插入 Person Insertion | 编辑 | Generate a [场景] where this person is [动作]. [人物和场景细节]. | input_fidelity="high", quality="high" |
| 多图合成 Multi-Image Compositing | 编辑 | Place [物体] from the second image into the setting of image 1. Do not change anything else. | input_fidelity="high" |
| 室内替换 Interior Replacement | 编辑 | In this room photo, replace ONLY [旧物体] with [新物体]. Preserve [保持要素]. | input_fidelity="high" |

## 生成 + 编辑混合模式 (Generate + Edit)

| 场景 | 模式 | 提示词模板（精简版） | 关键参数 |
|------|------|---------------------|---------|
| 儿童绘本 Children's Book | 生成+编辑 | Step1: 创建角色锚点. Step2: 使用 edit 模式传入角色图保持一致性. | quality="high", input_fidelity="high" |
