# 🎨 GPT Image Official Prompting Guide

> Complete Chinese translation + runnable code examples for OpenAI's official GPT Image Generation Models Prompting Guide

[中文](README.md) | MIT License

---

## 📖 About

This is an open-source整理 project of OpenAI's official "GPT Image Generation Models Prompting Guide", featuring:

- 📝 **24 official prompt templates** — bilingual (EN/CN), covering both generate and edit modes
- 🐍 **Runnable Python code** — based on OpenAI SDK, ready to use
- 📋 **Cheat sheets** — prompt templates, API params, best practices at a glance
- 📚 **Detailed docs** — 6-chapter complete guide, from beginner to advanced

## ✨ Use Cases

### Generate (text → image)

Infographics | Photorealistic Images | Logo Generation | Ads | Comic Strips | UI Mockups | Scientific Diagrams | Pitch Decks

### Edit (text + image → image)

Style Transfer | Virtual Try-On | Drawing→Image | Product Mockups | Marketing Creatives | Lighting/Weather | Object Removal | Person Insertion | Multi-Image Compositing

## 🚀 Quick Start

```bash
pip install openai
export OPENAI_API_KEY="sk-your-api-key-here"

# Generate examples
python examples/generate_examples.py

# Edit examples (requires input images)
python examples/edit_examples.py

# Advanced examples (multi-step workflows)
python examples/advanced_examples.py
```

## 📁 Structure

```
gpt-image-prompting-guide/
├── prompts/          # Prompt templates (bilingual)
│   ├── generate/     # Generate prompts (10)
│   └── edit/         # Edit prompts (9)
├── examples/         # Python code examples
├── docs/             # Detailed documentation
└── cheat-sheet/      # Cheat sheets
```

## 📊 API Parameters

| Param | Description | Recommended |
|-------|-------------|-------------|
| `model` | Model selection | `"gpt-image-2"` |
| `quality` | Output quality | `"medium"` / `"high"` |
| `input_fidelity` | Input fidelity | `"high"` for precision edits |
| `size` | Output size | `"1024x1024"` / `"1024x1536"` / `"1536x1024"` |
| `n` | Variants count | `1` / `4` for logos |
| `background` | Background mode | `"opaque"` for products |

## 🤝 Contributing

PRs welcome! See [Contributing Guide](CONTRIBUTING.md).

## 📄 License

[MIT License](LICENSE)

## 🙏 Credits

- All prompt content sourced from [OpenAI Official Developer Documentation](https://platform.openai.com/docs/guides/image-generation)
- This project is for educational and reference purposes only
