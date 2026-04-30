# 提示词最佳实践清单 | Best Practices Checklist

GPT Image 2 提示词编写的最佳实践，按类别组织。

---

## 1. 提示词结构 (Prompt Structure)

- [ ] 遵循结构化顺序：**背景 (Context) → 主体 (Subject) → 细节 (Details) → 约束 (Constraints)**
- [ ] 使用分节格式组织长提示词，用换行或分号分隔不同部分
- [ ] 将最重要的内容放在提示词开头，模型对开头部分更敏感
- [ ] 每个段落聚焦一个方面，避免信息混杂

**示例结构：**
```
[背景/场景设定]
[主体描述]
[细节补充：光线、视角、氛围]
[约束条件：不要什么、避免什么]
```

---

## 2. 约束条件 (Constraints)

- [ ] **始终列出"不要什么"**：明确排除不想要的元素，如 "Avoid tiny text"、"No gradients"、"Do not add new elements"
- [ ] **每次迭代重申约束**：在多轮对话中，关键约束需要在每次请求中重复
- [ ] 使用否定指令时要具体，避免模糊表述（用 "No 3D effects" 而非 "Make it simple"）
- [ ] 对编辑模式，明确区分"要改变的部分"和"不要改变的部分"

---

## 3. 文字渲染 (Text Rendering)

- [ ] **用引号括起需要渲染的文字**：`Text (EXACT): "Your Tagline Here"`
- [ ] 使用 `EXACT` 或 `verbatim` 关键词强调文字准确性
- [ ] **指定字体风格**：如 "Use a clean sans-serif font"、"Bold headline in serif font"
- [ ] **指定文字位置**：如 "Title at the top center"、"Caption at the bottom"
- [ ] 避免在同一图像中放置过多文字，优先保持可读性
- [ ] 包含文字的图像务必使用 `quality="high"`

---

## 4. 身份保持 (Identity Preservation)

- [ ] **锁定关键特征**：明确列出需要保持的面部 (face)、体型 (body type)、姿势 (pose)、发型 (hairstyle)
- [ ] 使用 `input_fidelity="high"` 最大化保留原图人物特征
- [ ] 在提示词中明确写出 "Preserve the person's exact face and appearance"
- [ ] 对编辑模式，使用 "Do not change [特征列表]" 锁定不变元素
- [ ] 人物插入场景时，详细描述人物在新场景中的动作和位置

---

## 5. 质量控制 (Quality Control)

- [ ] **包含小文本时**：使用 `quality="high"`，这是最关键的规则
- [ ] **一般场景**：使用 `quality="medium"`（默认值），在质量和速度间取得平衡
- [ ] **快速草稿/预览**：使用 `quality="low"` 进行快速迭代
- [ ] 信息图表、科学图表、UI 模型、幻灯片等场景必须使用 `quality="high"`
- [ ] 大尺寸图像建议配合 `quality="high"` 以确保细节清晰

---

## 6. 构图描述 (Composition)

- [ ] **指定视角**：如 "Eye-level shot"、"Bird's-eye view"、"Low angle"、"Close-up"
- [ ] **描述光线**：如 "Golden hour lighting"、"Studio lighting with soft shadows"、"Dramatic side lighting"
- [ ] **设定氛围**：如 "Warm and inviting atmosphere"、"Professional and clean"、"Whimsical and playful"
- [ ] 提及构图参考：如 "Rule of thirds"、"Centered composition"、"Symmetrical layout"
- [ ] 描述景深：如 "Shallow depth of field with bokeh background"

---

## 7. 迭代优化 (Iterative Refinement)

- [ ] **小幅调整优于大幅重写**：每次只修改 1-2 个方面，观察效果变化
- [ ] 保留有效的提示词部分，只替换需要改进的段落
- [ ] 记录每次迭代的变化和效果，建立有效的提示词模式
- [ ] 使用 `n=4` 生成多个候选方案，从中选择最佳方向
- [ ] 遇到不满意的结果时，先分析是哪个部分导致了问题，再针对性修改

---

## 8. 编辑模式 (Edit Mode)

- [ ] **清楚区分变与不变**：用 "Change ONLY [X]" 和 "Preserve [Y]" 明确边界
- [ ] **使用高保真模式**：局部修改时使用 `input_fidelity="high"`
- [ ] 物品移除时补充 "Do not change anything else" 防止意外修改
- [ ] 多图编辑时，明确说明每张输入图像的用途
- [ ] 编辑提示词应聚焦于"差异"而非重新描述整张图像

---

## 9. 多图工作流 (Multi-Image Workflow)

- [ ] **两步法保持角色一致性**：
  1. Step 1: 使用 Generate 模式创建角色锚点图（character anchor）
  2. Step 2: 使用 Edit 模式传入角色图，在提示词中引用角色特征
- [ ] 儿童绘本、漫画连续场景等需要角色一致性的场景适用此方法
- [ ] 在编辑步骤中使用 `input_fidelity="high"` 保持角色外观一致
- [ ] 每次编辑都传入同一张角色锚点图作为参考

---

## 10. 版权安全 (Copyright Safety)

- [ ] **强调原创性**：在提示词中加入 "Original design only"、"No trademarks"、"Non-infringing"
- [ ] Logo 设计时明确 "Create an original logo, do not copy any existing brand"
- [ ] 避免在提示词中直接引用受版权保护的角色名、品牌名或商标
- [ ] 使用描述性语言替代品牌名称（如用 "a popular cola brand" 而非品牌名）
- [ ] 生成商业用途图像时，确保提示词不包含可能侵权的元素
