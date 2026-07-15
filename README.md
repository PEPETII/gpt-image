# GPT Image 官方提示词指南

> 基于 OpenAI Cookbook《GPT Image Generation Models Prompting Guide》的中文整理、官方示例和本地图片索引。

[English](README_en.md) | [官方 Cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) | MIT License

示例图片：
<img width="600" height="900" alt="new_case051" src="https://github.com/user-attachments/assets/4e800f13-4cf5-4646-acae-8626fe88b9ef" />

使用skills生成提示词：
<img width="1086" height="1448" alt="9b5afbef-814c-4c6c-a1ee-288b2580e091" src="https://github.com/user-attachments/assets/97aa1397-f2f9-4d95-8bd8-ad21db9d7233" />

本项目面向需要让 IDE 编写图片提示词的工作流：输入自然语言需求后，使用 `gpt-image-prompt-web` 生成可复制到 ChatGPT 网页端的英文提示词，或使用 `gpt-image-prompt-api` 生成 `gpt-image-2` Image API 的参数和 Python 示例。

## 内容范围

- 6 个官方主章节，完整保留英文说明并提供中文翻译；
- 23 个官方用例：4.1–4.10 生成、5.1–5.9 编辑、6.1–6.4 高级工作流；
- 37 个官方页面出现的唯一图片资源，原始文件保存在 `docs/assets/official-cookbook/`；
- 每个用例目录包含 `README.md`、`prompt.md`、Python 示例和本地图片角色索引；
- `manifest.json` 记录每个资源的官方 URL、本地路径、所属章节、输入/输出角色、下载时间和 SHA-256。

## 文档导航

| 章节 | 内容 |
|---|---|
| [第 1 章](docs/01-introduction/README.md) | 引言、`gpt-image-2` 能力、尺寸约束和迁移背景 |
| [第 2 章](docs/02-prompting-fundamentals/README.md) | 提示词结构、约束、文字、人物、多图和迭代 |
| [第 3 章](docs/03-setup/README.md) | Cookbook Python 初始化和图片保存 helper |
| [第 4 章](docs/04-generate/README.md) | 10 个 text → image 生成用例 |
| [第 5 章](docs/05-edit/README.md) | 9 个 text + image → image 编辑用例 |
| [第 6 章](docs/06-additional-use-cases/README.md) | 4 个高级场景和多步骤工作流 |

提示词索引见 [prompts/README.md](prompts/README.md)，参数速查见 [cheat-sheet/](cheat-sheet/README.md)，Python 汇总示例见 [examples/](examples/README.md)。

## API 边界

本仓库的 API 示例只使用当前 `gpt-image-2` Image API 的 `images.generate` 和 `images.edit`，不覆盖 Responses API。`gpt-image-2` 会自动以高保真处理图片输入，示例和推荐参数不使用 `input_fidelity`。尺寸、质量、背景、输出格式和压缩规则以 [官方 Image generation 文档](https://developers.openai.com/api/docs/guides/image-generation) 为准。

## 图片资产许可

图片文件来自 OpenAI Cookbook 页面，仅为文档复现和对照而下载；`LICENSE` 中的 MIT 许可不会自动覆盖 OpenAI 图片资产。每个文件的来源和哈希见 [`docs/assets/official-cookbook/manifest.json`](docs/assets/official-cookbook/manifest.json)。

## 快速开始

```bash
pip install openai
```

设置 `OPENAI_API_KEY` 后，可按 [第 3 章](docs/03-setup/README.md) 和 [examples/README.md](examples/README.md) 运行示例。运行真实 API 示例会消耗额度；本次文档重构没有调用真实图片生成 API。

## 贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。新内容应进入对应的 `docs/` 章节目录，避免重新建立与官方章节重复的独立 prompt 正文。
