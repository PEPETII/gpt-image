# Python 代码示例 | Python Code Examples

本目录包含 GPT Image 2 的完整 Python 调用示例，基于 OpenAI 官方提示词指南。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

### 3. 运行示例

```bash
# 生成类案例（4.1-4.10）
python generate_examples.py

# 编辑类案例（5.1-5.9），需要输入图像
python edit_examples.py

# 高级案例（6.1-6.4），含多步骤工作流
python advanced_examples.py
```

## 文件说明

| 文件 | 说明 | 案例数量 |
|------|------|---------|
| `generate_examples.py` | 生成类案例 (text → image) | 10 个 |
| `edit_examples.py` | 编辑类案例 (text + image → image) | 9 个 |
| `advanced_examples.py` | 高级案例（多步骤工作流） | 4 个 |

## 输入图像

编辑类案例需要输入图像，请将图片放在项目根目录的 `images/` 文件夹中。
所需的图像文件名在每个函数的注释中已标注。

## 输出

生成的图像将保存在 `output_images/` 目录下，文件名格式为 `{案例名}_{序号}.png`。

## 注意事项

- 运行前请确保已设置 `OPENAI_API_KEY` 环境变量
- 编辑类案例需要对应的输入图像文件
- 每次API调用都会消耗额度，建议先运行单个案例测试
- 生成类案例中 4.2（图片翻译）需要编辑模式，已标注说明
