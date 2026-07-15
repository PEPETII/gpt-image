# 5.7 Object Removal

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Official content

## 5.7 Object Removal

Person-in-scene compositing is useful for storyboards, campaigns, and “what if” scenarios where facial/identity preservation matters. Anchor realism by specifying a grounded photographic look (natural lighting, believable detail, no cinematic grading), and lock what must not change about the subject. When available, higher input fidelity helps maintain likeness during larger scene edits.

```
prompt = """
Remove the flower from man's hand. Do not change anything else.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../assets/official-cookbook/man_with_blue_hat.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "man_with_no_flower_gpt-image-2.png")
```

Input and output images:

| Original Input | Output Image |
| --- | --- |
|  |  |

## 中文整理

移除男人手中的花朵，不要改变任何其他内容。

## 本地图片

- ![man_with_blue_hat](../../assets/official-cookbook/man_with_blue_hat.png)
- ![man_with_no_flower_gpt-image-2](../../assets/official-cookbook/man_with_no_flower_gpt-image-2.png)

## 输入/输出角色

| 文件 | 角色 |
|---|---|
| `man_with_blue_hat.png` | input |
| `man_with_no_flower_gpt-image-2.png` | output |

## 复现说明

本目录中的提示词和代码按官方页面整理；运行代码前请按第 3 章配置环境变量，并检查输入图片路径。
