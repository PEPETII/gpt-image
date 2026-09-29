# 1. Introduction

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## 章节目录

本章没有独立用例子章节。

## Official content

## 1. Introduction

OpenAI’s gpt-image generation models are designed for production-quality visuals and highly controllable creative workflows. They are well-suited for both professional design tasks and iterative content creation, and support both high-quality rendering and lower-latency use cases depending on the workflow.

Key Capabilities include:

- **High-fidelity photorealism** with natural lighting, accurate materials, and rich color rendering
- **Flexible quality–latency tradeoffs**, allowing faster generation at lower settings while still exceeding the visual quality of prior-generation image models
- **Robust facial and identity preservation** for edits, character consistency, and multi-step workflows
- **Transparent-background PNG and WebP assets (preview)** with `gpt-image-2` for reusable logos, product cutouts, stickers, and presentation graphics
- **Reliable text rendering** with crisp lettering, consistent layout, and strong contrast inside images
- **Complex structured visuals**, including infographics, diagrams, and multi-panel compositions
- **Precise style control and style transfer** with minimal prompting, supporting everything from branded design systems to fine-art styles
- **Strong real-world knowledge and reasoning**, enabling accurate depictions of objects, environments, and scenarios

This guide highlights prompting patterns, best practices, and example prompts drawn from real production use cases for `gpt-image-2`. It is our most capable image model, with stronger image quality, improved editing performance, and broader support for production workflows. The `low` quality setting is especially strong for latency-sensitive use cases, while `medium` and `high` remain good fits when maximum fidelity matters.

## 1.1 OpenAI Image Model Parameters

This section is a reference for the image models covered in this guide, focused on:

- model name
- supported `quality` values
- supported `input_fidelity` values
- supported `size` / resolution behavior
- `background` and `output_format` requirements for transparent assets
- recommended use cases by workflow

## Model summary

As of April 21, 2026, OpenAI has the following image models available.

| Model | `quality` | `input_fidelity` | Resolutions | Recommended use |
| --- | --- | --- | --- | --- |
| `gpt-image-2` | `low`, `medium`, `high` | Disabled. `input_fidelity` does not work for this model because output is already high fidelity by default | Any resolution that satisfies the constraints below | Recommended default for new builds. Use for highest-quality generation and editing, text-heavy images, photorealism, compositing, identity-sensitive edits, and workflows where fewer retries matter more than the lowest possible cost. |
| `gpt-image-1.5` | `low`, `medium`, `high` | `low`, `high` | `1024x1024`, `1024x1536`, `1536x1024`, `auto` | Keep for existing validated workflows during migration. For new work, prefer `gpt-image-2`, especially when quality, editing reliability, or flexible sizing matter. |
| `gpt-image-1` | `low`, `medium`, `high` | `low`, `high` | `1024x1024`, `1024x1536`, `1536x1024`, `auto` | Legacy compatibility only. If you are starting a new workflow or refreshing prompts, move to `gpt-image-2`; keep `gpt-image-1` only when you need short-term stability while validating the upgrade. |
| `gpt-image-1-mini` | `low`, `medium`, `high` | `low`, `high` | `1024x1024`, `1024x1536`, `1536x1024`, `auto` | Use when cost and throughput are the main constraint: large batch variant generation, rapid ideation, previews, lightweight personalization, and draft assets that do not require the strongest generation or editing performance. |

### Transparent backgrounds with `gpt-image-2` (preview)

Transparent backgrounds are available in preview for `gpt-image-2`. To generate or edit an image with a transparent background:

- Set `background="transparent"`.
- Set `output_format="png"` (the default) or `output_format="webp"`. Both support transparency; `jpeg` does not.
- Omit `output_compression` for PNG output. WebP supports optional compression.
- Explicitly request an isolated subject on a fully transparent background, with no scenery, solid backdrop, checkerboard, or unwanted shadows.
- For edits, explicitly preserve the transparent background in each prompt so later steps do not introduce a new background.
- Keep the returned image as a PNG or WebP file and preserve its alpha channel throughout downstream processing.

### `gpt-image-2` size options

`gpt-image-2` supports any resolution passed in the `size` parameter as long as all of these constraints are met:

- Maximum edge length must be less than `3840px`
- Both edges must be a multiple of `16`
- Ratio between the long edge and short edge must not be greater than `3:1`
- Total pixels must not exceed `8,294,400`
- Total pixels must not be less than `655,360`

If the output image exceeds `2560x1440` pixels (`3,686,400` total pixels), commonly referred to as 2K, treat it as experimental because results can be more variable above this size.

### Popular `gpt-image-2` sizes

These are useful reference points that fit the constraints above:

| Label | Resolution | Notes |
| --- | --- | --- |
| HD portrait | `1024x1536` | Standard portrait option |
| HD landscape | `1536x1024` | Standard landscape option |
| Square | `1024x1024` | Good general-purpose default |
| 2K / QHD | `2560x1440` | Popular widescreen format and recommended upper reliability boundary for `gpt-image-2` |
| 4K / UHD | `3840x2160` | Experimental upper-end target. If the max-edge rule is enforced literally as `< 3840`, round down to the nearest valid size such as `3824x2144` |

### When to use which model

- Choose `gpt-image-2` as the default for most production workflows. It is the strongest overall model and the right upgrade target for teams currently using `gpt-image-1.5` or `gpt-image-1` for high-quality outputs.
- Choose `gpt-image-2` with quality: low when speed and unit economics dominate the decision. This setting has good quality for a lot of use cases and it a strong fit for high-volume generation and experimentation. You can also try `gpt-image-1-mini` for these use cases, but we have seen quality: low works just as well.
- Keep `gpt-image-1.5` or `gpt-image-1` only for backward compatibility while you validate prompt migrations, regression-test outputs, or maintain older workflows that are not yet ready to move.

### Recommended upgrade path from `gpt-image-1.5` and `gpt-image-1`

For workflows currently using `gpt-image-1.5` or `gpt-image-1`, the recommendation is:

- Upgrade to `gpt-image-2` for customer-facing assets, photorealistic generation, editing-heavy flows, brand-sensitive creative, text-in-image work, and any workflow where better first-pass quality reduces manual review or reruns.
- Consider `gpt-image-1-mini` instead of legacy models only when the main goal is lowering cost for large batches of exploratory or lower-stakes images.
- During migration, keep prompts largely the same at first, then retune only after you have compared output quality, latency, and retry rates on your real workload.

## 中文翻译

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

