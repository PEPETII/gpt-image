# 4.7 Story-to-Comic Strip

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.7 Story-to-Comic Strip

For story-to-comic generation, define the narrative as a sequence of clear visual beats, one per panel. Keep descriptions concrete and action-focused so the model can translate the story into readable, well-paced panels.

```
prompt = """
Create a short vertical comic-style reel with 4 equal-sized panels.
Panel 1: The owner leaves through the front door. The pet is framed in the window behind them, small against the glass, eyes wide, paws pressed high, the house suddenly quiet.
Panel 2: The door clicks shut. Silence breaks. The pet slowly turns toward the empty house, posture shifting, eyes sharp with possibility.
Panel 3: The house transformed. The pet sprawls across the couch like it owns the place, crumbs nearby, sunlight cutting across the room like a spotlight.
Panel 4: The door opens. The pet is seated perfectly by the entrance, alert and composed, as if nothing happened.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "comic_reel-gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/comic_reel-gpt-image-2.png)

## 中文整理

创建一条短的竖版漫画风视频缩略图，包含 4 个大小相同的面板。第 1 格：主人从前门离开，宠物被框在身后的窗户里，眼睛睁大、爪子高高贴在玻璃上。第 2 格：门咔哒一声关上，宠物转身面对空房子，眼神逐渐变得精明。第 3 格：房子已经变样，宠物像房子的主人一样摊在沙发上，旁边有碎屑，阳光像聚光灯一样穿过房间。第 4 格：门打开，宠物端坐在入口处，仿佛什么也没有发生。

## 本地图片

- ![comic_reel-gpt-image-2](../../assets/official-cookbook/comic_reel-gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `comic_reel-gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
