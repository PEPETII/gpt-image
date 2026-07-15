# 4.3 Photorealistic Images

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 4.3 Photorealistic Images that Feel “natural”

To get believable photorealism, prompt the model as if a real photo is being captured in the moment. Use photography language (lens, lighting, framing) and explicitly ask for real texture (pores, wrinkles, fabric wear, imperfections). Avoid words that imply studio polish or staging. When detail matters, set quality=“high”.

```
prompt = """
Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.
He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.
He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "photorealism-gpt-image-2.png")
```

Output Image:

![](../../assets/official-cookbook/photorealism-gpt-image-2.png)

## 中文整理

创建一张照片级写实的抓拍照片：一位年长的水手站在小渔船上，皮肤有风吹日晒的纹理和皱纹，手臂上有褪色的传统水手纹身。他正在平静地整理渔网，旁边的甲板上坐着他的狗。画面像 35mm 胶片照片，以平视中近景和 50mm 镜头拍摄；使用柔和的海岸日光、浅景深、轻微胶片颗粒和自然色彩。画面应真实、不摆拍，不要过度美化或重度修图。

## 本地图片

- ![photorealism-gpt-image-2](../../assets/official-cookbook/photorealism-gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `photorealism-gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
