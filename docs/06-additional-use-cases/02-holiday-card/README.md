# 6.2 3D pop-up holiday card

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 6.2 3D pop-up holiday card (product-style mock)

Ideal for seasonal marketing concepts and print previews. Emphasizes tactile realism—paper layers, fibers, folds, and soft studio lighting—so the result reads as a photographed physical product rather than a flat illustration.

```
scene_description = (
    "a cozy Christmas scene with an old teddy bear sitting inside a keepsake box, "
    "slightly worn fur, soft stitching repairs, placed near a window with falling snow outside. "
    "The scene suggests the child has grown up, but the memories remain."
)

short_copy = "Merry Christmas — some memories never fade."

prompt = f"""
Create a Christmas holiday card illustration.

Scene:
{scene_description}

Mood:
Warm, nostalgic, gentle, emotional.

Style:
Premium holiday card photography, soft cinematic lighting,
realistic textures, shallow depth of field,
tasteful bokeh lights, high print-quality composition.

Constraints:
- Original artwork only
- No trademarks
- No watermarks
- No logos

Include ONLY this card text (verbatim):
"{short_copy}"
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "christmas_holiday_card_teddy_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/christmas_holiday_card_teddy_gpt-image-2.png)

## 中文整理

创建一张圣诞节日贺卡插画：温馨的圣诞场景中，一只略有磨损、带柔软修补针脚的旧泰迪熊坐在纪念盒里，窗外正在下雪，暗示孩子已经长大但记忆仍在。氛围温暖、怀旧、柔和而感人；采用高端节日卡片摄影、柔和电影感灯光、真实纹理、浅景深、得体的散景灯光和适合印刷的构图。只使用原创艺术，不要商标、水印或 Logo；只加入文字“Merry Christmas — some memories never fade.”。

## 本地图片

- ![christmas_holiday_card_teddy_gpt-image-2](../../assets/official-cookbook/christmas_holiday_card_teddy_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `christmas_holiday_card_teddy_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
