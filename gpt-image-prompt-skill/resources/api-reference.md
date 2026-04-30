# GPT Image 2 API Quick Reference

## Models

| Model | Description |
|-------|-------------|
| `gpt-image-2` | Latest, most capable model (recommended) |
| `gpt-image-1.5` | Previous generation |
| `gpt-image-1` | Legacy |
| `gpt-image-1-mini` | Fast, cost-effective for bulk |

## Parameters

### quality

| Value | Use Case |
|-------|----------|
| `"low"` | Speed-sensitive, bulk generation |
| `"medium"` | Default, balanced quality/speed |
| `"high"` | Fine text, infographics, portraits, identity-sensitive edits |

### input_fidelity

| Value | Use Case |
|-------|----------|
| `"low"` | Creative reinterpretation allowed |
| `"medium"` | Moderate preservation |
| `"high"` | Object removal, lighting changes, person editing, compositing |

### size

| Label | Resolution | Use Case |
|-------|-----------|----------|
| Square | `1024x1024` | Logos, icons, product shots |
| Portrait | `1024x1536` | People, mobile screens, comic strips |
| Landscape | `1536x1024` | Scenery, slides, charts, ads |
| Wide | `1536x864` | Panoramic, banners |
| 2K | `2560x1440` | High-res (experimental above this) |

**Rules:** Max edge < 3840px; both edges multiples of 16; aspect ratio ≤ 3:1; total pixels 655,360 ~ 8,294,400

### background

| Value | Use Case |
|-------|----------|
| `"opaque"` | Product extraction, logo generation |

### n

| Value | Use Case |
|-------|----------|
| `1` | Default |
| `4` | Logo generation, multiple candidates |

## API Call Patterns

### Generate (text → image)

```python
result = client.images.generate(
    model="gpt-image-2",
    prompt="...",
    size="1024x1024",
    quality="medium",
    n=1,
)
```

### Edit (text + image → image)

```python
result = client.images.edit(
    model="gpt-image-2",
    prompt="...",
    image=[{"type": "image_url", "image_url": {"url": "data:image/png;base64,..."}}],
    input_fidelity="high",
    size="1024x1536",
    quality="medium",
)
```

### Multi-Image Edit

```python
result = client.images.edit(
    model="gpt-image-2",
    prompt="...",
    image=[
        {"type": "image_url", "image_url": {"url": "data:image/png;base64,IMAGE_1"}},
        {"type": "image_url", "image_url": {"url": "data:image/png;base64,IMAGE_2"}},
    ],
    input_fidelity="high",
    size="1024x1536",
)
```

## Save Image

```python
import base64

image_bytes = base64.b64decode(result.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
```
