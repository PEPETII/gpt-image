# 4.8 UI Mockups

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.8 UI Mockups

UI mockups work best when you describe the product as if it already exists. Focus on layout, hierarchy, spacing, and real interface elements, and avoid concept art language so the result looks like a usable, shipped interface rather than a design sketch.

```
prompt = """
Create a realistic mobile app UI mockup for a local farmers market.
Show today’s market with a simple header, a short list of vendors with small photos and categories, a small “Today’s specials” section, and basic information for location and hours.
Design it to be practical, and easy to use. White background, subtle natural accent colors, clear typography, and minimal decoration.
It should look like a real, well-designed, beautiful app for a small local market.
Place the UI mockup in an iPhone frame.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "ui_farmers_market_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/ui_farmers_market_gpt-image-2.png)

## 中文整理

创建一个真实的本地农贸市场移动应用 UI 模型。展示今日市场、简洁的标题栏、带小照片和分类的供应商列表、Today’s specials 区域，以及地点和营业时间等基本信息。设计要实用、易用、漂亮；使用白色背景、低调自然的强调色、清晰排版和极少装饰，并把 UI 放在 iPhone 外框中。

## 本地图片

- ![ui_farmers_market_gpt-image-2](../../assets/official-cookbook/ui_farmers_market_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `ui_farmers_market_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
