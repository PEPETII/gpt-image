# 虚拟服装试穿 | Virtual Try-On

> 章节：5.2 | 分类：编辑 (Edit)

---

## 提示词 / Prompt

```text
Edit the image to dress the woman using the provided clothing images. Do not change her face, facial features, skin tone, body shape, pose, or identity in any way. Preserve her exact likeness, expression, hairstyle, and proportions. Replace only the clothing, fitting the garments naturally to her existing pose and body geometry with realistic fabric behavior. Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on. Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks.
```

### 中文翻译

```
使用提供的服装图片为图中女性换装。不要以任何方式改变她的面部、五官、肤色、体型、姿势或身份。保留她精确的相貌、表情、发型和比例。仅替换服装，使衣物自然贴合她现有的姿势和体型，具有逼真的面料垂坠效果。匹配原始照片的光线、阴影和色温，使服装照片级自然融合，看起来不像粘贴上去的。不要改变背景、相机角度、构图或图像质量，也不要添加配饰、文字、标志或水印。
```

---

## 关键技巧 / Key Tips

明确锁定人物所有不应改变的特征（面部、体型、姿势、发型、表情）；仅允许更改服装；要求逼真的穿着效果（垂坠感、褶皱）和一致的光照/阴影。可传入多张服装图片。

## API 参数建议 / Recommended Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| input_fidelity | high | 高保真度，确保人物特征不被改变 |
| size | 1024x1536 | 竖版构图，适合人物全身展示 |

## 适用场景 / Use Cases

电商虚拟试穿、服装预览、造型搭配
