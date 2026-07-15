# 5.2 Virtual Clothing Try-On Prompt

Source: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

## Official prompt 1

```text
Edit the image to dress the woman using the provided clothing images. Do not change her face, facial features, skin tone, body shape, pose, or identity in any way. Preserve her exact likeness, expression, hairstyle, and proportions. Replace only the clothing, fitting the garments naturally to her existing pose and body geometry with realistic fabric behavior. Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on. Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks.
```

## 中文翻译

使用提供的服装图片为女性换装。不要改变她的脸、五官、肤色、体型、姿势或身份；保持她的相貌、表情、发型和比例完全一致。只替换服装，使其自然贴合现有姿势和身体几何，呈现真实的面料行为；匹配原图的光线、阴影和色温，让服装照片级融合而不是像贴上去的。不要改变背景、相机角度、构图或图像质量，也不要添加配饰、文字、Logo 或水印。

## 可替换变量

可替换人物图、服装图和衣物目标；人物身份、体型、姿势和背景属于保持项。
