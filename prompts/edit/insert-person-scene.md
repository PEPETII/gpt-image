# 人物插入场景 | Insert Person into Scene

> 章节：5.8 | 分类：编辑 (Edit)

---

## 提示词 / Prompt

```text
Generate a highly realistic action scene where this person is running away from a large, realistic brown bear attacking a campsite. The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
She is centered in the image but looking away from the camera, wearing outdoorsy camping attire, with dirt on her face and tears in her clothing. She is clearly afraid but focused on escaping, running away from the bear as it destroys the campsite behind her.
The campsite is in Yosemite National Park, with believable natural details. The time of day is dusk, with natural lighting and realistic colors. Everything should feel grounded, authentic, and unstyled, as if captured in a real moment. Avoid cinematic lighting, dramatic color grading, or stylized composition.
```

### 中文翻译

```
生成一个高度逼真的动作场景，这个人正在逃离一只正在攻击营地的大型棕色熊。图像应该看起来像一张真实照片，而不是过度增强的电影海报。
她位于图像中央但背对相机，穿着户外露营服装，脸上有泥土，衣服有破损。她明显害怕但专注于逃跑，逃离正在破坏身后营地的熊。
营地在优胜美地国家公园，具有可信的自然细节。时间是黄昏，自然光线和真实色彩。一切应该感觉接地气、真实、不做作，仿佛捕捉了一个真实的瞬间。避免电影化光照、戏剧性调色或风格化构图。
```

---

## 关键技巧 / Key Tips

通过指定接地气的摄影外观（自然光照、可信细节、无电影调色）来锚定真实感；锁定关于主体不应改变的内容；明确避免电影化光照和风格化构图。使用 `input_fidelity="high"` 有助于在较大场景编辑中保持相似度。

## API 参数建议 / Recommended Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| input_fidelity | high | 高保真度，保持人物相似度 |
| quality | high | 高质量输出，确保照片级真实感 |
| size | 1536x1024 | 横版构图，适合动作场景展示 |

## 适用场景 / Use Cases

故事板、活动营销、创意合成
