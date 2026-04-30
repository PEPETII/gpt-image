# 第3章：环境设置 | Setup

> 本章介绍如何安装 OpenAI Python SDK、配置 API Key，以及使用 Generate 和 Edit 两种模式的代码模板。

---

## 3.1 安装 OpenAI Python SDK

### 系统要求

- Python 3.8 或更高版本
- pip 包管理器

### 安装命令

```bash
pip install openai
```

### 验证安装

```bash
python -c "import openai; print(openai.__version__)"
```

---

## 3.2 API Key 配置

### 方式一：环境变量（推荐）

通过环境变量 `OPENAI_API_KEY` 配置，这是最安全的方式：

```bash
# Linux / macOS
export OPENAI_API_KEY="sk-your-api-key-here"

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-your-api-key-here"
```

> **安全提示**：不要将 API Key 硬编码在代码中，也不要提交到 Git 仓库。建议将 `.env` 文件添加到 `.gitignore`。

### 方式二：.env 文件

创建 `.env` 文件：

```env
OPENAI_API_KEY=sk-your-api-key-here
```

然后在代码中加载：

```python
from dotenv import load_dotenv
load_dotenv()  # 加载 .env 文件中的环境变量
```

### 方式三：直接传入（不推荐）

```python
from openai import OpenAI

client = OpenAI(api_key="sk-your-api-key-here")
```

> **注意**：此方式仅适合快速测试，生产环境请使用环境变量。

---

## 3.3 基本代码模板

### 3.3.1 Generate 模式（文本生成图像）

Generate 模式从文本提示词生成全新图像。

```python
from openai import OpenAI

client = OpenAI()

# 生成图像
response = client.images.generate(
    model="gpt-image-2",       # 模型选择
    prompt="A serene Japanese garden with cherry blossoms",  # 文本提示词
    size="1024x1024",          # 图像尺寸（宽x高）
    quality="medium",          # 输出质量：low / medium / high
    n=1,                       # 生成变体数量
)

# 获取生成的图像数据
image_data = response.data[0]

# 保存图像
with open("output.png", "wb") as f:
    f.write(image_data.b64_json_bytes)

print("图像已保存到 output.png")
```

#### Generate 模式参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | str | 是 | 模型名称：`"gpt-image-2"`, `"gpt-image-1.5"`, `"gpt-image-1"`, `"gpt-image-1-mini"` |
| `prompt` | str | 是 | 文本提示词，描述要生成的图像 |
| `size` | str | 否 | 图像尺寸，格式 `"宽x高"`，默认 `"1024x1024"` |
| `quality` | str | 否 | 输出质量：`"low"`, `"medium"`, `"high"`，默认 `"medium"` |
| `n` | int | 否 | 生成变体数量，默认 `1` |
| `background` | str | 否 | 背景设置：`"opaque"` 不透明背景 |

---

### 3.3.2 Edit 模式（图像编辑）

Edit 模式基于输入图像进行修改和编辑。

```python
from openai import OpenAI

client = OpenAI()

# 读取输入图像
with open("input.png", "rb") as f:
    image_data = f.read()

# 编辑图像
response = client.images.edit(
    model="gpt-image-2",       # 模型选择
    prompt="Change the background to a sunset sky",  # 编辑指令
    image=image_data,          # 输入图像（二进制数据）
    input_fidelity="high",     # 输入图像保真度：low / medium / high
    size="1024x1024",          # 输出图像尺寸
    quality="medium",          # 输出质量
)

# 获取编辑后的图像数据
image_data = response.data[0]

# 保存图像
with open("output.png", "wb") as f:
    f.write(image_data.b64_json_bytes)

print("编辑后的图像已保存到 output.png")
```

#### Edit 模式参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | str | 是 | 模型名称 |
| `prompt` | str | 是 | 编辑指令，描述要进行的修改 |
| `image` | bytes | 是 | 输入图像的二进制数据 |
| `input_fidelity` | str | 否 | 输入图像保真度：`"low"`, `"medium"`, `"high"`，默认 `"medium"` |
| `size` | str | 否 | 输出图像尺寸，默认与输入图像相同 |
| `quality` | str | 否 | 输出质量，默认 `"medium"` |

---

## 3.4 输出图像保存方法

### 方法一：保存为 PNG 文件

```python
with open("output.png", "wb") as f:
    f.write(response.data[0].b64_json_bytes)
```

### 方法二：保存多个变体

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt="A sunset over the ocean",
    size="1024x1024",
    quality="medium",
    n=3,  # 生成3个变体
)

for i, image in enumerate(response.data):
    filename = f"output_variant_{i+1}.png"
    with open(filename, "wb") as f:
        f.write(image.b64_json_bytes)
    print(f"已保存: {filename}")
```

### 方法三：指定输出目录

```python
import os

output_dir = "output_images"
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "output.png"), "wb") as f:
    f.write(response.data[0].b64_json_bytes)
```

---

## 3.5 完整示例脚本

以下是一个完整的示例脚本，包含 Generate 和 Edit 两种模式：

```python
"""
GPT Image 生成与编辑示例
"""
import os
from openai import OpenAI

# 初始化客户端（自动读取 OPENAI_API_KEY 环境变量）
client = OpenAI()

# 创建输出目录
os.makedirs("output_images", exist_ok=True)


def generate_image(prompt: str, size: str = "1024x1024",
                   quality: str = "medium", n: int = 1) -> list[str]:
    """使用 Generate 模式生成图像"""
    response = client.images.generate(
        model="gpt-image-2",
        prompt=prompt,
        size=size,
        quality=quality,
        n=n,
    )

    saved_files = []
    for i, image in enumerate(response.data):
        filename = f"output_images/generate_{i+1}.png"
        with open(filename, "wb") as f:
            f.write(image.b64_json_bytes)
        saved_files.append(filename)
        print(f"已生成: {filename}")

    return saved_files


def edit_image(prompt: str, input_path: str,
               input_fidelity: str = "high",
               size: str = "1024x1024",
               quality: str = "medium") -> str:
    """使用 Edit 模式编辑图像"""
    with open(input_path, "rb") as f:
        image_data = f.read()

    response = client.images.edit(
        model="gpt-image-2",
        prompt=prompt,
        image=image_data,
        input_fidelity=input_fidelity,
        size=size,
        quality=quality,
    )

    filename = "output_images/edit_output.png"
    with open(filename, "wb") as f:
        f.write(response.data[0].b64_json_bytes)
    print(f"已编辑: {filename}")

    return filename


if __name__ == "__main__":
    # Generate 示例
    generate_image(
        prompt="A serene Japanese garden with cherry blossoms and a koi pond",
        size="1024x1024",
        quality="medium",
    )

    # Edit 示例（需要先有 input.png）
    # edit_image(
    #     prompt="Change the background to a sunset sky",
    #     input_path="input.png",
    #     input_fidelity="high",
    # )
```

---

## 3.6 常见问题

| 问题 | 解决方案 |
|------|----------|
| `AuthenticationError` | 检查 `OPENAI_API_KEY` 是否正确设置 |
| `InvalidImageSize` | 确保尺寸格式为 `"宽x高"`，两边为 16 的倍数，长宽比不超过 3:1 |
| `RateLimitError` | 降低请求频率，或升级 API 计划 |
| `InvalidModelError` | 确认模型名称正确：`"gpt-image-2"`, `"gpt-image-1.5"`, `"gpt-image-1"`, `"gpt-image-1-mini"` |
| 输出图像模糊 | 尝试使用 `quality="high"` 或增大输出尺寸 |

---

> 上一章：[02-prompting-fundamentals.md](02-prompting-fundamentals.md) — 提示词基本原理
>
> 下一章：[04-generate-use-cases.md](04-generate-use-cases.md) — 生成用例
