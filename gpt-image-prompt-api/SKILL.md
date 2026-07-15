---
name: gpt-image-prompt-api
description: >-
  为 gpt-image-2 Image API 编写图像生成与编辑提示词，推荐当前参数并输出完整 Python 示例。
  Use when the user mentions OpenAI image API, API, Python, SDK, code, images.generate, images.edit, or API request parameters.
---

# GPT Image API Prompt

## Scope

为当前 `gpt-image-2` Image API 生成提示词、参数建议和 Python 调用示例。本 skill 是独立包，只使用同目录下的 `resources/api-reference.md` 和 `resources/prompt-templates.md`，不要求读取仓库文件或访问网站。

只覆盖 Image API 的 `images.generate` 和 `images.edit`。不覆盖 Responses API，不执行真实请求，不索取、写入或打印 API Key。

## Workflow

### 1. 识别模式

- 出现 API、Python、SDK、代码、接口、`images.generate` 或 `images.edit` 时使用本 skill。
- 没有输入图片时使用 `images.generate`。
- 有输入图片、参考图、编辑目标、移除、替换、换装或合成需求时使用 `images.edit`。
- 多张图片时给每张输入定义稳定编号、角色和顺序。
- 用户只说“帮我写图片提示词”且没有接口语境时，由网页版 skill 处理。
- 用户提到网页、ChatGPT、复制或粘贴时交给网页版 skill；不要把 Python 或参数表混入网页版结果。
- 用户明确要求两个版本时，分别输出两个独立契约的结果。

### 2. 提取需求

提取并保留：

- 生成或编辑模式；
- 主体、场景、动作、身份、几何、材质和视觉目标；
- 构图、视角、景别、光线、颜色、背景和用途；
- 图片内精确文字、语言、大小写、出现次数和排版；
- 每张输入图片的本地路径、格式、角色和目标关系；
- 必须保持、必须改变和禁止额外改变的内容；
- 用户明确要求的尺寸、质量、背景、格式、压缩和结果数量。

只询问会改变操作类型、输入顺序、编辑范围、身份/几何保护或精确文字的缺口。其余细节使用合理默认值，并在中文说明中标出。

### 3. 选择本地方法

按任务读取 `resources/prompt-templates.md` 中的场景小节，再读取 `resources/api-reference.md` 选择字段。资源已经包含生成、编辑、多图和高级工作流，不需要其他目录。

- 信息图、科学图、幻灯片和 UI：优先锁定内容层级、数据、标签、可读性和页面结构。
- 写实、历史和广告：优先描述真实材质、光线、受众、构图和文字。
- Logo：强调原创、轮廓、负空间、小尺寸可读性和无额外标识。
- 编辑：先写唯一变化，再写 `Change`、`Preserve`、`Do not change` 三组语义。
- 多图编辑：在 prompt 中使用 `Image 1`、`Image 2` 等编号，并让代码列表保持完全相同的顺序。
- 角色连续性：将第一张参考图作为角色锚点，重复外观、比例、服装和性格清单。

### 4. 编写英文 prompt

按以下顺序组织：

1. 最终图像目标和用途；
2. 主体、动作、环境和关键细节；
3. 构图、视角、光线、颜色、材质和风格；
4. 图片文字，使用引号并注明 `EXACT, verbatim`、出现次数和可读性；
5. 编辑保护、输入图角色和禁止额外变化。

API 参数只放在“推荐参数”和 Python 调用中，不放入 prompt 代码块。提示词使用模型可执行的自然语言，不编写伪 JSON 或内部说明。

### 5. 选择参数

读取 `resources/api-reference.md` 并遵循以下固定边界：

- `model` 固定为 `gpt-image-2`。
- 无输入图使用 `client.images.generate`；有输入图使用 `client.images.edit`。
- 未指定时使用 `size="auto"`、`quality="medium"`、`n=1`、`background="auto"`，输出默认 PNG。
- 用户明确需要特定尺寸时，只使用契约允许的尺寸；不要从旧示例猜测限制。
- 只有用户需要 JPEG 或 WebP 时才设置 `output_format` 和 `output_compression`。
- 只有局部遮罩编辑确实需要时才传 `mask`，并确认遮罩与输入图尺寸匹配且包含 alpha 通道。
- 不推荐透明背景；当前契约只使用 `auto` 或 `opaque`。

### 6. 编写 Python 示例

代码必须包含必要的 import、`OpenAI()` 初始化、请求调用、Base64 解码和文件保存。默认从环境读取凭证，不在示例中硬编码密钥。编辑示例要打开真实输入路径；多图示例用 `ExitStack` 管理文件句柄，并在 prompt 中按代码顺序标注角色。

不要调用真实 API。验证只做语法解析、字符串和请求形状检查。

### 7. 返回结果

严格使用以下结构：

````markdown
## API Prompt

```text
[适用于 gpt-image-2 的英文 prompt]
```

## 推荐参数

| 参数 | 值 | 说明 |
|---|---|---|

## Python 示例

```python
[完整的 images.generate 或 images.edit 示例]
```

## 中文说明

[提示词、参数、输入图角色、保存路径和关键假设说明]
````

推荐参数表只列本次请求需要的字段。中文说明必须解释操作类型、每张输入图的角色、默认值和用户需要替换的路径；不要声称精确文字、身份一致性或一次生成必然成功。

## Quality rules

- 只使用 `gpt-image-2`，不写其他模型调用。
- 只覆盖 `images.generate` 和 `images.edit`，不输出 Responses API 代码。
- 不把参数表塞进英文 prompt。
- 多图代码顺序、prompt 编号和中文角色说明必须一致。
- 编辑提示词必须明确唯一变化和保持项。
- Python 示例必须有完整请求和结果保存逻辑，不能只给伪代码。
- 不执行 API 请求，不索取或打印用户密钥。

## Bundled resources

- [resources/api-reference.md](resources/api-reference.md)：本包内置的模型、参数、尺寸、输入图和代码契约。
- [resources/prompt-templates.md](resources/prompt-templates.md)：4.1–4.10、5.1–5.9、6.1–6.4 的场景方法和英文 prompt 模板。
