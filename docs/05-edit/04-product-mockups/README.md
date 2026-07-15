# 5.4 Product Mockups

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 5.4 Product Mockups (clean background + label integrity)

Product extraction and mockup prep is commonly used for catalogs, marketplaces, and design systems. Success depends on edge quality (clean silhouette, no fringing/halos) and label integrity (text stays sharp and unchanged). For `gpt-image-2`, keep the output background opaque and use a downstream background-removal step if you need a final transparent asset. If you want realism without re-styling, ask for only light polishing and optionally a subtle contact shadow on a plain background.

```
prompt = """
Extract the product from the input image and place it on a plain white opaque background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing and a subtle realistic contact shadow.
Do not restyle the product; only remove background and lightly polish.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/shampoo.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
    background="opaque",
)

save_image(result, "extract_product_gpt-image-2.png")
```

Input Image:

![](../../assets/official-cookbook/shampoo.png)

Output Image:

![](../../assets/official-cookbook/extract_product_gpt-image-2.png)

## 中文整理

从输入图片中提取产品并放到纯白不透明背景上。输出应是居中的产品、干净的轮廓且没有光晕或边缘残留；精确保留产品几何形状和标签可读性。只做轻微润色和自然接触阴影，不要重新设计、改变风格或扭曲产品。

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
