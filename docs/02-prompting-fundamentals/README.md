# 2. Prompting Fundamentals

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## 章节目录

本章没有独立用例子章节。

## Official content

## 2. Prompting Fundamentals

The following prompting fundamentals are applicable to GPT image generation models. They are based on patterns that showed up repeatedly in alpha testing across generation, edits, infographics, ads, human images, UI mockups, and compositing workflows.

- **Structure + goal:** Write prompts in a consistent order (background/scene → subject → key details → constraints) and include the intended use (ad, UI mock, infographic) to set the “mode” and level of polish. For complex requests, use short labeled segments or line breaks instead of one long paragraph.
- **Prompt format:** Use the format that is easiest to maintain. Minimal prompts, descriptive paragraphs, JSON-like structures, instruction-style prompts, and tag-based prompts can all work well as long as the intent and constraints are clear. For production systems, prioritize a skimmable template over clever prompt syntax.
- **Specificity + quality cues:** Be concrete about materials, shapes, textures, and the visual medium (photo, watercolor, 3D render), and add targeted “quality levers” only when needed (e.g., *film grain*, *textured brushstrokes*, *macro detail*). For photorealism, include the word “photorealistic” directly in the prompt to strongly engage the model’s photorealistic mode. Similar phrases like “real photograph,” “taken on a real camera,” “professional photography,” or “iPhone photo” can also help, but detailed camera specs may be interpreted loosely, so use them mainly for high-level look and composition rather than exact physical simulation.
- **Latency vs fidelity:** For latency-sensitive or high-volume use cases, start with `quality="low"` and evaluate whether it meets your visual requirements. In many cases, it provides sufficient fidelity with significantly faster generation. For small or dense text, detailed infographics, close-up portraits, identity-sensitive edits, and high-resolution outputs, compare `medium` or `high` before shipping.
- **Composition:** Specify framing and viewpoint (close-up, wide, top-down), perspective/angle (eye-level, low-angle), and lighting/mood (soft diffuse, golden hour, high-contrast) to control the shot. If layout matters, call out placement (e.g., “logo top-right,” “subject centered with negative space on left”). For wide, cinematic, low-light, rain, or neon scenes, add extra detail about scale, atmosphere, and color so the model does not trade mood for surface realism.
- **People, pose, and action:** For people in scenes, describe scale, body framing, gaze, and object interactions. Examples: “full body visible, feet included,” “child-sized relative to the table,” “looking down at the open book, not at the camera,” or “hands naturally gripping the handlebars.” These details help with body proportion, action geometry, and gaze alignment.
- **Constraints (what to change vs preserve):** State exclusions and invariants explicitly (e.g., “no watermark,” “no extra text,” “no logos/trademarks,” “preserve identity/geometry/layout/brand elements”). For edits, use “change only X” + “keep everything else the same,” and repeat the preserve list on each iteration to reduce drift. If the edit should be surgical, also say not to alter saturation, contrast, layout, arrows, labels, camera angle, or surrounding objects.
- **Transparent backgrounds:** For `gpt-image-2`, transparency is available in preview. Pair `background="transparent"` with `output_format="png"` (the default) or `output_format="webp"`; `jpeg` does not support transparency. Describe the subject as isolated on a fully transparent background and explicitly exclude scenery, solid backdrops, checkerboards, and unwanted shadows. For edits, repeat “preserve the transparent background” so the workflow does not introduce or preserve an opaque scene. Omit `output_compression` for PNG; WebP supports optional compression.
- **Text in images:** Put literal text in **quotes** or **ALL CAPS** and specify typography details (font style, size, color, placement) as constraints. For tricky words (brand names, uncommon spellings), spell them out letter-by-letter to improve character accuracy. Use `medium` or `high` quality for small text, dense information panels, and multi-font layouts.
- **Multi-image inputs:** Reference each input by **index and description** (“Image 1: product photo… Image 2: style reference…”) and describe how they interact (“apply Image 2’s style to Image 1”). When compositing, be explicit about which elements move where (“put the bird from Image 1 on the elephant in Image 2”).
- **Iterate instead of overloading:** Long prompts can work well, but debugging is easier when you start with a clean base prompt and refine with small, single-change follow-ups (“make lighting warmer,” “remove the extra tree,” “restore the original background”). Use references like “same style as before” or “the subject” to leverage context, but re-specify critical details if they start to drift.

## 中文翻译

以下原则来自生成、编辑、信息图、广告、人物、UI 和合成等生产场景的反复验证。

1. **结构与目标**：按“背景/场景 → 主体 → 关键细节 → 约束”的顺序组织内容，并说明用途，例如广告、UI 模型或信息图。复杂请求使用短标题或换行，便于扫描和维护。
2. **提示词形式**：最小提示词、描述性段落、类 JSON 结构、指令式文本和标签式文本都可以使用。生产系统应优先选择清晰、可维护的模板，而不是追求特殊语法。
3. **具体描述与质量线索**：明确材质、形状、纹理和媒介。照片级任务直接写 `photorealistic`；“real photograph”“professional photography”等表达也可帮助模型进入相应视觉方向，但不要把精确相机参数当作物理模拟保证。
4. **延迟与保真度**：高并发或对延迟敏感时从 `quality="low"` 开始；小文字、密集信息图、特写肖像、身份敏感编辑和高分辨率输出应比较 `medium` 或 `high`。
5. **构图**：写明景别、视角、透视、角度、光线和情绪；布局重要时指出主体、Logo 或留白的位置。宽幅、电影感、低光、雨景和霓虹场景还需要补充尺度、空气感和色彩关系。
6. **人物、姿势与动作**：描述人物在画面中的比例、身体取景、视线和与物体的互动，例如“全身可见并包含脚部”或“看向打开的书而不是镜头”。
7. **约束与保持项**：明确什么要排除、什么必须保持。编辑任务使用“只改变 X”“保持其他内容不变”，并在每轮迭代中重复身份、几何、布局、标签和相机角度等不变量。
8. **透明背景**：对于 `gpt-image-2`，可以生成具有透明背景的图像。需要将 `background="transparent"` 与 `output_format="png"`（默认）或 `output_format="webp"` 配对；`jpeg` 不支持透明度。将主题描述为隔离在完全透明的背景上，并明确排除风景、实心背景、棋盘格和不需要的阴影。对于编辑，请重复“保留透明背景”，以防工作流程引入或保留不透明的场景。
9. **图像文字**：将原文放进引号或使用大写，并指定字体特征、字号关系、颜色、位置和对比度。品牌名或生僻词可逐字拼写；小文字和密集版面应比较 `medium` 或 `high`。
10. **多图输入**：用编号和角色引用每张图，例如“Image 1: 产品图；Image 2: 风格参考”，再说明元素如何从一张图进入另一张图。
11. **逐步迭代**：先生成干净的基础版本，再用一次只改变一个变量的后续请求修正光线、文字、对象或背景。关键约束如果开始漂移，应在后续请求中重新写明。

