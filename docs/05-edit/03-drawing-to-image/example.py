"""Official Python example adapted for repository-local Cookbook assets."""

import base64
from pathlib import Path

from openai import OpenAI


ASSET_ROOT = Path(__file__).resolve().parents[2] / "assets" / "official-cookbook"
OUTPUT_DIR = Path(__file__).resolve().parent / "output_images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
client = OpenAI()


def save_image(result, filename: str) -> None:
    """Save the first returned image next to this example."""
    image_bytes = base64.b64decode(result.data[0].b64_json)
    (OUTPUT_DIR / filename).write_bytes(image_bytes)

prompt = """
Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open(ASSET_ROOT / "drawings.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "realistic_valley_gpt-image-2.png")
