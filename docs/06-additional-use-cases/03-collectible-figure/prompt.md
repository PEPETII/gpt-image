# 6.3 Collectible Action Figure Prompt

Source: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

## Official prompt 1

```text
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
```

## 中文翻译

创建一个放在泡罩包装中的复古螺旋桨玩具飞机收藏手办。飞机有圆形机翼、前置旋转螺旋桨、略有磨损的油漆边缘和经典的童年玩具比例，作为怀旧节日收藏品。包装概念唤起冬日玩具、温暖、想象力和童真；使用高端玩具摄影、真实塑料和涂漆金属材质、影棚灯光、浅景深、清晰标签印刷和高端零售展示。只做原创设计，不要商标、水印或 Logo；只加入文字“Christmas Memories Edition”。

## 可替换变量

可替换收藏品描述、包装概念、材质、摄影方向和 `[SHORT_COPY]`。
