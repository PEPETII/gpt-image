# 第2章：提示词基本原理 | Prompting Fundamentals

> 本章介绍编写高质量提示词的核心原则，包括结构化组织、约束条件、文字渲染、身份保持和迭代优化。

---

## 2.1 提示词结构化

高质量的提示词应当按逻辑层次组织信息。推荐的提示词结构为：

```
背景 (Context) → 主体 (Subject) → 细节 (Details) → 约束 (Constraints)
```

### 结构说明

| 层次 | 作用 | 示例 |
|------|------|------|
| **背景** | 设定场景环境和整体氛围 | "A modern minimalist office with natural lighting" |
| **主体** | 描述核心对象 | "a golden retriever sitting on a white desk" |
| **细节** | 添加具体特征和属性 | "wearing a blue collar with a name tag, soft focus background" |
| **约束** | 明确限制和排除条件 | "Do not include any people. Maintain photorealistic style." |

### 示例

```
Background: A cozy coffee shop interior with warm ambient lighting and wooden furniture.
Subject: A barista pouring latte art into a ceramic cup.
Details: Steaming milk, heart-shaped latte pattern, marble countertop, shallow depth of field.
Constraints: No text or logos visible. Photorealistic style only. Warm color palette.
```

> **关键要点**：结构化的提示词让模型更容易理解你的意图，从而生成更符合预期的图像。

---

## 2.2 明确约束条件

始终在提示词中列出"不应做什么"（negative constraints）。约束条件是控制输出质量的关键手段。

### 为什么约束条件重要

- 模型在没有明确约束时可能会添加你不想要的元素
- 约束条件帮助模型理解你的精确意图
- 在编辑场景中，约束条件确保不应改变的部分保持不变

### 约束条件示例

| 场景 | 约束条件示例 |
|------|-------------|
| 产品摄影 | "No shadows except natural contact shadows. Clean white background only." |
| 人物肖像 | "Do not alter facial features. Maintain original skin tone." |
| 建筑设计 | "No people in the scene. Preserve original building proportions." |
| 文字渲染 | "Do not add any decorative elements around the text." |

### 编辑场景中的约束

在编辑模式下，约束条件尤为重要。你需要明确告诉模型：

```
What to change: Replace the red sofa with a blue one.
What to preserve: Keep the room layout, lighting, floor, and all other furniture unchanged.
```

---

## 2.3 文字渲染

`gpt-image-2` 具备强大的文字渲染能力，但需要精确的提示词来获得最佳效果。

### 文字渲染最佳实践

| 技巧 | 说明 |
|------|------|
| **用引号精确引用** | 将需要渲染的文字用引号包裹，如 `"Hello World"` |
| **指定字体风格** | 明确字体类型，如 "bold sans-serif font"、"elegant serif typeface" |
| **指定文字位置** | 告诉模型文字应出现在图像的哪个位置 |
| **使用 quality="high"** | 小文本和精细文字需要高质量模式 |

### 示例

```
A minimalist poster with the text "SPRING SALE" in large bold sans-serif font
centered at the top. Below the text, a simple illustration of cherry blossoms.
Clean white background. The text should be crisp and perfectly legible.
```

### 文字渲染注意事项

- 短文本（1-5个单词）效果最佳
- 复杂排版（多行、多字体）可能需要多次迭代
- 英文文字渲染效果优于其他语言
- 使用 `quality="high"` 可以显著提升小文本的清晰度

---

## 2.4 身份保持

在编辑图像时，保持人物或物体的身份一致性是常见需求。

### 身份保持技巧

| 技巧 | 说明 |
|------|------|
| **锁定面部特征** | "Preserve the person's facial features exactly" |
| **锁定体型** | "Maintain the original body proportions" |
| **锁定姿势** | "Keep the same pose and posture" |
| **锁定服装** | "Do not change the clothing" |
| **使用 input_fidelity="high"** | 高保真度参数最大程度保留输入图像细节 |

### 示例

```
Keep the person's face, hairstyle, and body type exactly the same as in the
original image. Only change the background to a beach sunset. Maintain the
original lighting on the person's face.
```

### 适用场景

- 虚拟试穿（更换服装但保持人物身份）
- 场景替换（更换背景但保持人物不变）
- 风格迁移（改变艺术风格但保持主体可识别）

---

## 2.5 质量选择

`quality` 参数直接影响输出质量和生成速度，选择合适的质量等级至关重要。

### 质量等级选择指南

| quality | 适用场景 | 不适用场景 |
|---------|----------|------------|
| `"high"` | 包含小文本的海报、精细产品图、需要高细节的场景 | 快速预览、大批量生成 |
| `"medium"` | 大多数常规场景、社交媒体图片、一般创意工作 | 需要极致细节的场景 |
| `"low"` | 快速原型迭代、概念验证、低精度预览 | 最终交付物、文字渲染 |

### 决策流程

```
需要渲染文字？ → 是 → quality="high"
需要极致细节？ → 是 → quality="high"
一般创意用途？ → 是 → quality="medium"
快速预览迭代？ → 是 → quality="low"
```

---

## 2.6 迭代优化

获得理想图像通常需要多次迭代。遵循以下原则可以提高迭代效率：

### 迭代原则

| 原则 | 说明 |
|------|------|
| **小幅调整** | 每次只修改提示词的一小部分，观察效果变化 |
| **避免大幅重写** | 不要每次都从头重写提示词，逐步微调更高效 |
| **记录有效修改** | 记录哪些修改产生了正面效果，便于后续复用 |
| **利用 n 参数** | 使用 `n` 参数一次生成多个变体，从中选择最佳结果 |

### 迭代示例

```
第1轮: "A cat sitting on a table"
第2轮: "A fluffy orange cat sitting on a wooden table"  (+ 颜色、材质)
第3轮: "A fluffy orange cat sitting on a wooden table, soft morning light"  (+ 光线)
第4轮: "A fluffy orange cat sitting on a wooden table, soft morning light, shallow depth of field"  (+ 构图)
```

> **关键要点**：每次只添加或修改一个维度（颜色、光线、构图、风格等），这样你可以清楚地知道每个修改的效果。

---

## 2.7 核心原则总结

编写高质量提示词的核心在于 **清楚区分什么应该改变、什么必须保持不变**：

| 原则 | Generate 模式 | Edit 模式 |
|------|--------------|-----------|
| **明确主体** | 清晰描述要生成的核心对象 | 明确指出要修改的部分 |
| **设定约束** | 列出不应出现的元素 | 列出必须保持不变的部分 |
| **提供细节** | 描述光线、构图、氛围、风格 | 描述期望的修改效果 |
| **迭代优化** | 小幅调整，逐步逼近理想结果 | 小幅调整，逐步逼近理想结果 |

---

> 上一章：[01-introduction.md](01-introduction.md) — 引言
>
> 下一章：[03-setup.md](03-setup.md) — 环境设置
