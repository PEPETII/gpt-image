# 贡献指南

本项目按 OpenAI Cookbook [GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) 整理。贡献应保持官方章节目录为唯一正文来源，并明确区分官方内容、中文翻译和本项目补充说明。

## 文档与提示词

- 新增或修正官方章节内容时，修改对应的 `docs/01-06/**` 目录；
- 生成、编辑和高级用例分别放在 `docs/04-generate/`、`docs/05-edit/` 和 `docs/06-additional-use-cases/` 下的编号目录；
- 每个用例应保持 `README.md`、`prompt.md`、`example.py` 和本地图片角色索引的一致性；
- `prompts/README.md` 只做章节导航，不新增与 `docs/` 重复的完整 prompt 正文；
- API 内容只使用当前 `gpt-image-2` Image API，不添加 `input_fidelity`、旧模型或未经官方文档确认的字段；
- 网页版提示词不得混入 Python、SDK 或 API 参数。

## 图片资源

官方页面图片必须保留原文件名、格式和字节内容，并在 `docs/assets/official-cookbook/manifest.json` 中记录官方 URL、本地路径、所属章节、输入/输出角色、下载时间和 SHA-256。不要把仓库 MIT 许可证解释为覆盖 OpenAI 图片资产。

## Python 示例

- 使用 OpenAI Python SDK；
- 示例必须通过 AST 解析，且不在验证阶段调用真实 API；
- 输入图片使用 manifest 中的本地官方资源或清晰标注的用户路径；
- 结果保存代码应处理 `result.data[0].b64_json`；
- 每个多图输入都要在 prompt 和 README 中说明角色及顺序。

## 验证

提交前至少运行：

```bash
python -X utf8 "scripts/sync_official_cookbook_guide.py" --dry-run
python -X utf8 -m py_compile "scripts/sync_official_cookbook_guide.py"
git diff --check
```

并检查 6 个主章节、23 个用例、37 个图片哈希、两个 skill 的 `quick_validate.py` 结果。不要提交、推送或调用真实图像 API作为文档验证的一部分。

## 提交规范

```text
<type>(<scope>): <description>
```

常用类型：`docs`、`fix`、`i18n`、`refactor`。
