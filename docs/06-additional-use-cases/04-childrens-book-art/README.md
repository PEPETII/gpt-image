# 6.4 Children’s Book Art

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 6.4 Children’s Book Art with Character Consistency (multi-image workflow)

Designed for multi-page illustration pipelines where character drift is unacceptable. A reusable “character anchor” ensures visual continuity across scenes, poses, and pages while allowing environmental and narrative variation.

1️⃣ Character Anchor — establish the reusable main character

Goal: Lock the character’s appearance, proportions, outfit, and tone.

```
# ---- Inputs ----
prompt = """
Create a children’s book illustration introducing a main character.

Character:
A young, storybook-style hero inspired by a little forest outlaw,
wearing a simple green hooded tunic, soft brown boots, and a small belt pouch.
The character has a kind expression, gentle eyes, and a brave but warm demeanor.
Carries a small wooden bow used only for helping, never harming.

Theme:
The character protects and rescues small forest animals like squirrels, birds, and rabbits.

Style:
Children’s book illustration, hand-painted watercolor look,
soft outlines, warm earthy colors, whimsical and friendly.
Proportions suitable for picture books (slightly oversized head, expressive face).

Constraints:
- Original character (no copyrighted characters)
- No text
- No watermarks
- Plain forest background to clearly showcase the character
"""

# ---- Image generation ----
result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "childrens_book_illustration_1_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/childrens_book_illustration_1_gpt-image-2.png)

2️⃣ Story continuation — reuse character, advance the narrative

Goal: Same character, new scene + action.
Character appearance must remain unchanged.

```
# ---- Inputs ----
prompt = """
Continue the children’s book story using the same character.

Scene:
The same young forest hero is gently helping a frightened squirrel
out of a fallen tree after a winter storm.
The character kneels beside the squirrel, offering reassurance.

Character Consistency:
- Same green hooded tunic
- Same facial features, proportions, and color palette
- Same gentle, heroic personality

Style:
Children’s book watercolor illustration,
soft lighting, snowy forest environment,
warm and comforting mood.

Constraints:
- Do not redesign the character
- No text
- No watermarks
"""
# ---- Image generation ----
result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/childrens_book_illustration_1_gpt-image-2.png", "rb"),  # use image from step 1
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "childrens_book_illustration_2_gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/childrens_book_illustration_2_gpt-image-2.png)

## 中文整理

第一步：创建一张儿童绘本插画来介绍主角。主角是受森林小侠启发的年轻绘本英雄，穿绿色连帽上衣、柔软棕色靴子并带小腰包，表情善良、眼神温和，勇敢但亲切，携带只用于帮助而不伤害他人的小木弓。主题是保护和救助松鼠、鸟和兔子等小动物；使用手绘水彩、柔和轮廓、温暖土色和友善奇幻的绘本风格，背景保持简单的森林。第二步：继续同一个儿童故事，让同一位英雄在暴风雪后的倒树旁温柔地帮助受惊的松鼠；保持同样的绿色上衣、面部特征、比例、色彩和性格，不要重新设计角色、文字或水印。

## 本地图片

- ![childrens_book_illustration_1_gpt-image-2](../../assets/official-cookbook/childrens_book_illustration_1_gpt-image-2.png)
- ![childrens_book_illustration_2_gpt-image-2](../../assets/official-cookbook/childrens_book_illustration_2_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `childrens_book_illustration_1_gpt-image-2.png` | output and next-step input |
| `childrens_book_illustration_2_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
