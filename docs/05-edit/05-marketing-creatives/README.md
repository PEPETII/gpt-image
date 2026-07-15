# 5.5 Marketing Creatives with Real Text In-Image

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 5.5 Marketing Creatives with Real Text In-Image

Marketing creatives with real in-image text are great for rapid ad concepting, but typography needs explicit constraints. Put the exact copy in quotes, demand verbatim rendering (no extra characters), and describe placement and font style. If text fidelity is imperfect, keep the prompt strict and iterate—small wording/layout tweaks usually improve legibility.

```
prompt = """
Create a realistic billboard mockup of the shampoo on a highway scene during sunset.
Billboard text (EXACT, verbatim, no extra characters):
"Fresh and clean"
Typography: bold sans-serif, high contrast, centered, clean kerning.
Ensure text appears once and is perfectly legible.
No watermarks, no logos.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/shampoo.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "billboard_gpt-image-2.png")
```

Input Image:

![](../../assets/official-cookbook/shampoo.png)

Output Image:

![](../../assets/official-cookbook/billboard_gpt-image-2.png)

## 中文整理

创建一张真实的洗发水广告牌模型：产品位于日落时分的高速公路场景中。广告牌文字必须逐字为“Fresh and clean”，只出现一次；使用高对比、居中的粗体无衬线字体和干净字距，确保清晰可读。不要水印或 Logo。

## 本地图片

- ![billboard_gpt-image-2](../../assets/official-cookbook/billboard_gpt-image-2.png)
- ![shampoo](../../assets/official-cookbook/shampoo.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `billboard_gpt-image-2.png` | output |
| `shampoo.png` | input: product |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
