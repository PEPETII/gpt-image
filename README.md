# 🎨 GPT Image 官方提示词指南

> OpenAI 官方《GPT Image Generation Models Prompting Guide》完整中文翻译 + 可运行代码示例

[English](README_en.md) | MIT License

---

## 📖 项目简介

本项目是 OpenAI 官方《GPT Image Generation Models Prompting Guide》的开源整理项目，包含：

- 📝 **24 个官方提示词模板** — 中英双语，覆盖生成和编辑两大类
- 🐍 **可运行的 Python 代码** — 基于 OpenAI SDK，开箱即用
- 📋 **速查表** — 提示词模板、API 参数、最佳实践一页速查
- 📚 **详细文档** — 6 章完整指南，从入门到高级

## ✨ 案例预览

### 生成类 (text → image)

| 场景 | 效果 |
|------|------|
| 信息图表 | 咖啡机工作流程信息图 |
| 照片级写实 | 老水手在渔船上 |
| Logo 生成 | Field & Flour 面包店 Logo（4个候选） |
| 广告创意 | Thread 街头品牌广告 |
| 故事转漫画 | 宠物独处 4 格漫画 |
| UI 模型 | 农贸市场 App 界面 |
| 科学教育 | 细胞呼吸生物学图表 |
| 融资幻灯片 | Market Opportunity TAM/SAM/SOM |

### 编辑类 (text + image → image)

| 场景 | 效果 |
|------|------|
| 风格迁移 | 像素风参考 → 像素风摩托车 |
| 虚拟试穿 | 人物照片 + 服装 → 试穿效果 |
| 素描转图像 | 手绘草图 → 照片级渲染 |
| 物品移除 | 一句话移除手中花朵 |
| 营销创意 | 产品 → 高速公路广告牌（含文字） |
| 光照变换 | 日落广告牌 → 冬夜降雪版 |
| 室内替换 | 白色椅子 → 木质椅子 |
| 人物合成 | 人物 + 狗 → 同框合成 |

## 🚀 快速开始

### 安装

```bash
pip install openai
```

### 配置 API Key

```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

### 运行示例

```bash
# 生成类案例
python examples/generate_examples.py

# 编辑类案例（需要输入图像）
python examples/edit_examples.py

# 高级案例（含多步骤工作流）
python examples/advanced_examples.py
```

## 📁 项目结构

```
gpt-image-prompting-guide/
├── README.md                    # 项目主页
├── LICENSE                      # MIT 协议
├── prompts/                     # 提示词模板（中英双语）
│   ├── generate/                # 生成类（10个）
│   └── edit/                    # 编辑类（9个）
├── examples/                    # Python 代码示例
│   ├── generate_examples.py     # 生成类案例
│   ├── edit_examples.py         # 编辑类案例
│   └── advanced_examples.py     # 高级案例
├── docs/                        # 详细文档
│   ├── 01-introduction.md       # 引言与模型参数
│   ├── 02-prompting-fundamentals.md  # 提示词基本原理
│   ├── 03-setup.md              # 环境设置
│   ├── 04-generate-use-cases.md # 生成用例详解
│   ├── 05-edit-use-cases.md     # 编辑用例详解
│   └── 06-additional-use-cases.md  # 高级用例
└── cheat-sheet/                 # 速查表
    ├── prompt-cheatsheet.md     # 提示词速查
    ├── api-params-cheatsheet.md # API 参数速查
    └── best-practices.md        # 最佳实践
```

## 📊 API 参数速查

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| `model` | 模型选择 | `"gpt-image-2"` |
| `quality` | 输出质量 | `"medium"`（一般）/ `"high"`（精细文本） |
| `input_fidelity` | 输入保真度 | `"high"`（精细编辑） |
| `size` | 输出尺寸 | `"1024x1024"` / `"1024x1536"` / `"1536x1024"` |
| `n` | 变体数量 | `1`（默认）/ `4`（Logo等需要多候选） |
| `background` | 背景模式 | `"opaque"`（产品图） |

## 🤝 贡献

欢迎提交新的提示词模板、改进翻译或添加代码示例！请阅读 [贡献指南](CONTRIBUTING.md)。

## 📄 许可证

[MIT License](LICENSE)

## 🙏 致谢

- 所有提示词内容来源于 [OpenAI 官方开发者文档](https://platform.openai.com/docs/guides/image-generation)
- 本项目仅供学习和参考使用
