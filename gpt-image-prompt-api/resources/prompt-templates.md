# 内置 API 场景提示词方法库

本文件是 `gpt-image-prompt-api` 的本地场景参考。所有英文 prompt 都可直接放入 `images.generate` 或 `images.edit` 的 `prompt` 字段；参数和 Python 代码另由 `resources/api-reference.md` 选择。使用时替换方括号变量，不要把变量名、标题或方法说明放进请求。

## 通用 prompt 骨架

```text
Create [the final image and its purpose].

Subject:
[Subject, quantity, identity, action, material, and important details]

Composition:
[Viewpoint, framing, scale, placement, hierarchy, and negative space]

Visual direction:
[Medium, style, color, lighting, texture, realism, and mood]

Text:
[Exact text in quotation marks, language, placement, count, and legibility]

Constraints:
[What must change, what must remain unchanged, and what must not be added]
```

### 选择操作

- 无输入图：使用 `client.images.generate`。
- 一张或多张输入图：使用 `client.images.edit`。
- 编辑 prompt 必须写清唯一变化、保持项和禁止额外变化。
- 多图 prompt 必须给每张图编号和角色，编号与 Python 输入列表一致。
- 精确文字使用 `EXACT, verbatim`，明确出现次数和可读性；不要添加隐藏参数或请求字段到 prompt。

## 场景索引

| 场景 | 操作 | 主要方法 |
|---|---|---|
| 4.1 信息图 | generate | 按流程、组件和箭头组织信息 |
| 4.2 图片内文字翻译 | edit | 只替换文字，锁定全部视觉元素 |
| 4.3 照片级写实 | generate | 用真实材质、镜头和自然光建立可信度 |
| 4.4 世界知识 | generate | 锁定地点、日期和时代细节 |
| 4.5 Logo | generate | 原创、轮廓、负空间、小尺寸可读 |
| 4.6 广告 | generate | 受众、视觉钩子和唯一精确文案 |
| 4.7 故事漫画 | generate | 面板、动作和角色连续性 |
| 4.8 UI 模型 | generate | 内容层级、导航和真实可用状态 |
| 4.9 科学教育 | generate | 概念、箭头、准确标签和可读性 |
| 4.10 幻灯片图表 | generate | 页面目标、数据层级、图表和脚注 |
| 5.1 风格迁移 | edit | 只迁移视觉语言，生成原创主体 |
| 5.2 虚拟试穿 | edit | 锁定人物身份，只替换服装 |
| 5.3 草图转图像 | edit | 锁定布局、比例和透视 |
| 5.4 产品模型 | edit | 去背景并保持几何和标签 |
| 5.5 营销创意文字 | edit | 产品广告与唯一精确文案 |
| 5.6 光线天气 | edit | 只变更天气、时间或光照 |
| 5.7 对象移除 | edit | 删除对象并重建自然背景 |
| 5.8 人物入景 | edit | 保持人物身份并匹配场景空间 |
| 5.9 多图合成 | edit | 按角色合并基底图和输入图 |
| 6.1 室内替换 | edit | 只替换家具或室内对象 |
| 6.2 立体节日卡 | generate | 纸张层次、材质和短文案 |
| 6.3 收藏品包装 | generate | 物件、泡罩包装和零售展示 |
| 6.4 绘本角色连续性 | generate/edit | 角色锚点和连续场景 |

## 生成场景

### 4.1 信息图

调用重点：`generate`。按读者、学习目标、真实流程和组件关系组织 prompt；箭头有方向，标签短且可读。

```text
Create a detailed infographic explaining the function and flow of [SYSTEM] for [AUDIENCE].
Show the complete sequence from [START] through [STEP 1], [STEP 2], [STEP 3], to [END].
Include these components: [COMPONENTS]. Use clear directional arrows, numbered stages, short readable labels, and a visual hierarchy that makes the process understandable at a glance.
Use [STYLE], [BACKGROUND], and [COLOR SYSTEM]. Keep the diagram technically coherent, uncluttered, and easy to follow. Avoid tiny text, decorative elements, and unlabeled ambiguous arrows.
```

### 4.2 图片内文字翻译

调用重点：`edit`。输入图是唯一视觉基准，只替换可见文字，并保持文字数量、顺序和布局。

```text
Translate every visible text element in the input image into [TARGET LANGUAGE].
Preserve the exact image composition, layout, illustrations, icons, colors, shapes, spacing, hierarchy, and visual style.
Replace only the text. Keep the same meaning, number of labels, reading order, and approximate typography. Make the translated text natural, accurate, and fully legible.
Do not change anything else. Do not add, remove, duplicate, or invent text, logos, or watermarks.
```

### 4.3 照片级写实

调用重点：`generate`。用可观察的皮肤、材料、磨损、环境和镜头特征代替空泛风格词。

```text
Create a photorealistic candid photograph of [SUBJECT] in [SETTING].
Show [VISIBLE DETAILS: skin, fabric, surface wear, weather, and everyday objects] and [ACTION or RELATIONSHIP].
Shoot it as a [FORMAT] photograph, [SHOT SIZE] at [VIEWPOINT], with a [LENS] lens. Use [LIGHTING], [DEPTH OF FIELD], [COLOR BALANCE], and subtle [GRAIN or CAMERA CHARACTER].
The moment should feel honest and unposed, with natural proportions, believable materials, and ordinary environmental detail. Avoid glamorization, heavy retouching, artificial posing, and overly cinematic grading.
```

### 4.4 世界知识与时代场景

调用重点：`generate`。地点、日期或时代必须与服装、建筑、道具、交通和环境相互一致。

```text
Create a realistic [INDOOR or OUTDOOR] scene in [PLACE] on [DATE or HISTORICAL PERIOD].
Show [EVENT or ACTIVITY] with period-accurate clothing, architecture, objects, transport, signage, staging, and environmental details.
Use [REALISM and CAMERA DIRECTION]. Keep the scene historically coherent and grounded in the specified location and time. Do not introduce modern objects, anachronistic text, or unrelated landmarks.
```

### 4.5 Logo

调用重点：`generate`。强调原创、强轮廓、负空间和小尺寸识别度，不模仿现有品牌。

```text
Create an original logo for [BRAND], a [BUSINESS TYPE].
The identity should feel [BRAND QUALITIES]. Use clean vector-like shapes, a strong silhouette, balanced negative space, and a restrained [COLOR SYSTEM]. Favor simplicity over detail so it remains clear at both small and large sizes.
Use flat design with minimal strokes and no gradients unless essential. Place one centered logo on a plain [BACKGROUND] with generous padding. Include no extra text, trademark-like symbols, watermark, or unrelated logo.
```

### 4.6 广告

调用重点：`generate`。写明品牌、受众、场景、视觉钩子和唯一文案；不要让模型补充其他文字。

```text
Create a polished [AD FORMAT] for [BRAND], a [BRAND DESCRIPTION], aimed at [AUDIENCE].
Show [PEOPLE or PRODUCT] in [SCENE] with [VISUAL HOOK]. Make it [AD QUALITIES] using [COMPOSITION], [COLOR DIRECTION], natural poses, and [PHOTOGRAPHIC or ILLUSTRATIVE CUES].
Render the tagline "[EXACT TAGLINE]" exactly once, EXACT, verbatim, clearly and legibly, integrated into the layout.
No extra text, watermarks, fake logos, or unrelated brand marks.
```

### 4.7 故事转漫画

调用重点：`generate`。固定面板比例、阅读顺序、角色设计和逐格动作，避免每格重新设计角色。

```text
Create a [VERTICAL or HORIZONTAL] comic strip with [PANEL COUNT] equal-sized panels, read in [READING ORDER]. Keep the same character design, clothing, proportions, and visual style in every panel.

Panel 1: [SETUP, CHARACTER, ACTION, CAMERA, and EMOTION].
Panel 2: [TURNING POINT, ACTION, CAMERA, and EMOTION].
Panel 3: [DEVELOPMENT, ACTION, CAMERA, and EMOTION].
Panel 4: [ENDING, ACTION, CAMERA, and EMOTION].

Use [COMIC STYLE], clear panel boundaries, readable visual storytelling, and coherent lighting. Include only [TEXT or NO TEXT]. Do not add unrelated panels, duplicate characters, watermarks, or extra captions.
```

### 4.8 UI 模型

调用重点：`generate`。定义用户任务、内容模块、导航、信息状态和真实标签；画面应像可用产品而不是装饰海报。

```text
Create a realistic [MOBILE or WEB] app UI mockup for [PRODUCT], designed for [AUDIENCE] to [PRIMARY TASK].
Show [HEADER or NAVIGATION], [CORE CONTENT MODULES], [SECONDARY MODULES], and [CALL TO ACTION or STATUS]. Use realistic short labels and coherent information hierarchy.
Make it practical, accessible, and easy to scan. Use [BACKGROUND], [ACCENT COLORS], clear typography, consistent spacing, and minimal decoration. Place the interface in [DEVICE FRAME or PRESENTATION CONTEXT].
Show a complete, believable screen. Avoid placeholder gibberish, impossible controls, clutter, fake logos, and unrelated text.
```

### 4.9 科学与教育视觉

调用重点：`generate`。精确列出概念、顺序、关系和标签，避免微小文字以及未经用户提供的科学断言。

```text
Create a clear educational diagram titled "[EXACT TITLE]" for [AUDIENCE].
Explain [CONCEPT] by showing [STAGES or COMPONENTS] in the correct order. Use arrows to connect the relationships and label these exact terms: [EXACT LABELS].
Make it look like a clean classroom handout or presentation slide with [BACKGROUND], simple explanatory icons, clear grouping, readable text, and an obvious visual hierarchy.
Avoid tiny text, decorative clutter, scientifically misleading connections, invented labels, and anything that makes the concept hard to understand.
```

### 4.10 幻灯片、图表与生产力图片

调用重点：`generate`。把数据、单位、日期、脚注和品牌占位符列成可核对清单。

```text
Create one presentation slide titled "[EXACT TITLE]" for [AUDIENCE and PURPOSE].
Use a [BACKGROUND] and [TYPOGRAPHY] with a crisp, readable layout. Include:
- [PRIMARY DIAGRAM or VISUAL]
- [EXACT DATA, VALUES, and UNITS]
- [CHART TYPE] showing [METRIC] from [START] to [END]
- Footnotes: "[EXACT FOOTNOTE 1]" and "[EXACT FOOTNOTE 2]"
- [LOGO PLACEHOLDER or BRAND AREA, if needed]

Make the data hierarchy, spacing, labels, and reading order immediately clear. Use a restrained professional visual language. Avoid clip art, stock photography, gradients, decorative shadows, invented data, extra text, and unreadable small labels.
```

## 编辑场景

### 5.1 风格迁移

调用重点：`edit`。Image 1 提供风格，目标主体和构图必须原创且不复制参考图的具体内容。

```text
Use Image 1 as the style reference. Generate [NEW SUBJECT] in [NEW SETTING] on [BACKGROUND].
Preserve the reference's [MEDIUM, BRUSHWORK, LINE QUALITY, COLOR LOGIC, TEXTURE, and LIGHTING CHARACTER], but create an original composition and subject.
Change only the subject and scene described above. Do not copy recognizable characters, logos, text, or unrelated objects from the reference.
```

### 5.2 虚拟试穿

调用重点：`edit`。Image 1 是人物基准，Image 2 及后续图片只提供衣物；代码输入顺序必须相同。

```text
Image 1: the person reference and base photograph.
Image 2: the clothing reference to apply.

Edit Image 1 to dress the person using the provided clothing reference. Change only the clothing. Preserve the person's face, facial features, skin tone, body shape, pose, expression, hairstyle, proportions, identity, background, camera angle, framing, and image quality exactly.
Fit the garments naturally to the existing pose and body geometry with realistic fabric behavior, seams, folds, occlusion, and shadows. Match the original lighting and color temperature so the outfit integrates photorealistically.
Do not add accessories, text, logos, watermarks, or any other changes.
```

### 5.3 草图转图像

调用重点：`edit`。输入图的布局、比例、透视、主体位置和空间关系不可改变。

```text
Turn Image 1, a drawing or sketch, into a [TARGET MEDIUM] image.
Preserve the exact layout, proportions, perspective, subject placement, silhouette, and spatial relationships of the sketch. Choose realistic [MATERIALS] and [LIGHTING] consistent with the sketch's intent.
Change only the rendering from drawing to [TARGET MEDIUM]. Do not add, remove, move, redesign, or label elements. Do not add text, logos, or watermarks.
```

### 5.4 产品模型

调用重点：`edit`。只去除背景并轻微润色；产品几何和标签不可重绘。

```text
Extract the product from Image 1 and place it centered on a plain white opaque background.
Change only the background and apply light polishing. Preserve the product's exact geometry, proportions, materials, colors, surface details, label artwork, and label legibility.
Create a crisp silhouette with no halos, fringing, clipping, or warped edges. Add only a subtle realistic contact shadow. Do not restyle, redesign, recolor, rotate unexpectedly, add text, add logos, or add a watermark.
```

### 5.5 带真实文字的营销创意

调用重点：`edit`。产品来自输入图，新增文字是唯一允许的文字，必须逐字且只出现一次。

```text
Create a realistic [AD FORMAT] featuring the product from Image 1 in [SCENE] during [TIME or LIGHTING].

Text (EXACT, verbatim, no extra characters):
"[EXACT COPY]"

Typography: [TYPE STYLE], [CONTRAST], [ALIGNMENT], and clean spacing. Ensure the text appears exactly once and is perfectly legible, integrated naturally into the layout.
Preserve the product's geometry, colors, label, and identity. Do not add any other text, logo, watermark, or unrelated object.
```

### 5.6 光线与天气变换

调用重点：`edit`。只改变天气、时间或环境光，保持主体、构图和背景结构。

```text
Change only the lighting and weather in Image 1 so it looks like [TARGET WEATHER and TIME].
Preserve the subject, identity, pose, objects, geometry, composition, camera angle, framing, background structure, and image quality.
Apply believable [SNOW, RAIN, FOG, SUNLIGHT, or OTHER EFFECT] with physically coherent shadows, reflections, color temperature, and visibility.
Do not add, remove, move, redesign, or relight unrelated elements beyond what the requested weather and time require.
```

### 5.7 对象移除

调用重点：`edit`。删除一个对象并根据周围纹理、透视、光线和景深重建背景。

```text
Remove only [OBJECT] from [LOCATION] in Image 1.
Reconstruct the exposed background naturally using the surrounding texture, geometry, perspective, lighting, shadows, and depth of field.
Preserve everything else exactly, including the subject, face, pose, clothing, composition, colors, camera angle, and image quality. Do not add replacement objects, text, logos, or watermarks.
```

### 5.8 将人物放入场景

调用重点：`edit`。人物身份来自 Image 1；新场景的空间、尺度、接触点、光线和颜色必须匹配。

```text
Image 1: the person reference. Place this exact person into [TARGET SCENE] performing [ACTION].
Preserve the person's identity, face, facial features, skin tone, hairstyle, body proportions, and recognizable likeness. Use [POSE, CLOTHING, and EXPRESSION] only if explicitly requested; otherwise keep the reference unchanged.
Match the person's scale, perspective, feet or contact points, lighting, shadows, color temperature, depth of field, and motion blur to the scene. Make it look like an authentic photograph, not a poster.
Change only what is necessary to create the requested scene. Do not alter the person's identity, add unrelated objects, add text, logos, or watermarks.
```

### 5.9 多图引用与合成

调用重点：`edit`。先列基底图，再列插入图；多图列表顺序必须和编号一致。

```text
Image 1: [BASE SCENE and its elements to preserve].
Image 2: [OBJECT or PERSON to insert].
[Image 3: OPTIONAL additional reference and its role.]

Place [OBJECT or PERSON] from Image 2 into [TARGET LOCATION] in Image 1. Use Image 1 as the base for composition, background, camera, and lighting.
Match scale, perspective, pose, occlusion, contact shadows, color temperature, and depth of field so the composite is natural.
Preserve all unrelated elements of Image 1 and the identity or geometry of the inserted subject. Do not change anything else. Do not add text, logos, or watermarks.
```

## 高级场景

### 6.1 室内设计替换

调用重点：`edit`。只替换一个室内对象，保持相机、房间光线、地面阴影和周围物体。

```text
In Image 1, replace ONLY [ORIGINAL OBJECT] with [NEW OBJECT] made of [MATERIAL and COLOR].
Preserve the camera angle, room lighting, floor shadows, surrounding objects, wall and floor geometry, composition, and image quality.
Make the new object fit the existing scale and perspective. Add only physically realistic contact shadows, reflections, and material texture required by the replacement.
Keep every other aspect unchanged. Do not add, remove, or redesign unrelated furniture, decor, text, or watermarks.
```

### 6.2 立体节日贺卡

调用重点：`generate`。强调弹出纸层、真实材质、印刷构图和唯一短文案。

```text
Create an original [HOLIDAY] pop-up greeting card illustration.

Scene:
[SCENE DESCRIPTION, including the layered paper structure, focal object, and background]

Mood:
[WARM, NOSTALGIC, GENTLE, JOYFUL, or OTHER MOOD]

Style:
Premium greeting-card photography, [SOFT LIGHTING], realistic paper layers and material texture, shallow depth of field, tasteful [DECORATIVE LIGHT], and high print-quality composition.

Constraints:
- Original artwork only
- No trademarks, logos, or watermarks
- Include ONLY this card text, EXACT, verbatim: "[SHORT COPY]"
```

### 6.3 收藏品与泡罩包装

调用重点：`generate`。分别描述收藏品、包装、材质、零售陈列和唯一包装文字。

```text
Create a collectible [FIGURE or OBJECT] of [CHARACTER DESCRIPTION] in blister packaging.

Concept:
[COLLECTIBLE CONCEPT, STORY, and TARGET AUDIENCE]

Object details:
[SILHOUETTE, POSE, ACCESSORIES, SURFACE WEAR, and SCALE]

Style:
Premium toy photography, realistic [PLASTIC, METAL, PAPER, or FABRIC] textures, studio lighting, shallow depth of field, sharp label printing, and high-end retail presentation.

Constraints:
- Original design only
- No trademarks, logos, or watermarks
- Include ONLY this packaging text, EXACT, verbatim: "[SHORT COPY]"
```

### 6.4 绘本艺术与角色一致性

调用重点：初次角色建立用 `generate`；有角色参考图的连续场景用 `edit`。重复角色锚点，禁止每次重设计。

角色建立：

```text
Create a children's book illustration introducing a main character.

Character:
[AGE, SILHOUETTE, CLOTHING, FACE, EYES, HAIR, PROPORTIONS, PERSONALITY, and SIGNATURE OBJECT]

Theme:
[WHAT THE CHARACTER PROTECTS, LEARNS, OR DOES]

Style:
[MEDIUM], soft outlines, [COLOR PALETTE], and a whimsical, friendly mood. Use picture-book proportions with an expressive face.

Constraints:
- Original character only
- No text
- No watermarks
- Use a simple [BACKGROUND] that clearly showcases the character
```

连续场景：

```text
Continue the children's book story using the same character established in Image 1.

Scene:
[NEW SCENE, ACTION, OTHER CHARACTERS, and EMOTIONAL BEAT]

Character consistency:
- Same [CLOTHING and SIGNATURE OBJECT]
- Same facial features, proportions, silhouette, and color palette
- Same gentle, [PERSONALITY] personality

Style:
The same [MEDIUM], line quality, lighting language, and visual tone as Image 1.

Constraints:
- Do not redesign the character
- No text
- No watermarks
```

## 迭代与调试

第一轮只锁定目标、主体、构图和操作类型。后续每轮只改变一个变量，并保留所有身份、几何、文字和背景保护项。若结果偏离，先检查输入顺序、角色编号、唯一变化和精确文字，再调整风格词。参数变化与 prompt 变化分开记录，便于定位问题。
