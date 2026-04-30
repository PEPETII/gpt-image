# 图片翻译 | Image Translation

> 章节：4.2 | 分类：生成 (Generate)

---

## 提示词 / Prompt

```text
Translate the text in the infographic to Spanish. Do not change any other aspect of the image.
```

### 中文翻译

```
将信息图中的文字翻译为西班牙语。不要改变图像的任何其他方面。
```

---

## 关键技巧 / Key Tips

明确指定目标语言，加约束"不要改变其他任何东西"防止模型过度修改。

## API 参数建议 / Recommended Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| input_fidelity | "high" | 高保真模式，最大程度保留原图内容，仅修改文字 |

## 适用场景 / Use Cases

多语言本地化、国际化内容制作
