# 5.4 Product Mockups

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 5.4 Product Mockups (transparent background + label integrity)

Product extraction and mockup prep is commonly used for catalogs, marketplaces, and design systems. Success depends on edge quality (clean silhouette, no fringing/halos) and label integrity (text stays sharp and unchanged). Transparent backgrounds are available in preview for `gpt-image-2`; request `background="transparent"` with `output_format="png"` (the default) or `output_format="webp"` to create a reusable product cutout directly. `jpeg` does not support transparent backgrounds. Ask for an isolated subject, preserve the existing product geometry and label, and omit solid backdrops, checkerboards, and unnecessary shadows. Omit `output_compression` for PNG output; WebP supports optional compression.

```
prompt = """
Extract the product from the input image and isolate it on a fully transparent background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing. Do not add a solid backdrop, checkerboard, scenery, or shadow.
Do not restyle the product; remove the background and preserve clean alpha transparency.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/shampoo.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
    background="transparent",
    output_format="png",
)

save_image(result, "extract_product_gpt-image-2.png")
```

Input Image:

![](../../assets/official-cookbook/shampoo.png)

Output Image:

![](../../assets/official-cookbook/extract_product_gpt-image-2.png)

## 中文整理

从输入图片中提取产品，并将其隔离在完全透明的背景上。输出应是居中的产品、干净的轮廓且没有光晕或边缘残留；精确保留产品几何形状和标签可读性。只需添加淡淡的抛光。不要添加坚实的背景、棋盘格、风景或阴影，请勿重新设计产品样式；移除背景并保持清晰的 alpha 透明度。

## 本地图片

- ![extract_product_gpt-image-2](../../assets/official-cookbook/extract_product_gpt-image-2.png)
- ![shampoo](../../assets/official-cookbook/shampoo.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `extract_product_gpt-image-2.png` | output |
| `shampoo.png` | input: product |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
