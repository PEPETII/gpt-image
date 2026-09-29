# gpt-image-2 Image API 内置参考

本文件是 `gpt-image-prompt-api` 的自包含参数和代码参考。它只描述本 skill 输出所需的 Image API 请求形状；不要求联网查文档，也不调用真实服务。

## 范围

- 模型：`gpt-image-2`；
- 操作：`client.images.generate`、`client.images.edit`；
- SDK：Python `openai`；
- 图片结果：从 `result.data[0].b64_json` 解码保存；
- 凭证：由 `OpenAI()` 从环境配置读取；
- 不覆盖 Responses API。

## 参数契约

| 参数 | 适用操作 | 值或规则 |
|---|---|---|
| `model` | 生成、编辑 | 固定为 `"gpt-image-2"` |
| `prompt` | 生成、编辑 | 必填的英文图像指令 |
| `image` | 编辑 | 一张或多张以二进制方式打开的输入图片 |
| `mask` | 编辑 | 局部编辑时可选；应与输入图尺寸匹配并带 alpha 通道 |
| `size` | 生成、编辑 | `"auto"` 或满足尺寸约束的自定义尺寸 |
| `quality` | 生成、编辑 | `"low"`、`"medium"`、`"high"` |
| `n` | 生成、编辑 | 返回数量；未指定时使用 `1` |
| `background` | 生成、编辑 | `"auto"` 或 `"opaque"`；对于 `gpt-image-2` 也可以使用 `"transparent"`（预览） |
| `output_format` | 生成、编辑 | 默认 PNG；需要时使用 `"jpeg"` 或 `"webp"` |
| `output_compression` | 生成、编辑 | 仅 JPEG/WebP 使用，整数范围 `0`–`100` |

### 默认决策

没有特别要求时：

```text
model = "gpt-image-2"
size = "auto"
quality = "medium"
n = 1
background = "auto"
output_format = PNG by omission
```

用户没有明确要求时，不主动增加可选字段。推荐参数表必须只列本次请求真正需要的字段。

### 尺寸约束

自定义尺寸必须同时满足：

- 最大边小于 `3840px`；
- 两条边都是 `16` 的倍数；
- 长短边比例不超过 `3:1`；
- 总像素数不低于 `655,360` 且不超过 `8,294,400`；
- 超过 `2560x1440` 的输出应在说明中标为较高资源消耗的选择。

常用尺寸：`1024x1024`、`1024x1536`、`1536x1024`、`2560x1440`。若用户的尺寸违反约束，应先指出并改用 `auto` 或最近的合规尺寸。

## 生成调用

适用于没有输入图片的任务：

```python
import base64
from openai import OpenAI

client = OpenAI()
result = client.images.generate(
    model="gpt-image-2",
    prompt="""
[English image prompt]
""",
    size="auto",
    quality="medium",
)

image_bytes = base64.b64decode(result.data[0].b64_json)
with open("output.png", "wb") as file:
    file.write(image_bytes)
```

只在用户要求时增加 `n`、`background`、`output_format` 或 `output_compression`。如果输出格式是 JPEG 或 WebP，同步修改保存扩展名。

## 单图编辑调用

适用于有一张输入图片的修改、风格迁移、局部移除或场景变换：

```python
import base64
from openai import OpenAI

client = OpenAI()
with open("input.png", "rb") as image:
    result = client.images.edit(
        model="gpt-image-2",
        image=image,
        prompt="""
Change:
[Only the requested change]

Preserve:
[Identity, geometry, pose, framing, lighting, and other invariants]

Do not change:
Anything outside the requested edit.
""",
        size="auto",
        quality="medium",
    )

image_bytes = base64.b64decode(result.data[0].b64_json)
with open("output.png", "wb") as file:
    file.write(image_bytes)
```

使用遮罩时，在同一个文件打开上下文中加入 `with open("mask.png", "rb") as mask`，再将 `mask=mask` 传给编辑调用。遮罩必须与输入图片对应，且只覆盖允许修改的区域。

## 多图编辑调用

输入列表的顺序必须与 prompt 中的 `Image 1`、`Image 2` 编号完全一致：

```python
import base64
from contextlib import ExitStack
from openai import OpenAI

client = OpenAI()
with ExitStack() as stack:
    images = [
        stack.enter_context(open("base-scene.png", "rb")),
        stack.enter_context(open("insert-object.png", "rb")),
    ]
    result = client.images.edit(
        model="gpt-image-2",
        image=images,
        prompt="""
Image 1 is the base scene. Image 2 is the object to insert.
Place the object from Image 2 at [TARGET LOCATION] in Image 1.
Preserve Image 1 except for this change, and match scale, perspective, lighting, shadows, and depth of field.
""",
        size="auto",
        quality="medium",
    )

image_bytes = base64.b64decode(result.data[0].b64_json)
with open("output.png", "wb") as file:
    file.write(image_bytes)
```

多图中文说明必须逐项列出文件路径、图片编号、输入角色和目标关系；不能只说“参考上面的图片”。

## 代码检查清单

- import、客户端初始化、请求和结果保存均存在；
- `generate` 不接收输入图片，`edit` 明确打开输入图片；
- 多图列表和 prompt 编号相同；
- 输出扩展名与 `output_format` 一致；
- 代码不包含硬编码密钥、不打印响应中的敏感信息；
- 只做 AST 解析或静态检查，不执行请求。
