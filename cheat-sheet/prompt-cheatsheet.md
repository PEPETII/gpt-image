# Prompt 速查表

完整官方提示词位于 [docs/](../docs/README.md) 的 23 个用例目录。本表只保留选择路径和最小结构，避免形成第二套正文。

## 生成

| 场景 | 章节 | 首要写清 |
|---|---|---|
| 信息图 | [4.1](../docs/04-generate/01-infographics/) | 主题、受众、步骤、关系、标签和版式 |
| 图像文字翻译 | [4.2](../docs/04-generate/02-translation-in-images/) | 目标语言，以及“只改变文字” |
| 照片级写实 | [4.3](../docs/04-generate/03-photorealistic/) | 人物/主体、动作、材质、景别、光线和真实瑕疵 |
| 世界知识 | [4.4](../docs/04-generate/04-world-knowledge/) | 地点、日期、时代服装、建筑和工具 |
| Logo | [4.5](../docs/04-generate/05-logo-generation/) | 原创、轮廓、负空间、颜色和大小可读性 |
| 广告 | [4.6](../docs/04-generate/06-ads-generation/) | 品牌、受众、视觉钩子、版式和唯一精确文案 |
| 漫画 | [4.7](../docs/04-generate/07-story-to-comic/) | 面板数量、每格动作、角色一致性和叙事顺序 |
| UI | [4.8](../docs/04-generate/08-ui-mockups/) | 内容、导航、操作、排版和设备外框 |
| 科学/教育图 | [4.9](../docs/04-generate/09-scientific-educational/) | 标题、组件、箭头、精确标签和受众层级 |
| 幻灯片/图表 | [4.10](../docs/04-generate/10-slides-charts/) | 关键结论、数据、图表、脚注和可比较的层级 |

## 编辑

| 场景 | 章节 | 首要写清 |
|---|---|---|
| 风格迁移 | [5.1](../docs/05-edit/01-style-transfer/) | 参考图的媒介、线条、色彩和新主体 |
| 虚拟试穿 | [5.2](../docs/05-edit/02-virtual-try-on/) | 人物图、服装图，以及必须锁定的身份特征 |
| 草图转图像 | [5.3](../docs/05-edit/03-drawing-to-image/) | 需要保留的布局、比例、透视和主体位置 |
| 产品模型 | [5.4](../docs/05-edit/04-product-mockups/) | 产品几何、材质、颜色、标签和边缘 |
| 营销创意 | [5.5](../docs/05-edit/05-marketing-creatives/) | 产品、环境、光线、透视和精确文案 |
| 光照/天气 | [5.6](../docs/05-edit/06-lighting-weather/) | 唯一环境变化和所有保持项 |
| 物体移除 | [5.7](../docs/05-edit/07-object-removal/) | 对象位置、背景重建和“不要改变其他内容” |
| 人物插入 | [5.8](../docs/05-edit/08-insert-person-scene/) | 人物身份、目标场景、尺度、透视、光线和阴影 |
| 多图合成 | [5.9](../docs/05-edit/09-multi-image-compositing/) | 每张图角色、元素移动方向和目标位置 |

## 最小结构

```text
Create or edit [the target image].

Subject / Change:
[What the image should show or the only requested change]

Composition / Visual direction:
[Framing, viewpoint, materials, style, lighting, and color]

Preserve:
[Identity, geometry, pose, layout, labels, and unrelated elements]

Constraints:
[Exact text, exclusions, and no watermark or extra text]
```
