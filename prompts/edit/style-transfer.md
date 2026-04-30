# 风格迁移 | Style Transfer

> 章节：5.1 | 分类：编辑 (Edit)

---

## 提示词 / Prompt

```text
Use the same style from the input image and generate a man riding a motorcycle on a white background.
```

### 中文翻译

```
使用输入图像的相同风格，生成一个在白色背景上骑摩托车的男人。
```

---

## 关键技巧 / Key Tips

描述什么必须保持一致（风格线索），什么必须改变（新内容），添加硬约束（背景、构图、"不要添加额外元素"）防止偏移。使用 `client.images.edit()` API 传入参考图像。

## API 参数建议 / Recommended Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| size | 1024x1536 | 竖版构图，适合人物主体 |

## 适用场景 / Use Cases

艺术风格复用、品牌视觉统一、创意探索
