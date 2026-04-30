# 提示词模板 | Prompt Templates

> 本目录包含 OpenAI 官方《GPT Image Generation Models Prompting Guide》中的全部提示词模板，中英双语。

## 目录结构

### 生成类 (Generate: text → image)

| 文件 | 章节 | 说明 |
|------|------|------|
| [infographic.md](generate/infographic.md) | 4.1 | 信息图表生成 |
| [translation.md](generate/translation.md) | 4.2 | 图片中的文字翻译 |
| [photorealistic.md](generate/photorealistic.md) | 4.3 | 照片级写实图像 |
| [world-knowledge.md](generate/world-knowledge.md) | 4.4 | 利用世界知识生成场景 |
| [logo-generation.md](generate/logo-generation.md) | 4.5 | Logo 生成 |
| [ads-generation.md](generate/ads-generation.md) | 4.6 | 广告创意生成 |
| [comic-strip.md](generate/comic-strip.md) | 4.7 | 故事转漫画条 |
| [ui-mockups.md](generate/ui-mockups.md) | 4.8 | 用户界面模型 |
| [scientific-educational.md](generate/scientific-educational.md) | 4.9 | 科学/教育视觉材料 |
| [slides-charts.md](generate/slides-charts.md) | 4.10 | 幻灯片、图表和生产力图像 |

### 编辑类 (Edit: text + image → image)

| 文件 | 章节 | 说明 |
|------|------|------|
| [style-transfer.md](edit/style-transfer.md) | 5.1 | 风格迁移 |
| [virtual-try-on.md](edit/virtual-try-on.md) | 5.2 | 虚拟服装试穿 |
| [drawing-to-image.md](edit/drawing-to-image.md) | 5.3 | 素描转图像渲染 |
| [product-mockups.md](edit/product-mockups.md) | 5.4 | 产品模型（干净背景） |
| [marketing-creatives.md](edit/marketing-creatives.md) | 5.5 | 带真实文字的营销创意 |
| [lighting-weather.md](edit/lighting-weather.md) | 5.6 | 光照和天气变换 |
| [object-removal.md](edit/object-removal.md) | 5.7 | 物品移除 |
| [insert-person-scene.md](edit/insert-person-scene.md) | 5.8 | 人物插入场景 |
| [multi-image-compositing.md](edit/multi-image-compositing.md) | 5.9 | 多图引用与合成 |

## 使用方式

1. 选择你需要的场景对应的 `.md` 文件
2. 复制英文提示词原文到你的 API 调用或 ChatGPT 对话中
3. 根据你的需求修改提示词中的具体内容（品牌名、产品描述等）
4. 参考"API 参数建议"设置合适的参数

## 注意事项

- **建议使用英文提示词**：模型对英文的理解和执行效果通常更好
- **中文翻译仅供参考**：帮助你理解提示词的含义和结构
- **所有提示词来源**：OpenAI 官方开发者文档
