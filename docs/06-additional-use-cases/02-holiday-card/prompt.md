# 6.2 3D pop-up holiday card Prompt

Source: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

## Official prompt 1

```text
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
```

## 中文翻译

创建一张圣诞节日贺卡插画：温馨的圣诞场景中，一只略有磨损、带柔软修补针脚的旧泰迪熊坐在纪念盒里，窗外正在下雪，暗示孩子已经长大但记忆仍在。氛围温暖、怀旧、柔和而感人；采用高端节日卡片摄影、柔和电影感灯光、真实纹理、浅景深、得体的散景灯光和适合印刷的构图。只使用原创艺术，不要商标、水印或 Logo；只加入文字“Merry Christmas — some memories never fade.”。

## 可替换变量

可替换节日、场景描述、氛围、纸张/材质风格和 `[SHORT_COPY]`。
