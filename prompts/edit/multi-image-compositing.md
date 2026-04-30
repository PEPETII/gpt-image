# 多图合成 | Multi-Image Compositing

> 章节：5.9 | 分类：编辑 (Edit)

---

## 提示词 / Prompt

```text
Place the dog from the second image into the setting of image 1, right next to the woman, use the same style of lighting, composition and background. Do not change anything else.
```

### 中文翻译

```
将第二张图像中的狗放入图像1的场景中，紧挨着女人旁边，使用相同风格的光照、构图和背景。不要改变其他任何东西。
```

---

## 关键技巧 / Key Tips

清楚指定要移植什么（如"第二张图像中的狗"）、放在哪里（如"图像1中女人旁边"）、什么必须保持不变（场景、背景、构图）；同时匹配光照、透视、比例和阴影。使用 `input_fidelity="high"`。

## API 参数建议 / Recommended Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| input_fidelity | high | 高保真度，保持场景和背景不被改变 |
| size | 1024x1536 | 竖版构图，适合人物与动物主体 |

## 适用场景 / Use Cases

创意合成、产品场景替换、广告素材制作
