# GPT Image 2 Prompt Templates

> 官方提示词模板参考库，供 SKILL.md 工作流使用

---

## Generate Mode Templates

### G1. Infographic Template

```
Create a detailed Infographic of [TOPIC/PROCESS].
From [STEP_1], to [STEP_2], [STEP_3], etc.
I'd like to understand [ASPECT] technically and visually.
```

**Parameters:** quality="high", size="1536x1024"
**Key Tips:** List all components explicitly; use quality="high" for dense labels

---

### G2. Translation Template

```
Translate the text in the image to [TARGET_LANGUAGE].
Do not change any other aspect of the image.
```

**Parameters:** input_fidelity="high"
**Key Tips:** Specify target language clearly; add "do not change" constraint

---

### G3. Photorealistic Template

```
Create a photorealistic [PHOTOGRAPH_TYPE] of [SUBJECT].
[SUBJECT_DETAILS: age, appearance, clothing, expression, action].
[COMPANION_OBJECTS/PEOPLE].
Shot like a [FILM_TYPE] photograph, [SHOT_TYPE] at [ANGLE], using a [LENS] lens.
[LIGHTING_DESCRIPTION].
The image should feel [MOOD], with [TEXTURE_DETAILS]. No [AVOID].
```

**Parameters:** quality="high", size="1024x1536"
**Key Tips:** Use "photorealistic"; add material/texture details; specify camera params

---

### G4. World Knowledge Template

```
Create a realistic [SCENE_TYPE] in [LOCATION] on [DATE/EVENT].
Photorealistic, period-accurate [CLOTHING/STAGING/ENVIRONMENT].
```

**Parameters:** quality="high", size="1536x1024"
**Key Tips:** Be specific about time and place; request "period-accurate" details

---

### G5. Logo Template

```
Create an original, non-infringing logo for [COMPANY_NAME], a [BUSINESS_TYPE].
The logo should feel [ADJECTIVES]. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes.
Flat design, minimal strokes, no gradients unless essential.
Plain background. Deliver a single centered logo with generous padding. No watermark.
```

**Parameters:** n=4, size="1024x1024", background="opaque"
**Key Tips:** Emphasize "original, non-infringing"; use n=4 for multiple candidates

---

### G6. Ads Template

```
Give me a [STYLE] ad / [SHOT_TYPE] for a brand called [BRAND].
It's a [BRAND_DESCRIPTION]. The ad shows [SCENE] with the tagline "[TAGLINE]."
Make it feel like a polished campaign image for [AUDIENCE]: [ADJECTIVES].
Use [COMPOSITION_STYLE], [COLOR_DIRECTION], [POSE_STYLE], and [PHOTOGRAPHY_CUES].
Render the tagline exactly once, clearly and legibly, integrated into the ad layout.
No extra text, no watermarks, no unrelated logos.
```

**Parameters:** quality="high", size="1536x1024"
**Key Tips:** Write like a creative brief; tagline in quotes; specify audience and mood

---

### G7. Comic Strip Template

```
Create a [ORIENTATION] comic-style reel with [NUMBER] equal-sized panels.
Panel 1: [SCENE_DESCRIPTION_WITH_ACTION_AND_EMOTION].
Panel 2: [SCENE_DESCRIPTION_WITH_ACTION_AND_EMOTION].
Panel 3: [SCENE_DESCRIPTION_WITH_ACTION_AND_EMOTION].
Panel 4: [SCENE_DESCRIPTION_WITH_ACTION_AND_EMOTION].
```

**Parameters:** size="1024x1536" (vertical) or "1536x1024" (horizontal)
**Key Tips:** Specify panel count and size; action-oriented descriptions per panel

---

### G8. UI Mockup Template

```
Create a realistic mobile app UI mockup for [APP/Product].
Show [MAIN_CONTENT] with a simple header, a [LIST_SECTION], a [FEATURE_SECTION], and basic information for [INFO].
Design it to be practical, and easy to use. [BACKGROUND_COLOR], [ACCENT_COLORS], clear typography, and minimal decoration.
It should look like a real, well-designed, beautiful app for [AUDIENCE].
Place the UI mockup in [DEVICE_FRAME].
```

**Parameters:** quality="high", size="1024x1536"
**Key Tips:** Describe as if the product already exists; focus on layout, hierarchy, spacing

---

### G9. Scientific/Educational Template

```
Create a [SUBJECT] diagram titled "[TITLE]" for [AUDIENCE_LEVEL].
Show [MAIN_CONCEPT]. Include [COMPONENT_1], [COMPONENT_2], and [COMPONENT_3].
Use arrows to connect the steps, and label the main elements: [LABEL_1], [LABEL_2], [LABEL_3].
Make it look like a clean [FORMAT], with a white background, simple icons, clear labels, and easy-to-read text.
Avoid tiny text, extra decoration, or anything that makes the diagram hard to understand.
```

**Parameters:** quality="high", size="1536x1024"
**Key Tips:** Specify audience and objectives; list required and excluded elements

---

### G10. Slides/Charts Template

```
Create one [DELIVERABLE_TYPE] titled "[TITLE]" that feels like a real [CONTEXT].
Use a clean white background, modern sans-serif typography like [FONT], and a crisp, minimal layout.
The slide should include:
* [ELEMENT_1]: [DETAILS]
* [ELEMENT_2]: [DETAILS with specific numbers]
* [ELEMENT_3]: [DETAILS]
* Small footnotes: "[FOOTNOTE_1]" and "[FOOTNOTE_2]"
The design should look [QUALITY_DESCRIPTION]: highly readable text, clear data hierarchy, polished spacing.
Avoid [UNWANTED_ELEMENTS].
```

**Parameters:** quality="high", size="1536x1024"
**Key Tips:** Write like a product spec; include exact numbers; use landscape for slides

---

## Edit Mode Templates

### E1. Style Transfer Template

```
Use the same style from the input image and generate [NEW_CONTENT] on a [BACKGROUND].
```

**Parameters:** size="1024x1536"
**Key Tips:** Describe what stays (style) vs. what changes (content); add hard constraints

---

### E2. Virtual Try-On Template

```
Edit the image to dress the [PERSON] using the provided clothing images.
Do not change [IDENTITY_FEATURES: face, facial features, skin tone, body shape, pose, or identity] in any way.
Preserve [PERSON_ATTRIBUTES: exact likeness, expression, hairstyle, and proportions].
Replace only the clothing, fitting the garments naturally to [BODY_DESCRIPTION] with realistic fabric behavior.
Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on.
Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks.
```

**Parameters:** input_fidelity="high", size="1024x1536"
**Key Tips:** Lock ALL identity features; supports multi-image input for clothing items

---

### E3. Drawing to Image Template

```
Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text.
```

**Parameters:** input_fidelity="high", quality="high", size="1536x1024"
**Key Tips:** Keep it simple; "do not add new elements" prevents creative reinterpretation

---

### E4. Product Mockup Template

```
Extract the product from the input image and place it on a plain white opaque background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing and a subtle realistic contact shadow.
Do not restyle the product; only remove background and lightly polish.
```

**Parameters:** background="opaque", input_fidelity="high", size="1024x1024"
**Key Tips:** Use background="opaque"; request "crisp silhouette, no halos"

---

### E5. Marketing Creatives Template

```
Create a realistic [AD_TYPE] of the [PRODUCT] on a [SCENE] during [TIME/SETTING].
[AD_TEXT_LABEL] (EXACT, verbatim, no extra characters):
"[EXACT_TEXT]"
Typography: [FONT_STYLE].
Ensure text appears once and is perfectly legible.
No watermarks, no logos.
```

**Parameters:** quality="high", size="1536x1024"
**Key Tips:** "EXACT, verbatim" for text; specify font; iterate if text isn't perfect

---

### E6. Lighting/Weather Template

```
Make it look like a [WEATHER/TIME_CONDITION] with [EFFECT].
```

**Parameters:** input_fidelity="high", size="1536x1024"
**Key Tips:** Only change environmental conditions; keep identity and geometry unchanged

---

### E7. Object Removal Template

```
Remove the [OBJECT] from [LOCATION]. Do not change anything else.
```

**Parameters:** input_fidelity="high", size="1024x1536"
**Key Tips:** Simple and direct; "do not change anything else" is the key constraint

---

### E8. Person Insert Template

```
Generate a highly realistic [SCENE] where this person is [ACTION].
The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
[PERSON_DESCRIPTION: clothing, appearance, expression, action].
The [ENVIRONMENT_DESCRIPTION].
The time of day is [TIME], with natural lighting and realistic colors.
Everything should feel grounded, authentic, and unstyled, as if captured in a real moment.
Avoid cinematic lighting, dramatic color grading, or stylized composition.
```

**Parameters:** input_fidelity="high", quality="high", size="1536x1024"
**Key Tips:** Anchor realism with "grounded photography"; explicitly avoid cinematic style

---

### E9. Multi-Image Compositing Template

```
Place the [OBJECT] from the [SOURCE_IMAGE] into the setting of [TARGET_IMAGE], [POSITION].
Use the same style of lighting, composition and background.
Do not change anything else.
```

**Parameters:** input_fidelity="high", size="1024x1536"
**Key Tips:** Explicitly reference which image provides which element; match lighting/shadows
