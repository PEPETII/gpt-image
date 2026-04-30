# 第6章：其他高价值用例 | Additional Use Cases

> 本章介绍 4 个高级用例，展示 GPT 图像模型在复杂场景下的强大能力，包括室内设计替换、3D 立体贺卡、收藏级手办/毛绒钥匙扣以及儿童绘本艺术（多图工作流）。

---

## 6.1 室内设计替换 | Interior Design Replacement

### 场景说明

利用 Edit 模式对室内设计照片进行手术级精确编辑，只替换目标物体（如家具、装饰品），同时完美保留房间布局、光照、阴影和周围环境。该用例展示了 `gpt-image-2` 在精细编辑方面的卓越能力。

### 关键技巧

- 使用 `input_fidelity="high"` 确保最大程度保留原始图像
- 明确列出所有需要保留的元素（相机角度、光照、阴影、周围物体）
- 使用 "ONLY" 强调只修改目标物体
- 指定物理效果（contact shadows、fabric texture）以增强真实感

### 提示词

```text
In this room photo, replace ONLY white chairs with chairs made of wood. Preserve camera angle, room lighting, floor shadows, and surrounding objects. Keep all other aspects of the image unchanged. Photorealistic contact shadows and fabric texture.
```

### 提示词结构分析

| 部分 | 内容 | 作用 |
|------|------|------|
| **操作指令** | "replace ONLY white chairs with chairs made of wood" | 明确只替换白色椅子为木椅 |
| **保留约束** | "Preserve camera angle, room lighting, floor shadows, and surrounding objects" | 列出所有必须保持不变的元素 |
| **全局约束** | "Keep all other aspects of the image unchanged" | 兜底约束，确保无意外修改 |
| **质量要求** | "Photorealistic contact shadows and fabric texture" | 指定物理效果，增强真实感 |

### 推荐参数

```python
response = client.images.edit(
    model="gpt-image-2",
    prompt="In this room photo, replace ONLY white chairs with chairs made of wood. Preserve camera angle, room lighting, floor shadows, and surrounding objects. Keep all other aspects of the image unchanged. Photorealistic contact shadows and fabric texture.",
    image=image_data,
    input_fidelity="high",
    size="1536x1024",
    quality="high",
)
```

---

## 6.2 3D 立体节日贺卡 | 3D Pop-up Holiday Card

### 场景说明

生成具有触觉真实感的 3D 立体节日贺卡，强调纸张的层次感、纤维质感和物理深度。该用例展示了模型在模拟物理材质和 3D 效果方面的能力。

### 关键技巧

- 使用结构化提示词格式（Scene / Mood / Style / Constraints）组织复杂信息
- 强调物理材质细节（paper layers、fibers、depth、tactile quality）
- 明确光照和阴影效果以增强 3D 立体感
- 使用 "Original design only / No trademarks" 避免版权问题

### 提示词

```text
Scene: A 3D pop-up holiday card with a winter village scene. The card is open, standing upright on a wooden table. Inside, layered paper cutouts create a snowy village with small houses, a church with a steeple, pine trees covered in snow, and tiny warm lights in the windows. A paper moon hangs from the top fold. Gentle snowfall made of tiny white paper confetti.

Mood: Warm, nostalgic, magical. The contrast between the cozy warm lights from the village and the cool blue-white snow creates an enchanting atmosphere. The tactile quality of real paper layers gives it a handmade, artisanal feel.

Style: Handcrafted paper art style. Visible paper fibers and subtle texture on all surfaces. Each layer has slight shadow depth where it connects to the layer behind it. Soft ambient lighting from above, warm point lights from the village windows. The outer card surface is a deep forest green with a subtle linen texture. Slight wear on the card edges suggests it's been treasured and opened many times.

Constraints: Original design only. No trademarks, no copyrighted characters. No text. Photorealistic paper textures. The card must look like a real physical object that could be touched and held. Maintain consistent paper grain direction across all layers.
```

### 提示词结构分析

| 部分 | 内容 | 作用 |
|------|------|------|
| **Scene** | 贺卡的完整场景描述 | 设定场景内容和空间布局 |
| **Mood** | 温暖、怀旧、魔幻的情感基调 | 定义视觉氛围和情感传达 |
| **Style** | 手工纸艺风格、纸张纤维、阴影层次 | 指定艺术风格和物理材质细节 |
| **Constraints** | 原创设计、无版权、无文字、真实纸张质感 | 明确限制条件和质量标准 |

### 推荐参数

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt="Scene: A 3D pop-up holiday card with a winter village scene...",
    size="1024x1536",
    quality="high",
)
```

---

## 6.3 收藏级手办/毛绒钥匙扣 | Collectible Figurine / Plush Keychain

### 场景说明

以高端产品摄影的风格生成收藏级手办或毛绒钥匙扣的图像，强调材质质感、光影效果和展示品质。该用例展示了模型在产品摄影和材质渲染方面的能力。

### 关键技巧

- 使用结构化提示词格式（Concept / Style / Constraints）组织信息
- 详细描述材质特征（毛绒质感、缝线细节、光泽度）
- 指定摄影参数（镜头、光线、背景）以获得专业产品摄影效果
- 明确 "Original design only / No trademarks" 避免版权问题

### 提示词

```text
Concept: A collectible plush keychain of a cute round cat character. The cat has large sparkling eyes, tiny pink nose, small pointed ears, and a fluffy tail. It's wearing a tiny red scarf. The plush is made of ultra-soft premium polyester with visible stitching details. A shiny metal keyring is attached through a fabric loop on top. The character is sitting on a circular display stand.

Style: High-end product photography. Soft studio lighting from the upper left with a subtle fill light from the right. Clean gradient background transitioning from soft lavender to white. Shot with a macro lens at f/2.8, creating a shallow depth of field that blurs the background while keeping the character razor-sharp. Subtle reflections on the metal keyring. The plush texture should look so realistic that viewers can almost feel the softness.

Constraints: Original character design only. No trademarks, no copyrighted characters, no references to existing IP. No text or logos. The character must look appealing and huggable. Maintain consistent lighting and shadows. Photorealistic rendering of all materials.
```

### 提示词结构分析

| 部分 | 内容 | 作用 |
|------|------|------|
| **Concept** | 手办/钥匙扣的完整外观描述 | 定义产品的视觉设计和组成元素 |
| **Style** | 高端产品摄影风格、光线、镜头参数 | 指定摄影风格和技术参数 |
| **Constraints** | 原创设计、无版权、无文字、真实材质渲染 | 明确限制条件和质量标准 |

### 推荐参数

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt="Concept: A collectible plush keychain of a cute round cat character...",
    size="1024x1024",
    quality="high",
)
```

---

## 6.4 儿童绘本艺术（多图工作流）| Children's Picture Book Art (Multi-Image Workflow)

### 场景说明

使用两步法工作流创建儿童绘本，通过角色锚点（Character Anchor）确保跨场景的角色一致性。该用例展示了如何通过多步骤工作流实现复杂的创意项目。

### 关键技巧

- **两步法工作流**：先建立角色锚点，再基于锚点生成故事延续
- 第一步生成角色参考图，第二步将参考图作为输入进行编辑
- 使用 `input_fidelity="high"` 确保角色特征在所有场景中保持一致
- 保持统一的画风和色彩方案

### Step 1：角色锚点（Character Anchor）

首先生成一张清晰的角色参考图，作为后续所有场景的基础：

```text
A cheerful young girl with curly brown hair, big brown eyes, wearing a yellow raincoat and red rain boots. She is standing in a field of colorful flowers, smiling at the camera. Children's book illustration style with soft watercolor textures, warm pastel colors, and gentle outlines. Simple, clean background with a light blue sky.
```

```python
# Step 1: 生成角色锚点
response = client.images.generate(
    model="gpt-image-2",
    prompt="A cheerful young girl with curly brown hair, big brown eyes, wearing a yellow raincoat and red rain boots...",
    size="1024x1024",
    quality="high",
)

# 保存角色锚点
with open("character_anchor.png", "wb") as f:
    f.write(response.data[0].b64_json_bytes)
```

### Step 2：故事延续（Story Continuation）

基于角色锚点，生成不同故事场景中的角色图像：

```text
The same girl from the reference image is now walking through a magical forest. She looks curious and amazed as she discovers glowing mushrooms and fireflies around her. Children's book illustration style with soft watercolor textures, warm pastel colors, and gentle outlines. Preserve the girl's exact appearance: curly brown hair, brown eyes, yellow raincoat, red rain boots.
```

```python
# Step 2: 基于角色锚点生成故事场景
with open("character_anchor.png", "rb") as f:
    anchor_data = f.read()

response = client.images.edit(
    model="gpt-image-2",
    prompt="The same girl from the reference image is now walking through a magical forest...",
    image=anchor_data,
    input_fidelity="high",  # 关键：保持角色一致性
    size="1024x1024",
    quality="high",
)

with open("story_scene_1.png", "wb") as f:
    f.write(response.data[0].b64_json_bytes)
```

### 工作流示意

```
Step 1: Generate Character Anchor
  ┌─────────────────┐
  │  Text Prompt     │ ──→ gpt-image-2 (generate) ──→ character_anchor.png
  └─────────────────┘

Step 2: Generate Story Scenes
  ┌─────────────────┐
  │  character_      │
  │  anchor.png      │ ──→ gpt-image-2 (edit) ──→ story_scene_1.png
  │  + Text Prompt   │
  └─────────────────┘
  ┌─────────────────┐
  │  character_      │
  │  anchor.png      │ ──→ gpt-image-2 (edit) ──→ story_scene_2.png
  │  + Text Prompt   │
  └─────────────────┘
  ┌─────────────────┐
  │  character_      │
  │  anchor.png      │ ──→ gpt-image-2 (edit) ──→ story_scene_3.png
  │  + Text Prompt   │
  └─────────────────┘
```

### 推荐参数

| 步骤 | 模式 | quality | input_fidelity | 说明 |
|------|------|---------|----------------|------|
| Step 1 | Generate | `"high"` | N/A | 生成高质量角色锚点 |
| Step 2 | Edit | `"high"` | `"high"` | 最大程度保持角色一致性 |

---

## 高级用例通用最佳实践

### 1. 结构化提示词适用于复杂场景

对于复杂的生成任务，使用结构化的提示词格式可以显著提升输出质量：

| 格式 | 适用场景 | 示例 |
|------|----------|------|
| **Scene / Mood / Style / Constraints** | 艺术创作、场景生成 | 3D 立体贺卡 |
| **Concept / Style / Constraints** | 产品设计、角色设计 | 手办/钥匙扣 |
| **Background / Subject / Details / Constraints** | 通用场景 | 室内设计替换 |

### 2. 多步骤工作流实现跨场景一致性

当需要在不同场景中保持角色或物体的视觉一致性时，使用多步骤工作流：

```
步骤 1：生成锚点图像（角色/物体参考图）
步骤 2：基于锚点生成各场景变体（使用 Edit 模式 + input_fidelity="high"）
步骤 3：可选的精修步骤（进一步调整细节）
```

### 3. 明确 "Original design only / No trademarks" 避免版权问题

在生成可能涉及品牌、角色或 IP 的图像时，始终在约束条件中明确声明：

```text
Constraints: Original design only. No trademarks, no copyrighted characters,
no references to existing IP.
```

### 4. 物理效果描述增强真实感

当需要生成具有真实感的图像时，详细描述物理效果可以显著提升质量：

| 物理效果 | 描述示例 |
|----------|----------|
| **阴影** | "Photorealistic contact shadows", "Soft ambient occlusion" |
| **材质** | "Visible paper fibers", "Ultra-soft polyester texture" |
| **反射** | "Subtle reflections on the metal keyring" |
| **光照** | "Soft studio lighting from the upper left" |
| **深度** | "Shallow depth of field", "Layered paper with shadow depth" |

---

## 用例总览表

| 编号 | 用例 | 模式 | 关键技术 |
|------|------|------|----------|
| 6.1 | 室内设计替换 | Edit | `input_fidelity="high"` + 精确约束 |
| 6.2 | 3D 立体节日贺卡 | Generate | 结构化提示词（Scene/Mood/Style/Constraints） |
| 6.3 | 收藏级手办/毛绒钥匙扣 | Generate | 结构化提示词（Concept/Style/Constraints） |
| 6.4 | 儿童绘本艺术 | Generate + Edit | 两步法工作流 + 角色锚点 |

---

> 上一章：[05-edit-use-cases.md](05-edit-use-cases.md) — 编辑用例
>
> 返回目录：[README.md](README.md)
