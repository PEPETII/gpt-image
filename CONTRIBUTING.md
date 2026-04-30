# 贡献指南 | Contributing Guide

感谢你对本项目的关注！以下是参与贡献的方式。

## 如何贡献

### 1. 提交新的提示词模板

如果你发现了好的提示词写法或新的用例场景，欢迎提交：

- 在 `prompts/generate/` 或 `prompts/edit/` 目录下创建新的 `.md` 文件
- 文件名使用小写 kebab-case（如 `my-new-prompt.md`）
- 按照现有文件的格式模板编写（标题、英文提示词、中文翻译、技巧说明、参数建议）

### 2. 改进现有提示词

如果你发现某个提示词可以优化：

- 直接修改对应的 `.md` 文件
- 在 PR 中说明改进点和效果对比

### 3. 添加代码示例

在 `examples/` 目录下添加新的 Python 示例：

- 使用 `openai` SDK
- 包含完整的参数注释
- 通过环境变量读取 API Key

### 4. 翻译和文档改进

- 改进中文翻译的准确性
- 补充文档中的遗漏内容
- 修复错别字和格式问题

## 提交规范

### Commit Message 格式

```
<type>(<scope>): <description>

类型:
- feat: 新功能/新提示词
- fix: 修复错误
- docs: 文档改进
- i18n: 翻译相关
- refactor: 代码重构
```

### PR 流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/my-feature`)
3. 提交更改 (`git commit -m 'feat: add new prompt template'`)
4. 推送到分支 (`git push origin feature/my-feature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 协议。提交贡献即表示你同意你的贡献也遵循 MIT 协议。

## 免责声明

本项目的提示词内容来源于 OpenAI 官方开发者文档，仅供学习和参考使用。
