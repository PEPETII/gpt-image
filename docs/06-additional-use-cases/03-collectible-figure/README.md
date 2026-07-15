# 6.3 Collectible Action Figure

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 6.3 Collectible Action Figure / Plush Keychain (merch concept)

Used for early merch ideation and pitch visuals. Focuses on premium product photography cues (materials, packaging, print clarity) while keeping designs original and non-infringing. Works well for testing multiple character or packaging variants quickly.

```
# ---- Inputs ----
character_description = (
    "a vintage-style toy propeller airplane with rounded wings, "
    "a front-mounted spinning propeller, slightly worn paint edges, "
    "classic childhood proportions, designed as a nostalgic holiday collectible"
)

short_copy = "Christmas Memories Edition"

# ---- Prompt ----
prompt = f"""
Create a collectible action figure of {character_description}, in blister packaging.

Concept:
A nostalgic holiday collectible inspired by the simple toy airplanes
children used to play with during winter holidays.
Evokes warmth, imagination, and childhood wonder.

Style:
Premium toy photography, realistic plastic and painted metal textures,
studio lighting, shallow depth of field,
sharp label printing, high-end retail presentation.

Constraints:
- Original design only
- No trademarks
- No watermarks
- No logos

Include ONLY this packaging text (verbatim):
"{short_copy}"
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "christmas_collectible_toy_airplane_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/christmas_collectible_toy_airplane_gpt-image-2.png)

## 中文整理

创建一个放在泡罩包装中的复古螺旋桨玩具飞机收藏手办。飞机有圆形机翼、前置旋转螺旋桨、略有磨损的油漆边缘和经典的童年玩具比例，作为怀旧节日收藏品。包装概念唤起冬日玩具、温暖、想象力和童真；使用高端玩具摄影、真实塑料和涂漆金属材质、影棚灯光、浅景深、清晰标签印刷和高端零售展示。只做原创设计，不要商标、水印或 Logo；只加入文字“Christmas Memories Edition”。

## 本地图片

- ![christmas_collectible_toy_airplane_gpt-image-2](../../assets/official-cookbook/christmas_collectible_toy_airplane_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `christmas_collectible_toy_airplane_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
