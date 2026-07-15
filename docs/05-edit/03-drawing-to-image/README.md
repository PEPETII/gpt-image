# 5.3 Drawing → Image (Rendering)

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 5.3 Drawing → Image (Rendering)

Sketch-to-render workflows are great for turning rough drawings into photorealistic concepts while keeping the original intent. Treat the prompt like a spec: preserve layout and perspective, then *add realism* by specifying plausible materials, lighting, and environment. Include “do not add new elements/text” to avoid creative reinterpretations.

```
prompt = """
Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/drawings.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "realistic_valley_gpt-image-2.png")
```

Input Image:

![](../../assets/official-cookbook/drawings.png)

Output Image:

![](../../assets/official-cookbook/realistic_valley_gpt-image-2.png)

## 中文整理

将这幅图画转换成照片级写实图像。保持准确的布局、比例和透视；根据草图意图选择真实材质和光线；不要添加新的元素或文字。

## 本地图片

- ![drawings](../../assets/official-cookbook/drawings.png)
- ![realistic_valley_gpt-image-2](../../assets/official-cookbook/realistic_valley_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `drawings.png` | input |
| `realistic_valley_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
