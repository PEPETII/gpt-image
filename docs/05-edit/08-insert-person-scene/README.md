# 5.8 Insert the Person Into a Scene

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 5.8 Insert the Person Into a Scene

Person-in-scene compositing is useful for storyboards, campaigns, and “what if” scenarios where facial/identity preservation matters. Anchor realism by specifying a grounded photographic look (natural lighting, believable detail, no cinematic grading), and lock what must not change about the subject. When available, higher input fidelity helps maintain likeness during larger scene edits.

```
prompt = """
Generate a highly realistic action scene where this person is running away from a large, realistic brown bear attacking a campsite. The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
She is centered in the image but looking away from the camera, wearing outdoorsy camping attire, with dirt on her face and tears in her clothing. She is clearly afraid but focused on escaping, running away from the bear as it destroys the campsite behind her.
The campsite is in Yosemite National Park, with believable natural details. The time of day is dusk, with natural lighting and realistic colors. Everything should feel grounded, authentic, and unstyled, as if captured in a real moment. Avoid cinematic lighting, dramatic color grading, or stylized composition.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/woman_in_museum.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "scene_gpt-image-2.png")
```

Output Image:

```
```

## 中文整理

生成一个高度写实的动作场景：图中人物正在逃离一只攻击露营地的大型写实棕熊。画面像真实照片，而不是过度增强或电影海报；她位于画面中央但看向远处，穿户外露营服，脸上有泥土、衣服有撕裂，既害怕又专注于逃跑。露营地位于约塞米蒂国家公园，背景有可信的自然细节；时间是黄昏，使用自然光和真实色彩。整体要朴素、真实、没有风格化处理，不要电影式灯光、戏剧化调色或过度设计的构图。

## 本地图片

- ![woman_in_museum](../../assets/official-cookbook/woman_in_museum.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `woman_in_museum.png` | input: person |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
