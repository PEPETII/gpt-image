# Prompt 章节索引

提示词正文已统一迁移到 `docs/` 的官方章节目录。本目录只保留导航，避免与章节 README 和 `prompt.md` 形成两套完整来源。

## 生成：4.1–4.10

| 章节 | 目录 |
|---|---|
| 4.1 Infographics | [docs/04-generate/01-infographics](../docs/04-generate/01-infographics/) |
| 4.2 Translation in Images | [docs/04-generate/02-translation-in-images](../docs/04-generate/02-translation-in-images/) |
| 4.3 Photorealistic Images | [docs/04-generate/03-photorealistic](../docs/04-generate/03-photorealistic/) |
| 4.4 World knowledge | [docs/04-generate/04-world-knowledge](../docs/04-generate/04-world-knowledge/) |
| 4.5 Logo Generation | [docs/04-generate/05-logo-generation](../docs/04-generate/05-logo-generation/) |
| 4.6 Ads Generation | [docs/04-generate/06-ads-generation](../docs/04-generate/06-ads-generation/) |
| 4.7 Story-to-Comic Strip | [docs/04-generate/07-story-to-comic](../docs/04-generate/07-story-to-comic/) |
| 4.8 UI Mockups | [docs/04-generate/08-ui-mockups](../docs/04-generate/08-ui-mockups/) |
| 4.9 Scientific / Educational Visuals | [docs/04-generate/09-scientific-educational](../docs/04-generate/09-scientific-educational/) |
| 4.10 Slides, Diagrams, Charts | [docs/04-generate/10-slides-charts](../docs/04-generate/10-slides-charts/) |

## 编辑：5.1–5.9

| 章节 | 目录 |
|---|---|
| 5.1 Style Transfer | [docs/05-edit/01-style-transfer](../docs/05-edit/01-style-transfer/) |
| 5.2 Virtual Clothing Try-On | [docs/05-edit/02-virtual-try-on](../docs/05-edit/02-virtual-try-on/) |
| 5.3 Drawing → Image | [docs/05-edit/03-drawing-to-image](../docs/05-edit/03-drawing-to-image/) |
| 5.4 Product Mockups | [docs/05-edit/04-product-mockups](../docs/05-edit/04-product-mockups/) |
| 5.5 Marketing Creatives | [docs/05-edit/05-marketing-creatives](../docs/05-edit/05-marketing-creatives/) |
| 5.6 Lighting and Weather | [docs/05-edit/06-lighting-weather](../docs/05-edit/06-lighting-weather/) |
| 5.7 Object Removal | [docs/05-edit/07-object-removal](../docs/05-edit/07-object-removal/) |
| 5.8 Insert the Person | [docs/05-edit/08-insert-person-scene](../docs/05-edit/08-insert-person-scene/) |
| 5.9 Multi-Image Compositing | [docs/05-edit/09-multi-image-compositing](../docs/05-edit/09-multi-image-compositing/) |

## 高级：6.1–6.4

| 章节 | 目录 |
|---|---|
| 6.1 Interior design swap | [docs/06-additional-use-cases/01-interior-design-swap](../docs/06-additional-use-cases/01-interior-design-swap/) |
| 6.2 3D pop-up holiday card | [docs/06-additional-use-cases/02-holiday-card](../docs/06-additional-use-cases/02-holiday-card/) |
| 6.3 Collectible Action Figure | [docs/06-additional-use-cases/03-collectible-figure](../docs/06-additional-use-cases/03-collectible-figure/) |
| 6.4 Children’s Book Art | [docs/06-additional-use-cases/04-childrens-book-art](../docs/06-additional-use-cases/04-childrens-book-art/) |

## 使用边界

- 网页端复制场景使用 `gpt-image-prompt-web`，输出英文 prompt、中文翻译和关键假设；
- API、Python、SDK、`images.generate` 或 `images.edit` 场景使用 `gpt-image-prompt-api`；
- API skill 只覆盖 `gpt-image-2` Image API，不覆盖 Responses API；
- 官方图片来源和角色见 [`docs/assets/official-cookbook/manifest.json`](../docs/assets/official-cookbook/manifest.json)。
