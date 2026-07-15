# 4.9 Scientific / Educational Visuals

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.9 Scientific / Educational Visuals

Scientific and educational visuals are strong fits for biology, chemistry, classroom explainers, flat scientific icon systems, diagrams, and learning assets. Prompt them like an instructional design brief: define the audience, lesson objective, visual format, required labels, and scientific constraints. For best results, ask for a clean, flat visual system with consistent icon style, clear arrows, readable labels, and enough white space for students to scan the concept quickly.

When accuracy matters, list the required components explicitly and say what should not be included. Use `quality="high"` for dense labels, diagrams, or assets that will be used in slides or course materials.

```
prompt = """
Create a simple biology diagram titled "Cellular Respiration at a Glance" for high school students.

Show how glucose turns into energy inside a cell. Include glycolysis, the Krebs cycle, and the electron transport chain.
Use arrows to connect the steps, and label the main molecules: glucose, pyruvate, ATP, NADH, FADH2, CO2, O2, and H2O.
Make it look like a clean classroom handout or slide, with a white background, simple icons, clear labels, and easy-to-read text.

Avoid tiny text, extra decoration, or anything that makes the diagram hard to understand.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1536x1024",
    quality="high",
)

save_image(result, "scientific_educational_cellular_respiration_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/scientific_educational_cellular_respiration_gpt-image-2.png)

## 中文整理

为高中生创建一张标题为“Cellular Respiration at a Glance”的简洁生物学图表。展示细胞内葡萄糖如何转化为能量，包括糖酵解、克雷布斯循环和电子传递链；用箭头连接步骤，并标注 glucose、pyruvate、ATP、NADH、FADH2、CO2、O2 和 H2O。画面像干净的课堂讲义或幻灯片，白色背景、简单图标、清晰且易读的文字，不要小字、额外装饰或难以理解的内容。

## 本地图片

- ![scientific_educational_cellular_respiration_gpt-image-2](../../assets/official-cookbook/scientific_educational_cellular_respiration_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `scientific_educational_cellular_respiration_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
