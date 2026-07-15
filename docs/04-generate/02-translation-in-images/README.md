# 4.2 Translation in Images

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.2 Translation in Images

Used for localizing existing designs (ads, UI screenshots, packaging, infographics) into another language without rebuilding the layout from scratch. The key is to preserve everything except the text—keep typography style, placement, spacing, and hierarchy consistent—while translating verbatim and accurately, with no extra words, no reflow unless necessary, and no unintended edits to logos, icons, or imagery.

```
prompt = """
Translate the text in the infographic to Spanish. Do not change any other aspect of the image.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/infographic_coffee_machine_gpt-image-2.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "infographic_coffee_machine_sp_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/infographic_coffee_machine_sp_gpt-image-2.png)

## 中文整理

将信息图中的文字翻译成西班牙语。不要改变图片的任何其他部分。

## 本地图片

- ![infographic_coffee_machine_gpt-image-2](../../assets/official-cookbook/infographic_coffee_machine_gpt-image-2.png)
- ![infographic_coffee_machine_sp_gpt-image-2](../../assets/official-cookbook/infographic_coffee_machine_sp_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `infographic_coffee_machine_gpt-image-2.png` | input |
| `infographic_coffee_machine_sp_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
