# GPT Image Official Prompting Guide

> Chinese translation, official examples, and a local asset index based on OpenAI Cookbook's GPT Image Generation Models Prompting Guide.

[中文](README.md) | [Official Cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) | MIT License

This repository supports an IDE-first workflow for image prompting. Use `gpt-image-prompt-web` to turn a natural-language request into an English prompt that can be copied into ChatGPT, or use `gpt-image-prompt-api` for a `gpt-image-2` Image API prompt, parameters, and Python example.

## Scope

- Six official chapters with the English source content and Chinese translation;
- 23 official use cases: 4.1–4.10 Generate, 5.1–5.9 Edit, and 6.1–6.4 Additional workflows;
- 37 unique image assets shown on the official page, stored in `docs/assets/official-cookbook/` without recompression;
- `README.md`, `prompt.md`, Python code, and local image role indexes for every use-case directory;
- `manifest.json` with each asset's official URL, local path, chapter, input/output role, retrieval time, and SHA-256.

## Documentation

| Chapter | Contents |
|---|---|
| [Chapter 1](docs/01-introduction/README.md) | Introduction, `gpt-image-2` capabilities, size constraints, and migration context |
| [Chapter 2](docs/02-prompting-fundamentals/README.md) | Prompt structure, constraints, text, people, multi-image references, and iteration |
| [Chapter 3](docs/03-setup/README.md) | Cookbook Python setup and image-saving helper |
| [Chapter 4](docs/04-generate/README.md) | Ten text-to-image generation use cases |
| [Chapter 5](docs/05-edit/README.md) | Nine text-plus-image editing use cases |
| [Chapter 6](docs/06-additional-use-cases/README.md) | Four additional workflows and multi-step examples |

Use [prompts/README.md](prompts/README.md) as the prompt index, [cheat-sheet/](cheat-sheet/README.md) for compact references, and [examples/](examples/README.md) for consolidated Python examples.

## API boundary

API examples in this repository use only the current `gpt-image-2` Image API endpoints `images.generate` and `images.edit`. Responses API is out of scope. `gpt-image-2` processes image inputs at high fidelity automatically, so the examples and recommendations do not use `input_fidelity`. Follow the [official Image generation guide](https://developers.openai.com/api/docs/guides/image-generation) for current size, quality, background, output-format, and compression rules.

## Image asset license

The image files were downloaded from the OpenAI Cookbook page for documentation and reproducibility. The repository MIT license does not automatically cover OpenAI image assets. See [`docs/assets/official-cookbook/manifest.json`](docs/assets/official-cookbook/manifest.json) for source URLs and hashes.

## Quick start

```bash
pip install openai
```

Set `OPENAI_API_KEY`, then follow [Chapter 3](docs/03-setup/README.md) and [examples/README.md](examples/README.md). Running real API examples consumes quota; this documentation rebuild did not call the image API.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). New material should live in the relevant `docs/` chapter directory rather than creating a second independent prompt corpus.
