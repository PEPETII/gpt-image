# 内置网页版提示词方法库

本文件是 `gpt-image-prompt-web` 的完整本地参考。每个场景都提供适用范围、方法重点和可直接改写的英文模板。使用时只读取相关小节，把方括号变量替换为用户需求；不要把变量名、方法说明或本文件标题复制进最终提示词。

## 通用骨架

```text
Create [the final image and its purpose].

Subject:
[Who or what must appear, quantity, identity, action, material, and important details]

Composition:
[Aspect, viewpoint, framing, scale, placement, visual hierarchy, and negative space]

Visual direction:
[Medium, style, color palette, lighting, texture, realism, and mood]

Text:
[If needed: exact text in quotation marks, language, placement, count, and legibility]

Constraints:
[What must be preserved, what must change, and what must not be added]
```

### 精确文字

把必须出现的文字原样放入引号，并写明 `EXACT, verbatim`。说明语言、大小写、标点、出现次数、位置、对比度和可读性。不要要求大量小字；将信息拆成清晰层级。对 Logo、广告、包装、UI、信息图和幻灯片，明确禁止额外文字、假 Logo、水印和无关标识。

### 编辑保护

```text
Change:
Only [the requested object, attribute, or text].

Preserve:
[Identity, face, body, pose, product geometry, label, composition, camera, lighting, and background]

Do not change:
Anything outside the requested edit. Do not add text, logos, accessories, or watermarks.
```

### 多图引用

```text
Image 1: [base scene or person reference].
Image 2: [object, clothing, style, or secondary reference].
Use Image 1 as [the structure or destination] and Image 2 as [the inserted source].
Match scale, perspective, lighting, shadows, color temperature, and depth of field.
```

## 生成场景

### 4.1 信息图

适合流程、系统、时间线、组件关系和带标签的技术图。先给读者和学习目标，再按真实顺序列组件，用方向明确的箭头连接；标签短、层级清楚、足够大。

```text
Create a detailed infographic explaining the function and flow of [SYSTEM] for [AUDIENCE].
Show the complete sequence from [START] through [STEP 1], [STEP 2], [STEP 3], to [END].
Include these components: [COMPONENTS]. Use clear directional arrows, numbered stages, short readable labels, and a visual hierarchy that makes the process understandable at a glance.
Use [STYLE], [BACKGROUND], and [COLOR SYSTEM]. Keep the diagram technically coherent, uncluttered, and easy to follow. Avoid tiny text, decorative elements, and unlabeled ambiguous arrows.
```

### 4.2 图片内文字翻译

适合已有信息图、海报或界面只改变可见文字的任务。把输入图作为整体基准，锁定布局、图标、颜色、插图、尺寸、字体风格和顺序。

```text
Translate every visible text element in the input image into [TARGET LANGUAGE].
Preserve the exact image composition, layout, illustrations, icons, colors, shapes, spacing, hierarchy, and visual style.
Replace only the text. Keep the same meaning, number of labels, reading order, and approximate typography. Make the translated text natural, accurate, and fully legible.
Do not change anything else. Do not add, remove, duplicate, or invent text, logos, or watermarks.
```

### 4.3 照片级写实

适合自然抓拍、人物、产品或环境照片。用具体可见的皮肤、材质、磨损、光线和镜头信息建立真实感；避免只写“电影感”或过度美化。

```text
Create a photorealistic candid photograph of [SUBJECT] in [SETTING].
Show [VISIBLE DETAILS: skin, fabric, surface wear, weather, and everyday objects] and [ACTION or RELATIONSHIP].
Shoot it as a [FORMAT] photograph, [SHOT SIZE] at [VIEWPOINT], with a [LENS] lens. Use [LIGHTING], [DEPTH OF FIELD], [COLOR BALANCE], and subtle [GRAIN or CAMERA CHARACTER].
The moment should feel honest and unposed, with natural proportions, believable materials, and ordinary environmental detail. Avoid glamorization, heavy retouching, artificial posing, and overly cinematic grading.
```

### 4.4 世界知识与时代场景

适合地点、日期、历史事件和时代环境。明确地点、日期或时代，并逐项约束服装、建筑、道具、交通、标识和社会环境的时代一致性；不确定的事实不要擅自补写。

```text
Create a realistic [INDOOR or OUTDOOR] scene in [PLACE] on [DATE or HISTORICAL PERIOD].
Show [EVENT or ACTIVITY] with period-accurate clothing, architecture, objects, transport, signage, staging, and environmental details.
Use [REALISM and CAMERA DIRECTION]. Keep the scene historically coherent and grounded in the specified location and time. Do not introduce modern objects, anachronistic text, or unrelated landmarks.
```

### 4.5 Logo

适合原创品牌标志和概念探索。先定义品牌和应用尺寸，再强调轮廓、负空间、少量颜色和小尺寸可读性；不要要求模仿现有品牌。

```text
Create an original logo for [BRAND], a [BUSINESS TYPE].
The identity should feel [BRAND QUALITIES]. Use clean vector-like shapes, a strong silhouette, balanced negative space, and a restrained [COLOR SYSTEM]. Favor simplicity over detail so it remains clear at both small and large sizes.
Use flat design with minimal strokes and no gradients unless essential. Place one centered logo on a plain [BACKGROUND] with generous padding. Include no extra text, trademark-like symbols, watermark, or unrelated logo.
```

### 4.6 广告

适合品牌广告、时尚 campaign、户外广告和社交媒体创意。写清品牌、受众、视觉钩子、版式和唯一文案；要求文案逐字出现且不增加其他文本。

```text
Create a polished [AD FORMAT] for [BRAND], a [BRAND DESCRIPTION], aimed at [AUDIENCE].
Show [PEOPLE or PRODUCT] in [SCENE] with [VISUAL HOOK]. Make it [AD QUALITIES: contemporary, energetic, premium, restrained] using [COMPOSITION], [COLOR DIRECTION], natural poses, and [PHOTOGRAPHIC or ILLUSTRATIVE CUES].
Render the tagline "[EXACT TAGLINE]" exactly once, EXACT, verbatim, clearly and legibly, integrated into the layout.
No extra text, watermarks, fake logos, or unrelated brand marks.
```

### 4.7 故事转漫画

适合多面板故事、竖版漫画和连续动作。先固定面板数量、比例和阅读顺序，再逐格写角色状态、动作、镜头和情绪转折；重复角色锚点保持一致。

```text
Create a [VERTICAL or HORIZONTAL] comic strip with [PANEL COUNT] equal-sized panels, read in [READING ORDER]. Keep the same character design, clothing, proportions, and visual style in every panel.

Panel 1: [SETUP, CHARACTER, ACTION, CAMERA, and EMOTION].
Panel 2: [TURNING POINT, ACTION, CAMERA, and EMOTION].
Panel 3: [DEVELOPMENT, ACTION, CAMERA, and EMOTION].
Panel 4: [ENDING, ACTION, CAMERA, and EMOTION].

Use [COMIC STYLE], clear panel boundaries, readable visual storytelling, and coherent lighting. Include only [TEXT or NO TEXT]. Do not add unrelated panels, duplicate characters, watermarks, or extra captions.
```

### 4.8 UI 模型

适合移动端、网页端和产品界面概念图。定义目标用户和核心任务，列出真实内容模块、层级、导航和状态；视觉上让界面可用而不是装饰性海报。

```text
Create a realistic [MOBILE or WEB] app UI mockup for [PRODUCT], designed for [AUDIENCE] to [PRIMARY TASK].
Show [HEADER or NAVIGATION], [CORE CONTENT MODULES], [SECONDARY MODULES], and [CALL TO ACTION or STATUS]. Use realistic short labels and coherent information hierarchy.
Make it practical, accessible, and easy to scan. Use [BACKGROUND], [ACCENT COLORS], clear typography, consistent spacing, and minimal decoration. Place the interface in [DEVICE FRAME or PRESENTATION CONTEXT].
Show a complete, believable screen. Avoid placeholder gibberish, impossible controls, clutter, fake logos, and unrelated text.
```

### 4.9 科学与教育视觉

适合生物、物理、化学、医学和课堂讲义。先写学习对象，再列概念、流程和精确标签；用箭头表达关系，确保文字足够大并避免无依据的细节。

```text
Create a clear educational diagram titled "[EXACT TITLE]" for [AUDIENCE].
Explain [CONCEPT] by showing [STAGES or COMPONENTS] in the correct order. Use arrows to connect the relationships and label these exact terms: [EXACT LABELS].
Make it look like a clean classroom handout or presentation slide with [BACKGROUND], simple explanatory icons, clear grouping, readable text, and an obvious visual hierarchy.
Avoid tiny text, decorative clutter, scientifically misleading connections, invented labels, and anything that makes the concept hard to understand.
```

### 4.10 幻灯片、图表与生产力图片

适合 pitch deck、数据图表、流程页和工作汇报。先固定页面目标和数据，再指定版式、层级、数值、脚注和禁用装饰；所有数字和脚注逐字核对。

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

适合保留输入图的媒介、笔触、色彩逻辑或渲染方式，同时更换主体。把风格图和目标主体关系写清楚，避免复制原图具体人物或标志性内容。

```text
Use Image 1 as the style reference. Generate [NEW SUBJECT] in [NEW SETTING] on [BACKGROUND].
Preserve the reference's [MEDIUM, BRUSHWORK, LINE QUALITY, COLOR LOGIC, TEXTURE, and LIGHTING CHARACTER], but create an original composition and subject.
Change only the subject and scene described above. Do not copy recognizable characters, logos, text, or unrelated objects from the reference.
```

### 5.2 虚拟试穿

适合人物图加一张或多张服装图。人物图是身份与身体基准，服装图只提供衣物；换装时匹配褶皱、遮挡、光线和阴影，严格保持人物和背景。

```text
Image 1: the person reference and base photograph.
Image 2: the clothing reference to apply.

Edit Image 1 to dress the person using the provided clothing reference. Change only the clothing. Preserve the person's face, facial features, skin tone, body shape, pose, expression, hairstyle, proportions, identity, background, camera angle, framing, and image quality exactly.
Fit the garments naturally to the existing pose and body geometry with realistic fabric behavior, seams, folds, occlusion, and shadows. Match the original lighting and color temperature so the outfit integrates photorealistically.
Do not add accessories, text, logos, watermarks, or any other changes.
```

### 5.3 草图转图像

适合把草图渲染成照片、产品概念或环境图。草图的布局、比例、透视和主体关系是不可变基准，材质与光线可按用户指定补全。

```text
Turn Image 1, a drawing or sketch, into a [TARGET MEDIUM] image.
Preserve the exact layout, proportions, perspective, subject placement, silhouette, and spatial relationships of the sketch. Choose realistic [MATERIALS] and [LIGHTING] consistent with the sketch's intent.
Change only the rendering from drawing to [TARGET MEDIUM]. Do not add, remove, move, redesign, or label elements. Do not add text, logos, or watermarks.
```

### 5.4 产品模型

适合抠出产品、白底电商图和透明感不足的边缘修正。必须保持产品几何、颜色、材质、标签和文字；只允许轻微润色与接触阴影。

```text
Extract the product from Image 1 and isolate it on a fully transparent background.
Change only the background and apply light polishing. Do not add a solid backdrop, checkerboard, scenery, or shadow. Preserve the product's exact geometry, proportions, materials, colors, surface details, label artwork, and label legibility.
Create a crisp silhouette with no halos, fringing, clipping, or warped edges. Do not restyle, redesign, recolor, rotate unexpectedly, add text, add logos, or add a watermark; remove the background and preserve clean alpha transparency.
```

### 5.5 带真实文字的营销创意

适合把产品图放进广告牌、海报、包装或活动场景。精确文案是唯一允许新增的文字，必须写出现次数、版式和可读性。

```text
Create a realistic [AD FORMAT] featuring the product from Image 1 in [SCENE] during [TIME or LIGHTING].

Text (EXACT, verbatim, no extra characters):
"[EXACT COPY]"

Typography: [TYPE STYLE], [CONTRAST], [ALIGNMENT], and clean spacing. Ensure the text appears exactly once and is perfectly legible, integrated naturally into the layout.
Preserve the product's geometry, colors, label, and identity. Do not add any other text, logo, watermark, or unrelated object.
```

### 5.6 光线与天气变换

适合只改变季节、时间、天气或环境光。把变化写成单一变量，并锁定主体、构图、背景结构和相机特征。

```text
Change only the lighting and weather in Image 1 so it looks like [TARGET WEATHER and TIME].
Preserve the subject, identity, pose, objects, geometry, composition, camera angle, framing, background structure, and image quality.
Apply believable [SNOW, RAIN, FOG, SUNLIGHT, or OTHER EFFECT] with physically coherent shadows, reflections, color temperature, and visibility.
Do not add, remove, move, redesign, or relight unrelated elements beyond what the requested weather and time require.
```

### 5.7 移除对象

适合去除人物手中物体、背景杂物和局部元素。明确对象和位置，让背景按周围纹理、透视和阴影自然重建。

```text
Remove only [OBJECT] from [LOCATION] in Image 1.
Reconstruct the exposed background naturally using the surrounding texture, geometry, perspective, lighting, shadows, and depth of field.
Preserve everything else exactly, including the subject, face, pose, clothing, composition, colors, camera angle, and image quality. Do not add replacement objects, text, logos, or watermarks.
```

### 5.8 将人物放入场景

适合将人物参考图放入新环境。人物身份、脸部和比例必须来自输入图；场景的尺度、姿势、动作、接触关系和光线要自然融合。

```text
Image 1: the person reference. Place this exact person into [TARGET SCENE] performing [ACTION].
Preserve the person's identity, face, facial features, skin tone, hairstyle, body proportions, and recognizable likeness. Use [POSE, CLOTHING, and EXPRESSION] only if they are explicitly requested; otherwise keep the reference unchanged.
Match the person's scale, perspective, feet or contact points, lighting, shadows, color temperature, depth of field, and motion blur to the scene. Make it look like an authentic photograph, not a poster.
Change only what is necessary to create the requested scene. Do not alter the person's identity, add unrelated objects, add text, logos, or watermarks.
```

### 5.9 多图引用与合成

适合从不同输入图取主体、服装、产品、风格或背景。先定义基底图，再定义插入图；所有图编号必须与用户实际提供顺序一致。

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

适合家具、地毯、墙面和局部室内对象替换。对象替换是唯一变化；相机角度、房间光线、地面阴影和周围物品必须保持。

```text
In Image 1, replace ONLY [ORIGINAL OBJECT] with [NEW OBJECT] made of [MATERIAL and COLOR].
Preserve the camera angle, room lighting, floor shadows, surrounding objects, wall and floor geometry, composition, and image quality.
Make the new object fit the existing scale and perspective. Add only physically realistic contact shadows, reflections, and material texture required by the replacement.
Keep every other aspect unchanged. Do not add, remove, or redesign unrelated furniture, decor, text, or watermarks.
```

### 6.2 立体节日贺卡

适合纸张层次、立体弹出结构、节日场景和短文案。场景描述决定主体，材质和印刷质量决定成品感；只允许指定文案出现。

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

适合收藏手办、玩具、包装、零售展示和材质探索。分别描述人物/物件、包装结构、材质和标签；设计必须原创且文字唯一。

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

适合先建立主角，再连续生成多个故事场景。第一张图建立角色锚点；后续每次重复服装、面部特征、比例、色彩和性格，禁止重新设计。

角色建立模板：

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

连续场景模板：

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

## 迭代方法

第一轮先锁定主体、构图和任务目标。后续每轮只改变一个变量，例如天气、镜头、颜色、服装或文案位置；继续重复所有必须保持的内容。若结果偏离，优先增加具体的保持项和唯一变化，而不是继续添加抽象形容词。
