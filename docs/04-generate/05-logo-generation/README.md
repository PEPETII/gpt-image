# 4.5 Logo Generation

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.5 Logo Generation

Strong logo generation comes from clear brand constraints and simplicity. Describe the brand’s personality and use case, then ask for a clean, original mark with strong shape, balanced negative space, and scalability across sizes.

You can specify parameter “n” to denote the number of variations you would like to generate.

```
prompt = """
Create an original, non-infringing logo for a company called Field & Flour, a local bakery.
The logo should feel warm, simple, and timeless. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential.
Plain background. Deliver a single centered logo with generous padding. No watermark.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
    n=4     # Generate 4 versions of the logo
)

# Save all 4 images to separate files
for i, item in enumerate(result.data, start=1):
    image_base64 = item.b64_json
    image_bytes = base64.b64decode(image_base64)
    with open(f"output_images/logo_generation_{i}_gpt-image-2.png", "wb") as f:
        f.write(image_bytes)
```

Output Images:

| Option 1 | Option 2 | Option 3 | Option 4 |
| --- | --- | --- | --- |
|  |  |  |  |

## 中文整理

为名为 Field & Flour 的本地面包店创建原创且不侵权的 Logo。Logo 应温暖、简洁、历久弥新，使用干净的矢量感形状、清晰轮廓和平衡的负空间；细节要足够少，使其在大小尺寸下都清晰可读。使用扁平设计和极少描边，置于纯色背景中央并留出充足边距，不要水印。

## 本地图片

- ![logo_generation_1_gpt-image-2](../../assets/official-cookbook/logo_generation_1_gpt-image-2.png)
- ![logo_generation_2_gpt-image-2](../../assets/official-cookbook/logo_generation_2_gpt-image-2.png)
- ![logo_generation_3_gpt-image-2](../../assets/official-cookbook/logo_generation_3_gpt-image-2.png)
- ![logo_generation_4_gpt-image-2](../../assets/official-cookbook/logo_generation_4_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `logo_generation_1_gpt-image-2.png` | output |
| `logo_generation_2_gpt-image-2.png` | output |
| `logo_generation_3_gpt-image-2.png` | output |
| `logo_generation_4_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
