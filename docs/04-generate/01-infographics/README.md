# 4.1 Infographics

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.1 Infographics

Use infographics to explain structured information for a specific audience: students, executives, customers, or the general public. Examples include explainers, posters, labeled diagrams, timelines, and “visual wiki” assets. For dense layouts or heavy in-image text, it’s recommended to set output generation quality to “high”.

```
prompt = """
Create a detailed Infographic of the functioning and flow of an automatic coffee machine like a Jura.
From bean basket, to grinding, to scale, water tank, boiler, etc.
I'd like to understand technically and visually the flow.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "infographic_coffee_machine_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/infographic_coffee_machine_gpt-image-2.png)

## 中文整理

创建一张详细的信息图，解释类似 Jura 的全自动咖啡机的工作功能和流程。从豆仓、研磨、秤、水箱到锅炉等部件都要展示出来，让读者从技术和视觉上理解整个流程。

## 本地图片

- ![infographic_coffee_machine_gpt-image-2](../../assets/official-cookbook/infographic_coffee_machine_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `infographic_coffee_machine_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
