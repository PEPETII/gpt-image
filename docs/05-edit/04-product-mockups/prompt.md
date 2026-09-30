# 5.4 Product Mockups Prompt

Source: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

## Official prompt 1

```text
Extract the product from the input image and isolate it on a fully transparent background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing. Do not add a solid backdrop, checkerboard, scenery, or shadow.
Do not restyle the product; remove the background and preserve clean alpha transparency.
```

## 中文翻译

从输入图片中提取产品，并将其隔离在完全透明的背景上。输出应是居中的产品、干净的轮廓且没有光晕或边缘残留；精确保留产品几何形状和标签可读性。只需添加淡淡的抛光。不要添加坚实的背景、棋盘格、风景或阴影，请勿重新设计产品样式；移除背景并保持清晰的 alpha 透明度。

## 可替换变量

可替换产品图和背景；几何形状、材质、颜色、标签和轮廓属于保持项。
