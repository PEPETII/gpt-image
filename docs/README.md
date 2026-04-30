# GPT Image 提示词指南 | GPT Image Prompting Guide

> 基于 OpenAI 官方《GPT Image Generation Models Prompting Guide》编写的详细说明文档，涵盖模型参数、提示词原理、生成与编辑用例，以及高级工作流。

---

## 项目简介

本项目是 OpenAI 官方 GPT 图像生成模型提示词指南的中文详解文档。文档涵盖以下核心内容：

- **图像模型概述**：`gpt-image-2`、`gpt-image-1.5`、`gpt-image-1`、`gpt-image-1-mini` 四款模型的参数与选型建议
- **提示词基本原理**：结构化提示词、约束条件、文字渲染、身份保持等核心技巧
- **环境设置**：Python SDK 安装、API Key 配置、generate 与 edit 两种模式的代码模板
- **生成用例**（10个）：信息图表、图片翻译、照片级写实、世界知识、Logo 生成、广告生成、故事转漫画、UI 模型、科学/教育、幻灯片/图表
- **编辑用例**（9个）：风格迁移、虚拟试穿、素描转图像、产品模型、营销创意、光照天气变换、物品移除、人物插入场景、多图合成
- **高级用例**（4个）：室内设计替换、3D 立体贺卡、收藏级手办/毛绒钥匙扣、儿童绘本艺术（多图工作流）

---

## 文档目录

| 文档 | 章节 | 说明 |
|------|------|------|
| [01-introduction.md](01-introduction.md) | 第1章：引言 | 图像模型概述、模型参数表、常用尺寸、模型选择建议 |
| [02-prompting-fundamentals.md](02-prompting-fundamentals.md) | 第2章：提示词基本原理 | 提示词结构化、约束条件、文字渲染、身份保持、迭代优化 |
| [03-setup.md](03-setup.md) | 第3章：环境设置 | SDK 安装、API Key 配置、generate/edit 代码模板 |
| [04-generate-use-cases.md](04-generate-use-cases.md) | 第4章：生成用例 | 10 个 text-to-image 用例详解与最佳实践 |
| [05-edit-use-cases.md](05-edit-use-cases.md) | 第5章：编辑用例 | 9 个 image-editing 用例详解与最佳实践 |
| [06-additional-use-cases.md](06-additional-use-cases.md) | 第6章：其他高价值用例 | 4 个高级用例详解，含完整提示词与多步骤工作流 |

---

## 快速开始

### 1. 安装依赖

```bash
pip install openai
```

### 2. 配置 API Key

```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

### 3. 生成第一张图片

```python
from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="gpt-image-2",
    prompt="A serene Japanese garden with cherry blossoms, koi pond, and stone lanterns",
    size="1024x1024",
    quality="medium",
)

# 保存图像
with open("output.png", "wb") as f:
    f.write(response.data[0].b64_json_bytes)
```

### 4. 编辑一张图片

```python
from openai import OpenAI

client = OpenAI()

with open("input.png", "rb") as f:
    image_data = f.read()

response = client.images.edit(
    model="gpt-image-2",
    prompt="Change the background to a sunset sky",
    image=image_data,
    input_fidelity="high",
    size="1024x1024",
    quality="medium",
)

with open("output.png", "wb") as f:
    f.write(response.data[0].b64_json_bytes)
```

---

## 提示词模板

所有提示词模板位于 [`prompts/`](../prompts/README.md) 目录下，按生成类（generate）和编辑类（edit）分类，每个模板包含英文原文、中文翻译、关键技巧和 API 参数建议。

---

## 代码示例

可运行的 Python 代码示例位于 [`examples/`](../examples/) 目录下，包含生成类、编辑类和高级案例的完整代码。

---

## 来源声明

所有提示词和指南内容均来源于 OpenAI 官方开发者文档。本项目仅做整理、翻译和补充说明，供开发者学习参考。
