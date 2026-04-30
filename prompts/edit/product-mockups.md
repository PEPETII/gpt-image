# 产品模型 | Product Mockups

> 章节：5.4 | 分类：编辑 (Edit)

---

## 提示词 / Prompt

```text
Extract the product from the input image and place it on a plain white opaque background. Output: centered product, crisp silhouette, no halos/fringing. Preserve product geometry and label legibility exactly. Add only light polishing and a subtle realistic contact shadow. Do not restyle the product; only remove background and lightly polish.
```

### 中文翻译

```
从输入图像中提取产品，放置在纯白色不透明背景上。输出：居中的产品，清晰的轮廓，无光晕/边缘效应。精确保持产品几何形状和标签可读性。仅添加轻度润色和微妙的真实接触阴影。不要重新设计产品外观；只移除背景并轻度修整。
```

---

## 关键技巧 / Key Tips

使用 `background="opaque"` 参数；要求仅做轻度润色和微妙的真实接触阴影；不要重新设计产品外观。如需透明资产可在下游使用背景移除步骤。

## API 参数建议 / Recommended Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| background | opaque | 不透明白色背景 |
| input_fidelity | high | 高保真度，精确保持产品几何形状和标签 |
| size | 1024x1024 | 正方形构图，适合产品展示 |

## 适用场景 / Use Cases

电商产品图、目录制作、设计系统素材
