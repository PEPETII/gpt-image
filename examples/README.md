# Python 汇总示例

这些脚本把官方 Cookbook 的 23 个用例按生成、编辑和高级工作流汇总到一起。每个章节目录中的 `example.py` 才是逐例官方示例；本目录脚本用于集中浏览和运行。

## 使用

```bash
pip install -r requirements.txt
```

设置 `OPENAI_API_KEY` 后运行单个脚本或其中的函数：

```bash
python generate_examples.py
python edit_examples.py
python advanced_examples.py
```

编辑示例默认读取 `docs/assets/official-cookbook/` 中的官方输入图片，生成结果写入根目录 `output_images/`。真实运行会调用 Image API 并消耗额度；静态验证不会执行这些函数。

## 文件

| 文件 | 覆盖范围 |
|---|---|
| `generate_examples.py` | 4.1–4.10，包含 4.2 图片翻译编辑调用 |
| `edit_examples.py` | 5.1–5.9，多图输入按官方顺序传递 |
| `advanced_examples.py` | 6.1–6.4，包含角色锚点两步工作流 |

所有调用固定使用 `gpt-image-2`，不传 `input_fidelity`，也不覆盖 Responses API。原始提示词和官方图片来源请回到 [docs/](../docs/README.md)。
