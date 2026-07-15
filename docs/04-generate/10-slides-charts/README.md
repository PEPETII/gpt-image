# 4.10 Slides, Diagrams, Charts, and Productivity Images

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.10 Slides, Diagrams, Charts, and Productivity Images

Productivity visuals work best when the prompt is written like an artifact spec rather than an illustration request. Name the exact deliverable (slide, workflow diagram, chart, page image), define the canvas and hierarchy, provide the real text or data, and describe the visual language. These prompts should include practical constraints: readable typography, polished spacing, no decorative clutter, and no generic stock-photo treatment.

For slides, charts, and diagram-heavy assets, include the numbers and labels directly in the prompt. Use a landscape size for deck-style outputs and `quality="high"` when the image contains small text, legends, axes, or footnotes.

```
prompt = """
Create one pitch-deck slide titled **"Market Opportunity"** that feels like a real Series A fundraising slide from a YC-backed startup.

Use a clean white background, modern sans-serif typography like Inter, and a crisp, minimal layout. The slide should include:

* A TAM/SAM/SOM concentric-circle diagram in muted blues and grays
* Specific, believable market sizing numbers:

  * **TAM:** $42B
  * **SAM:** $8.7B
  * **SOM:** $340M
* A clean bar chart below showing market growth from **2021 to 2026**, with a subtle upward trend
* Small footnotes: **"AGI Research, 2024"** and **"Internal analysis"**
* A company logo placeholder in the bottom-right corner

The design should look like it belongs in a deck that actually raised money: highly readable text, clear data hierarchy, polished spacing, and professional startup-style visual language.

Avoid clip art, stock photography, gradients, shadows, decorative elements, or anything that feels generic or overdesigned.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1536x864",
    quality="high",
)

save_image(result, "market_opportunity_slide_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/market_opportunity_slide_gpt-image-2.png)

## 中文整理

创建一张标题为“Market Opportunity”的融资演示幻灯片，像真正的 YC 支持的初创公司 Series A 融资页。使用白色背景、现代无衬线字体和清晰极简布局；包含 TAM/SAM/SOM 同心圆图、TAM $42B、SAM $8.7B、SOM $340M 的市场规模数据、2021 至 2026 年的增长柱状图、脚注“AGI Research, 2024”和“Internal analysis”，以及右下角的公司 Logo 占位符。要求文字高度可读、数据层级清晰、间距专业；不要剪贴画、图库照片、渐变、阴影或装饰性元素。

## 本地图片

- ![market_opportunity_slide_gpt-image-2](../../assets/official-cookbook/market_opportunity_slide_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `market_opportunity_slide_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
