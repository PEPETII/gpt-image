# GPT Image 文档目录

本目录完全按 OpenAI Cookbook [GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) 的第 1–6 章组织。英文正文、中文翻译、官方提示词、Python 示例和官方图片索引均以新章节目录为唯一正文来源。

## 主章节

| 目录 | 官方章节 | 内容 |
|---|---|---|
| [01-introduction](01-introduction/README.md) | 1. Introduction | 模型能力、`gpt-image-2` 尺寸约束和迁移背景 |
| [02-prompting-fundamentals](02-prompting-fundamentals/README.md) | 2. Prompting Fundamentals | 结构、质量线索、约束、文字、人物和多图提示 |
| [03-setup](03-setup/README.md) | 3. Setup | Python SDK 初始化和结果保存 helper |
| [04-generate](04-generate/README.md) | 4. Use Cases — Generate | 10 个生成用例和独立子目录 |
| [05-edit](05-edit/README.md) | 5. Use cases — Edit | 9 个编辑用例和独立子目录 |
| [06-additional-use-cases](06-additional-use-cases/README.md) | 6. Additional High-Value Use Cases | 4 个高级用例和多步骤工作流 |

## 用例数量

- 生成：4.1–4.10，共 10 个；
- 编辑：5.1–5.9，共 9 个；
- 高级：6.1–6.4，共 4 个；
- 合计：23 个官方用例。

每个用例目录包含：

- `README.md`：官方英文说明、中文翻译、适用场景、关键技巧、来源、本地图片和输入/输出角色；
- `prompt.md`：官方原始 prompt、中文翻译和可替换变量；
- `example.py`：只将官方 notebook 路径改为本地资源路径的 Python 示例；
- `docs/assets/official-cookbook/manifest.json`：官方图片来源、角色和 SHA-256 索引。

## 图片资产

官方页面出现的 37 个唯一图片资源保存在 [`assets/official-cookbook/`](assets/official-cookbook/)；输入图片在多个用例中复用但只保存一份。图片来源和哈希见 [`assets/official-cookbook/manifest.json`](assets/official-cookbook/manifest.json)。仓库 MIT 许可不自动覆盖这些 OpenAI 图片资产。

## API 说明

本目录中的 API 示例固定使用 `gpt-image-2` 的 `images.generate` 和 `images.edit`，不覆盖 Responses API。`gpt-image-2` 的图片输入自动按高保真处理，不传 `input_fidelity`。当前参数事实来源是 [OpenAI Image generation](https://developers.openai.com/api/docs/guides/image-generation)。

## 运行示例

```bash
pip install openai
```

设置 `OPENAI_API_KEY` 后，按 [03-setup](03-setup/README.md) 配置环境。文档验证只进行静态解析、哈希和路径检查，不调用真实图片生成 API。
