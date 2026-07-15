# `gpt-image-2` Image API 参数速查

事实来源：[OpenAI Image generation](https://developers.openai.com/api/docs/guides/image-generation)。本表只覆盖 Image API 的 `images.generate` 和 `images.edit`，不覆盖 Responses API。

## 当前字段

| 参数 | 用途 | 推荐规则 |
|---|---|---|
| `model` | 模型 | 固定为 `"gpt-image-2"` |
| `prompt` | 生成或编辑指令 | 必填；使用具体英文自然语言 |
| `image` | 编辑输入 | 仅 `images.edit` 使用；按 prompt 中的 Image 编号传入 |
| `size` | 输出尺寸 | `auto` 或符合官方约束的自定义尺寸 |
| `quality` | 渲染质量 | `low`、`medium`、`high` |
| `n` | 返回数量 | 默认 `1`，只有明确需要多候选时增加 |
| `background` | 背景 | `auto` 或 `opaque`；`gpt-image-2` 不支持透明背景 |
| `output_format` | 输出格式 | 默认 PNG；需要时使用 JPEG 或 WebP |
| `output_compression` | 压缩 | 只用于 JPEG/WebP，范围 `0`–`100` |

## 尺寸约束

自定义 `size` 必须满足：最大边小于 `3840px`；宽高都是 `16` 的倍数；长短边比例不超过 `3:1`；总像素数在 `655,360` 到 `8,294,400` 之间。超过 `2560x1440` 的尺寸应视为实验性输出。

常用参考：`1024x1024`、`1024x1536`、`1536x1024`、`2560x1440`。具体用例的官方尺寸以对应章节 `example.py` 为准。

## 生成

```python
import base64
from openai import OpenAI

client = OpenAI()
result = client.images.generate(
    model="gpt-image-2",
    prompt="[English prompt]",
    size="1024x1024",
    quality="medium",
)

with open("output.png", "wb") as file:
    file.write(base64.b64decode(result.data[0].b64_json))
```

## 编辑

```python
import base64
from openai import OpenAI

client = OpenAI()
with open("input.png", "rb") as image:
    result = client.images.edit(
        model="gpt-image-2",
        image=[image],
        prompt="Change only [target]. Preserve [invariants].",
        size="1024x1024",
        quality="medium",
    )

with open("output.png", "wb") as file:
    file.write(base64.b64decode(result.data[0].b64_json))
```

图片输入会由 `gpt-image-2` 自动按高保真处理，不传 `input_fidelity`。复杂编辑中，用 prompt 明确 `Change`、`Preserve` 和 `Do not change`。
