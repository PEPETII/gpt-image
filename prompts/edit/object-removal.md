# 物品移除 | Object Removal

> 章节：5.7 | 分类：编辑 (Edit)

---

## 提示词 / Prompt

```text
Remove the flower from man's hand. Do not change anything else.
```

### 中文翻译

```
移除男人手中的花。不要改变其他任何东西。
```

---

## 关键技巧 / Key Tips

提示词应简洁直接地说明要移除什么；使用 `input_fidelity="high"` 参数；明确说"Do not change anything else"以保护图像其余部分。

## API 参数建议 / Recommended Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| input_fidelity | high | 高保真度，保护图像其余部分不被改变 |
| size | 1024x1536 | 竖版构图，适合人物主体 |

## 适用场景 / Use Cases

照片修图、电商图片清理、房产照片优化
