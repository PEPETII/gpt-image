# 5.6 Lighting and Weather Transformation

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 5.6 Lighting and Weather Transformation

Used to re-stage a photo for different moods, seasons, or time-of-day variants (e.g., sunny → overcast, daytime → dusk, clear → snowy) while keeping the scene composition intact. The key is to change only environmental conditions—lighting direction/quality, shadows, atmosphere, precipitation, and ground wetness—while preserving identity, geometry, camera angle, and object placement so it still reads as the same original photo.

```
prompt = """
Make it look like a winter evening with snowfall.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/billboard_gpt-image-2.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "billboard_winter_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/billboard_winter_gpt-image-2.png)

## 中文整理

让画面看起来像一个有降雪的冬季夜晚。

## 本地图片

- ![billboard_gpt-image-2](../../assets/official-cookbook/billboard_gpt-image-2.png)
- ![billboard_winter_gpt-image-2](../../assets/official-cookbook/billboard_winter_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `billboard_gpt-image-2.png` | input |
| `billboard_winter_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
