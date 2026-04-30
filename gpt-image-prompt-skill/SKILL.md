---
name: gpt-image-prompt
description: "Generate professional GPT Image 2 prompts based on OpenAI's official prompting guide. Use this skill when the user wants to create AI-generated images, needs help writing image prompts, asks about GPT Image / DALL-E prompting techniques, or wants to generate/edit images using OpenAI's image models. Supports both generate (text→image) and edit (text+image→image) modes with structured, production-quality prompt output."
triggers:
  - "generate image prompt"
  - "write image prompt"
  - "GPT Image prompt"
  - "DALL-E prompt"
  - "create image"
  - "AI image prompt"
  - "图片提示词"
  - "图像生成提示词"
  - "GPT Image"
version: 1.0.0
category: automation
tags:
  - "image-generation"
  - "prompt-engineering"
  - "openai"
  - "gpt-image"
  - "visual-ai"
risk: safe
---

# GPT Image Prompt Generator

基于 OpenAI 官方《GPT Image Generation Models Prompting Guide》的专业提示词生成技能。帮助用户按照官方最佳实践创建高质量、可控的 GPT Image 2 提示词。

## Purpose

This skill guides users through creating professional-grade prompts for OpenAI's GPT Image 2 model. It follows the official prompting guide's methodology — structured prompts, explicit constraints, and mode-specific techniques — to produce reliable, production-quality results.

## When to Use This Skill

Use this skill when the user:

- Wants to generate AI images using GPT Image 2 / DALL-E
- Needs help writing or improving image prompts
- Asks about image prompting best practices
- Wants to create specific types of images (logos, ads, UI mockups, infographics, etc.)
- Needs to edit existing images (style transfer, object removal, background change, etc.)
- Wants to add text to images
- Asks about `quality`, `input_fidelity`, `size`, or other GPT Image API parameters
- Mentions keywords like "提示词", "prompt", "出图", "AI绘画", "图像生成"

## Workflow

### Step 1: Understand the User's Need

Ask the user (or infer from context) the following:

1. **Mode**: Generate (text → image) or Edit (text + image → image)?
2. **Scene/Use Case**: What type of image? (See Scene Catalog below)
3. **Subject**: What is the main subject/content?
4. **Style**: Any specific visual style? (photorealistic, illustration, flat design, etc.)
5. **Constraints**: Text to include? Things to avoid? Specific requirements?
6. **Output Size**: Portrait, landscape, square, or custom?

If the user's request is vague, use AskUserQuestion to clarify the mode and scene type before proceeding.

### Step 2: Select the Appropriate Template

Based on the user's scene type, select the matching template from `resources/prompt-templates.md`. Each template includes:

- Structured prompt format (Scene / Style / Mood / Constraints)
- Key parameters recommendation
- Common pitfalls to avoid

### Step 3: Generate the Prompt

Follow these principles when constructing the prompt:

#### For Generate Mode (text → image):

1. **Structure the prompt** in this order:
   - Background/Environment → Subject → Key Details → Constraints
2. **Be specific** about materials, textures, lighting, and atmosphere
3. **Specify composition**: camera angle, lens, depth of field, lighting direction
4. **Add explicit constraints**: "No watermarks", "No extra text", "No logos"
5. **For text in images**: use quotes, specify "EXACT, verbatim", define font style

#### For Edit Mode (text + image → image):

1. **Clearly separate** what should CHANGE vs. what must STAY THE SAME
2. **Lock identity features** when editing people (face, body, pose, hairstyle)
3. **Recommend `input_fidelity="high"`** for precision edits
4. **Use "ONLY"** to restrict changes to specific elements
5. **Reiterate constraints** in every iteration to prevent drift

### Step 4: Recommend API Parameters

Based on the scene type, recommend appropriate parameters:

| Scene | quality | input_fidelity | size | background | n |
|-------|---------|----------------|------|------------|---|
| Infographics | high | - | 1536x1024 | - | 1 |
| Photorealistic | high | - | 1024x1536 | - | 1 |
| Logo | medium | - | 1024x1024 | opaque | 4 |
| Ads | high | - | 1536x1024 | - | 1 |
| UI Mockups | high | - | 1024x1536 | - | 1 |
| Scientific/Edu | high | - | 1536x1024 | - | 1 |
| Slides/Charts | high | - | 1536x1024 | - | 1 |
| Style Transfer | medium | - | 1024x1536 | - | 1 |
| Virtual Try-On | medium | high | 1024x1536 | - | 1 |
| Drawing→Image | high | high | 1536x1024 | - | 1 |
| Product Mockup | medium | high | 1024x1024 | opaque | 1 |
| Marketing Text | high | - | 1536x1024 | - | 1 |
| Lighting/Weather | medium | high | 1536x1024 | - | 1 |
| Object Removal | medium | high | 1024x1536 | - | 1 |
| Person Insert | high | high | 1536x1024 | - | 1 |
| Multi-Image | medium | high | 1024x1536 | - | 1 |
| Interior Swap | medium | high | 1536x1024 | - | 1 |

### Step 5: Output Format

Present the final result to the user in this format:

```
## 📋 提示词 / Prompt

\```english
[Complete English prompt]
\```

### 中文翻译

\```
[Chinese translation]
\```

## ⚙️ 推荐参数

| 参数 | 值 | 说明 |
|------|-----|------|
| model | gpt-image-2 | 最新模型 |
| quality | [value] | [reason] |
| input_fidelity | [value] | [reason] |
| size | [value] | [reason] |
| [other params] | [value] | [reason] |

## 💡 关键技巧

- [Tip 1]
- [Tip 2]
- [Tip 3]

## 🐍 Python 代码

\```python
from openai import OpenAI
import base64, os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

result = client.images.[generate|edit](
    model="gpt-image-2",
    prompt="""[prompt]""",
    [image=[...],]  # edit mode only
    [input_fidelity="[value]",]  # edit mode only
    size="[size]",
    quality="[quality]",
    [n=[value],]
    [background="[value]",]
)

# Save image
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
\```
```

## Scene Catalog

### Generate Mode (text → image)

| # | Scene | Description | Key Technique |
|---|-------|-------------|---------------|
| G1 | 信息图表 | Technical diagrams, flowcharts, process illustrations | List all components, use quality="high" |
| G2 | 图片翻译 | Translate text within images to another language | "Do not change any other aspect" |
| G3 | 照片级写实 | Photorealistic photographs with natural feel | "photorealistic" + material textures + camera specs |
| G4 | 世界知识 | Historical/scientific scenes using GPT's knowledge | Specific time, place, "period-accurate" |
| G5 | Logo生成 | Brand logos, icons, visual identity | "original, non-infringing", flat design, n=4 |
| G6 | 广告生成 | Brand ads, fashion shots, marketing visuals | Creative brief style, tagline in quotes |
| G7 | 故事转漫画 | Comic strips, storyboards, visual narratives | Numbered panels, action-oriented descriptions |
| G8 | UI模型 | App interfaces, web mockups, product screens | "Like it already exists", layout + spacing |
| G9 | 科学/教育 | Educational diagrams, classroom materials | Audience + objectives + visual format |
| G10 | 幻灯片/图表 | Pitch decks, data visualization, presentations | Product spec style, exact numbers |

### Edit Mode (text + image → image)

| # | Scene | Description | Key Technique |
|---|-------|-------------|---------------|
| E1 | 风格迁移 | Apply style from reference image to new content | "Use the same style" + hard constraints |
| E2 | 虚拟试穿 | Dress a person in provided clothing | Lock ALL identity features, multi-image input |
| E3 | 素描转图像 | Render sketches into photorealistic images | "Preserve layout" + "Do not add new elements" |
| E4 | 产品模型 | Extract product onto clean background | background="opaque", "crisp silhouette" |
| E5 | 营销创意 | Create ads with real readable text | "EXACT, verbatim" + font specification |
| E6 | 光照天气 | Transform lighting/weather of a scene | Only change environmental conditions |
| E7 | 物品移除 | Remove specific objects from images | "Do not change anything else" + input_fidelity="high" |
| E8 | 人物插入 | Place a person into a new scene | Grounded photography, avoid cinematic |
| E9 | 多图合成 | Combine elements from multiple images | "from image X" + "into image Y" references |

## Prompt Structure Patterns

### Pattern A: Structured Prompt (for complex scenes)

```
[Scene description]

Subject:
[Detailed subject description]

Style:
[Visual style, medium, reference]

Mood:
[Atmosphere, emotion, tone]

Constraints:
- [Constraint 1]
- [Constraint 2]
- No watermarks, no logos
```

### Pattern B: Creative Brief (for ads/marketing)

```
[Brand/Client]: [name]
[Target audience]: [description]
[Concept]: [idea]
[Tagline]: "[exact text]"
[Visual direction]: [style, composition, color]
[Constraints]: [what to avoid]
```

### Pattern C: Specification (for UI/slides/charts)

```
Create a [deliverable type] for [product].

Include:
- [Element 1]: [details]
- [Element 2]: [details]
- [Element 3]: [details]

Design requirements:
- [Layout spec]
- [Color scheme]
- [Typography]
- [What to avoid]
```

### Pattern D: Precision Edit (for image editing)

```
[Action verb] [target] [from/in] [location].

Preserve:
- [Element 1]
- [Element 2]
- [Element 3]

Do not change anything else.
```

## Best Practices

1. **Always write prompts in English** — GPT Image 2 understands English best
2. **Structure over length** — A well-organized short prompt beats a rambling long one
3. **Explicit constraints** — Always state what NOT to do, not just what to do
4. **Iterate with small changes** — Don't rewrite the entire prompt; tweak one element at a time
5. **Separate change from constancy** — In edit mode, clearly distinguish what changes vs. what stays
6. **Use "ONLY" for surgical edits** — "replace ONLY X" is stronger than "replace X"
7. **Quote exact text** — For text-in-image, always use quotes and "EXACT, verbatim"
8. **Specify font for text** — "bold sans-serif, high contrast, centered, clean kerning"
9. **Lock identity in edits** — List every feature that must not change when editing people
10. **Match lighting in composites** — When combining images, explicitly request matched lighting/shadows

## Limitations

- This skill generates prompts for GPT Image 2; other models may need adjustments
- Text rendering in images may not be perfect on first try — iterate
- Complex multi-image workflows may require multiple API calls
- The skill provides prompt guidance, not actual image generation (requires OpenAI API access)
