# 4.6 Ads Generation

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.6 Ads Generation

Ad generation works best when the prompt is written like a creative brief rather than a purely technical image spec. Describe the brand, audience, culture, concept, composition, and exact copy, then let the model make taste-driven creative decisions inside those boundaries. This is useful for early campaign exploration because the model can interpret audience cues, infer art direction, and propose visual details that make the ad feel considered rather than merely rendered.

For stronger results, include the brand positioning, desired vibe, target audience, scene, and tagline in the same prompt. If the text must appear in the image, quote it exactly and ask for clean, legible typography.

```
prompt = """
Give me a cool in culture ad / fashion shot for a brand called Thread.
It's a hip young street brand. The ad shows a group of friends hanging out together with the tagline "Yours to Create."
Make it feel like a polished campaign image for a youth streetwear audience: stylish, contemporary, energetic, and tasteful.
Use clean composition, strong color direction, natural poses, and premium fashion photography cues.
Render the tagline exactly once, clearly and legibly, integrated into the ad layout.
No extra text, no watermarks, no unrelated logos.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "thread_ad_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/thread_ad_gpt-image-2.png)

## 中文整理

为名为 Thread 的年轻街头品牌创作一张文化/时尚广告图。画面是一群朋友一起消磨时光，带有标语“Yours to Create.”。面向年轻街头服饰受众，整体要时髦、当代、有活力且得体；使用干净构图、明确色彩方向、自然姿势和高端时尚摄影语言。标语只出现一次，清晰可读并融入版式，不添加其他文字、水印或无关 Logo。

## 本地图片

- ![thread_ad_gpt-image-2](../../assets/official-cookbook/thread_ad_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `thread_ad_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
