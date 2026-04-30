# Logo生成 | Logo Generation

> 章节：4.5 | 分类：生成 (Generate)

---

## 提示词 / Prompt

```text
Create an original, non-infringing logo for a company called Field & Flour, a local bakery. The logo should feel warm, simple, and timeless. Use clean, vector-like shapes, a strong silhouette, and balanced negative space. Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential. Plain background. Deliver a single centered logo with generous padding. No watermark.
```

### 中文翻译

```
为一家名为Field & Flour的本地面包店创建一个原创、不侵权的Logo。Logo应该感觉温暖、简洁、经典。使用干净的矢量风格形状、强烈的轮廓和平衡的留白。简洁优于细节，确保在小尺寸和大尺寸下都清晰可读。扁平设计，极简线条，除非必要不使用渐变。纯色背景。输出一个居中的Logo，留有充足的边距。无水印。
```

---

## 关键技巧 / Key Tips

强调"原创、不侵权"；描述设计风格而非具体图形；要求"扁平设计、矢量风格"；使用 `n=4` 生成多个候选方案。

## API 参数建议 / Recommended Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| n | 4 | 生成多个候选方案，便于比较和选择 |
| size | "1024x1024" | 正方形尺寸，适合Logo的标准比例 |
| background | "opaque" | 不透明背景，确保Logo在纯色背景上展示 |

## 适用场景 / Use Cases

品牌Logo设计、图标设计、视觉识别系统
