# 第4章：生成用例 | Generate Use Cases

> 本章介绍 Generate 模式（text-to-image）的 10 个核心用例，涵盖信息图表、图片翻译、照片级写实、世界知识、Logo 生成、广告生成、故事转漫画、UI 模型、科学/教育以及幻灯片/图表场景。

---

## 4.1 信息图表 | Infographic

利用 GPT 图像模型生成包含数据可视化和文字说明的信息图表，适合社交媒体分享和报告展示。

> 模型能够理解数据关系并生成结构化的图表布局，包括柱状图、饼图、流程图等多种形式。

**提示词模板**：[prompts/generate/infographic.md](../prompts/generate/infographic.md)

---

## 4.2 图片翻译 | Translation

将包含外文文字的图片翻译为目标语言，同时保持原始图像的布局、设计和视觉风格不变。

> 该用例特别适合需要将营销材料、产品包装或宣传海报本地化为不同语言版本的场景。

**提示词模板**：[prompts/generate/translation.md](../prompts/generate/translation.md)

---

## 4.3 照片级写实 | Photorealistic

生成具有极高真实感的照片级图像，包括人物肖像、风景摄影、产品摄影等多种摄影风格。

> 通过精确描述光线、相机参数、构图和氛围，模型可以生成几乎无法与真实照片区分的图像。

**提示词模板**：[prompts/generate/photorealistic.md](../prompts/generate/photorealistic.md)

---

## 4.4 世界知识 | World Knowledge

利用模型对真实世界的知识理解，生成包含真实地标、历史场景、文化元素等准确细节的图像。

> 模型能够理解地理、历史、文化等领域的知识，生成符合真实世界细节的图像。

**提示词模板**：[prompts/generate/world-knowledge.md](../prompts/generate/world-knowledge.md)

---

## 4.5 Logo 生成 | Logo Generation

根据品牌描述生成专业的 Logo 设计，支持多种风格（极简、复古、现代、手绘等）和格式。

> 适合初创品牌快速获得 Logo 设计方案，或为现有品牌探索新的视觉方向。

**提示词模板**：[prompts/generate/logo-generation.md](../prompts/generate/logo-generation.md)

---

## 4.6 广告生成 | Ads Generation

生成完整的广告创意图像，包括社交媒体广告、展示广告、印刷广告等多种格式和尺寸。

> 模型能够理解广告的视觉层次结构，生成包含产品展示、文案区域和品牌元素的完整广告画面。

**提示词模板**：[prompts/generate/ads-generation.md](../prompts/generate/ads-generation.md)

---

## 4.7 故事转漫画 | Comic Strip

将文字故事或叙事内容转化为多格漫画条，包含角色设计、对话气泡和分镜构图。

> 该用例展示了模型在叙事视觉化方面的能力，适合内容创作者和教育场景。

**提示词模板**：[prompts/generate/comic-strip.md](../prompts/generate/comic-strip.md)

---

## 4.8 UI 模型 | UI Mockups

生成逼真的用户界面模型，包括移动应用界面、网页设计、仪表盘等多种 UI 类型。

> 模型能够理解 UI 设计规范和布局模式，生成可用于概念验证和设计沟通的高保真 UI 模型。

**提示词模板**：[prompts/generate/ui-mockups.md](../prompts/generate/ui-mockups.md)

---

## 4.9 科学/教育 | Scientific & Educational

生成科学图解、教育插图、流程图等视觉材料，帮助解释复杂概念和科学原理。

> 模型能够准确表达科学概念，生成适合教材、论文和演示文稿的教育视觉内容。

**提示词模板**：[prompts/generate/scientific-educational.md](../prompts/generate/scientific-educational.md)

---

## 4.10 幻灯片/图表 | Slides & Charts

生成专业的幻灯片背景、数据图表和生产力相关的图像，适合演示文稿和商业报告。

> 该用例展示了模型在商业视觉内容生成方面的能力，可大幅提升演示文稿的制作效率。

**提示词模板**：[prompts/generate/slides-charts.md](../prompts/generate/slides-charts.md)

---

## 用例总览表

| 编号 | 用例 | 提示词模板 | 推荐质量 |
|------|------|-----------|----------|
| 4.1 | 信息图表 | [infographic.md](../prompts/generate/infographic.md) | `quality="high"` |
| 4.2 | 图片翻译 | [translation.md](../prompts/generate/translation.md) | `quality="high"` |
| 4.3 | 照片级写实 | [photorealistic.md](../prompts/generate/photorealistic.md) | `quality="medium"` |
| 4.4 | 世界知识 | [world-knowledge.md](../prompts/generate/world-knowledge.md) | `quality="medium"` |
| 4.5 | Logo 生成 | [logo-generation.md](../prompts/generate/logo-generation.md) | `quality="high"` |
| 4.6 | 广告生成 | [ads-generation.md](../prompts/generate/ads-generation.md) | `quality="medium"` |
| 4.7 | 故事转漫画 | [comic-strip.md](../prompts/generate/comic-strip.md) | `quality="medium"` |
| 4.8 | UI 模型 | [ui-mockups.md](../prompts/generate/ui-mockups.md) | `quality="high"` |
| 4.9 | 科学/教育 | [scientific-educational.md](../prompts/generate/scientific-educational.md) | `quality="medium"` |
| 4.10 | 幻灯片/图表 | [slides-charts.md](../prompts/generate/slides-charts.md) | `quality="high"` |

---

## 生成模式通用最佳实践

### 1. 描述具体性决定输出质量

提示词越具体，输出越符合预期。避免模糊的描述，提供尽可能多的细节：

| 模糊描述 | 具体描述 |
|----------|----------|
| "A beautiful landscape" | "A misty mountain landscape at dawn, with a winding river reflecting the golden sky, pine trees silhouetted in the foreground" |
| "A product photo" | "A sleek wireless headphone on a marble surface, soft studio lighting, shallow depth of field, dark background" |

### 2. 构图信息不可或缺

构图信息（视角、光线、氛围）对输出质量有决定性影响：

| 构图维度 | 示例 |
|----------|------|
| **视角** | "Bird's-eye view", "Close-up shot", "Wide-angle lens", "Low angle" |
| **光线** | "Golden hour lighting", "Soft diffused light", "Dramatic side lighting", "Neon glow" |
| **氛围** | "Serene and peaceful", "Energetic and vibrant", "Mysterious and moody" |
| **风格** | "Photorealistic", "Watercolor painting", "Minimalist illustration", "Cinematic" |

### 3. 像素级控制需要明确的约束条件

当你需要对图像的特定部分进行精确控制时，必须使用明确的约束条件：

```
# 示例：生成一个带文字的海报
A promotional poster for a coffee shop. The text "ARTISAN BREW" in bold
serif font at the top center. Below, an illustration of a coffee cup with
steam rising. Warm earth tones. No other text. No people. No logos.
Clean layout with ample white space.
```

### 4. 文字渲染使用 quality="high"

当生成包含文字的图像时，始终使用 `quality="high"` 以获得最佳的文字清晰度：

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt='A poster with the text "HELLO WORLD" in large bold letters',
    size="1024x1024",
    quality="high",  # 文字渲染必须使用高质量
)
```

### 5. 利用 n 参数获取多个变体

使用 `n` 参数一次生成多个变体，从中选择最佳结果，提高效率：

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt="A minimalist logo for a tech startup",
    size="1024x1024",
    quality="high",
    n=4,  # 一次生成4个变体
)
```

---

> 上一章：[03-setup.md](03-setup.md) — 环境设置
>
> 下一章：[05-edit-use-cases.md](05-edit-use-cases.md) — 编辑用例
