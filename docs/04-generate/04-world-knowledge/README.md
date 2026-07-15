# 4.4 World knowledge

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.4 World knowledge

GPT image generation models can pair strong reasoning with world knowledge. For example, when asked to generate a scene set in Bethel, New York in August 1969, they can infer Woodstock and produce an accurate, context-appropriate image without being explicitly told about the event.

```
prompt = """
Create a realistic outdoor crowd scene in Bethel, New York on August 16, 1969.
Photorealistic, period-accurate clothing, staging, and environment.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "world_knowledge-gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/world_knowledge-gpt-image-2.png)

## 中文整理

创建一幅写实的户外人群场景：地点是纽约州贝瑟尔，时间是 1969 年 8 月 16 日。服装、现场安排和环境都要符合时代，整体采用照片级写实风格。

## 本地图片

- ![world_knowledge-gpt-image-2](../../assets/official-cookbook/world_knowledge-gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `world_knowledge-gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
