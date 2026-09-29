# 3. Setup

> 官方来源：[https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## 章节目录

本章没有独立用例子章节。

## Official content

## 3. Setup

Run this once. It:

- creates the API client
- creates `output_images/` in the images folder.
- adds a small helper to save base64 images

Put any reference images used for edits into `input_images/` (or update the paths in the examples). When saving transparent outputs, use a `.png` or `.webp` extension matching the selected output format and preserve the returned image bytes; converting an RGBA image to RGB discards its transparent background.

```
import os
import base64
from openai import OpenAI

client = OpenAI()

os.makedirs("input_images", exist_ok=True)
os.makedirs("output_images", exist_ok=True)

def save_image(result, filename: str) -> None:
    """
    Saves the first returned image to the given filename inside the output_images folder.
    """
    image_base64 = result.data[0].b64_json
    out_path = os.path.join("output_images", filename)
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(image_base64))


def display_image_grid(items, width=240):
    cards = []
    for item in items:
        title = item.get("title", "")
        label = f'<div style="font-weight:600;margin-bottom:8px">{title}</div>' if title else ""
        cards.append(
            '<div style="text-align:center">'
            + label
            + f'<img src="{item["path"]}" width="{width}" style="max-width:100%;height:auto;" />'
            + '</div>'
        )
    display(HTML('<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start">' + ''.join(cards) + '</div>'))
```

The examples below uses our most capable image model `gpt-image-2`

## 中文翻译

第 3 章的初始化代码只需要运行一次：创建 OpenAI 客户端、创建输入和输出图片目录，并提供一个把 base64 结果保存为文件的 helper。编辑用的参考图片放到 `input_images/`，或按实际路径修改示例。

官方示例使用 Python SDK 和 `gpt-image-2`。仓库中的每个用例示例已将 notebook 的相对路径改为 `docs/assets/official-cookbook/` 下的本地资源；运行前请设置 `OPENAI_API_KEY`。生成使用 `client.images.generate`，编辑使用 `client.images.edit`。

`gpt-image-2` 的图片输入自动按高保真处理，因此编辑和参考图工作流不需要、也不应添加 `input_fidelity`。输出数据从 `result.data[0].b64_json` 解码后保存。第 3 章的官方 helper 只是文件保存工具，不代表项目覆盖 Responses API。

