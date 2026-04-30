# 第5章：编辑用例 | Edit Use Cases

> 本章介绍 Edit 模式（image editing）的 9 个核心用例，涵盖风格迁移、虚拟试穿、素描转图像、产品模型、营销创意、光照天气变换、物品移除、人物插入场景以及多图合成场景。

---

## 5.1 风格迁移 | Style Transfer

将一张图像的艺术风格应用到另一张图像上，或对现有图像进行风格变换（如将照片转为油画风格）。

> 风格迁移可以在保留原始图像内容结构的同时，赋予其全新的艺术表现形式，支持油画、水彩、素描、赛博朋克等多种风格。

**提示词模板**：[prompts/edit/style-transfer.md](../prompts/edit/style-transfer.md)

---

## 5.2 虚拟试穿 | Virtual Try-On

将服装或配饰虚拟地"穿"到人物图像上，保持人物的身份特征和自然姿态。

> 该用例在电商和时尚领域有广泛应用，可以快速展示不同服装的上身效果，无需实际拍摄。

**提示词模板**：[prompts/edit/virtual-try-on.md](../prompts/edit/virtual-try-on.md)

---

## 5.3 素描转图像 | Drawing to Image

将简单的素描、线稿或草图转化为完整的彩色图像，保持原始构图和设计意图。

> 该用例适合设计师快速将概念草图转化为高保真效果图，大幅加速设计迭代流程。

**提示词模板**：[prompts/edit/drawing-to-image.md](../prompts/edit/drawing-to-image.md)

---

## 5.4 产品模型 | Product Mockups

将产品图像放置到干净的背景中，或生成专业的产品展示效果（如产品在特定场景中的展示）。

> 模型能够精确抠出产品并生成专业的展示效果，包括阴影、反射和环境光照等细节。

**提示词模板**：[prompts/edit/product-mockups.md](../prompts/edit/product-mockups.md)

---

## 5.5 营销创意 | Marketing Creatives

基于现有素材生成包含真实文字的营销创意图像，如社交媒体帖子、广告横幅和宣传海报。

> 该用例展示了模型在保持品牌一致性的同时生成多样化营销内容的能力。

**提示词模板**：[prompts/edit/marketing-creatives.md](../prompts/edit/marketing-creatives.md)

---

## 5.6 光照天气变换 | Lighting & Weather

改变图像中的光照条件和天气状况，如将白天变为夜晚、晴天变为雨天、添加雾气效果等。

> 模型能够理解场景的物理光照特性，生成自然的光照和天气变换效果。

**提示词模板**：[prompts/edit/lighting-weather.md](../prompts/edit/lighting-weather.md)

---

## 5.7 物品移除 | Object Removal

从图像中移除不需要的物体，并智能填充被移除物体所在的区域，使画面保持自然。

> 该用例适合清理照片中的干扰元素，如移除背景中的人物、电线、垃圾桶等。

**提示词模板**：[prompts/edit/object-removal.md](../prompts/edit/object-removal.md)

---

## 5.8 人物插入场景 | Insert Person into Scene

将人物图像自然地插入到目标场景中，保持人物的身份特征并与场景的光照和透视相匹配。

> 该用例可以生成逼真的合成照片，适合创意摄影、广告制作和概念验证。

**提示词模板**：[prompts/edit/insert-person-scene.md](../prompts/edit/insert-person-scene.md)

---

## 5.9 多图合成 | Multi-Image Compositing

利用多张输入图像进行合成操作，将不同图像的元素组合成一张新的图像。

> 该用例支持多种合成场景，如将产品与模特合成、将人物与背景合成等，是 Edit 模式中最强大的功能之一。

**提示词模板**：[prompts/edit/multi-image-compositing.md](../prompts/edit/multi-image-compositing.md)

---

## 用例总览表

| 编号 | 用例 | 提示词模板 | 推荐 input_fidelity |
|------|------|-----------|---------------------|
| 5.1 | 风格迁移 | [style-transfer.md](../prompts/edit/style-transfer.md) | `"medium"` |
| 5.2 | 虚拟试穿 | [virtual-try-on.md](../prompts/edit/virtual-try-on.md) | `"high"` |
| 5.3 | 素描转图像 | [drawing-to-image.md](../prompts/edit/drawing-to-image.md) | `"high"` |
| 5.4 | 产品模型 | [product-mockups.md](../prompts/edit/product-mockups.md) | `"high"` |
| 5.5 | 营销创意 | [marketing-creatives.md](../prompts/edit/marketing-creatives.md) | `"medium"` |
| 5.6 | 光照天气变换 | [lighting-weather.md](../prompts/edit/lighting-weather.md) | `"high"` |
| 5.7 | 物品移除 | [object-removal.md](../prompts/edit/object-removal.md) | `"high"` |
| 5.8 | 人物插入场景 | [insert-person-scene.md](../prompts/edit/insert-person-scene.md) | `"high"` |
| 5.9 | 多图合成 | [multi-image-compositing.md](../prompts/edit/multi-image-compositing.md) | `"high"` |

---

## 编辑模式通用最佳实践

### 1. input_fidelity="high" 是精细编辑的关键参数

`input_fidelity` 参数控制模型对输入图像的保留程度，是编辑成功的核心参数：

| input_fidelity | 效果 | 适用场景 |
|----------------|------|----------|
| `"high"` | 最大程度保留输入图像的细节 | 物体替换、物品移除、人物身份保持 |
| `"medium"` | 平衡保留与创新 | 风格迁移、光照变换、一般编辑 |
| `"low"` | 允许较大幅度的改动 | 大范围重绘、创意性编辑 |

```python
# 精细编辑示例：替换物体但保持其他一切不变
response = client.images.edit(
    model="gpt-image-2",
    prompt="Replace the red chair with a blue chair. Keep everything else unchanged.",
    image=image_data,
    input_fidelity="high",  # 关键参数
    size="1024x1024",
    quality="medium",
)
```

### 2. 明确区分变与不变是编辑成功的核心

在编辑提示词中，必须清楚地告诉模型：

- **什么应该改变**（What to change）
- **什么必须保持不变**（What to preserve）

```
# 好的编辑提示词示例
Replace the background with a tropical beach scene.
Preserve the person's face, pose, clothing, and lighting exactly.
The person should appear naturally in the new scene with matching shadows.
```

```
# 不好的编辑提示词示例（缺乏约束）
Change the background to a beach.
# 问题：没有告诉模型保持人物的哪些特征
```

### 3. 多图输入支持高级合成场景

Edit 模式支持多张输入图像，适用于以下场景：

| 场景 | 输入图像 | 说明 |
|------|----------|------|
| 风格迁移 | 参考风格图 + 内容图 | 将风格图的艺术风格应用到内容图 |
| 虚拟试穿 | 人物图 + 服装图 | 将服装自然地穿到人物身上 |
| 多图合成 | 多张素材图 | 将不同图像的元素组合成新图像 |
| 产品模型 | 产品图 + 场景图 | 将产品放置到目标场景中 |

### 4. 编辑提示词的结构化写法

推荐的编辑提示词结构：

```
1. 明确操作：要做什么修改
2. 保留约束：什么必须保持不变
3. 质量要求：期望的输出质量标准
4. 风格约束：不应出现的元素或风格
```

示例：

```
Operation: Replace the wooden table with a glass table.
Preserve: Keep the room layout, wall color, floor, lighting, and all other
furniture exactly the same.
Quality: Photorealistic with natural reflections on the glass surface.
Constraints: No other changes. Maintain the original camera angle and perspective.
```

### 5. 迭代编辑策略

对于复杂的编辑任务，建议分步进行：

```
第1步：大范围修改（如更换背景）
第2步：细节调整（如调整光照匹配）
第3步：精修（如修正阴影和反射）
```

每一步都使用 `input_fidelity="high"` 来确保前一步的成果被保留。

---

> 上一章：[04-generate-use-cases.md](04-generate-use-cases.md) — 生成用例
>
> 下一章：[06-additional-use-cases.md](06-additional-use-cases.md) — 其他高价值用例
