"""Official Cookbook editing examples for sections 5.1-5.9."""

import base64
from contextlib import ExitStack
from pathlib import Path

from openai import OpenAI


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "docs" / "assets" / "official-cookbook"
OUTPUT_DIR = ROOT / "output_images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
client = OpenAI()


def edit_assets(prompt: str, filenames: list[str], output_name: str, size: str = "1024x1536", quality: str = "medium", background: str | None = None) -> None:
    with ExitStack() as stack:
        images = [stack.enter_context((ASSET_DIR / filename).open("rb")) for filename in filenames]
        kwargs = {
            "model": "gpt-image-2",
            "image": images,
            "prompt": prompt,
            "size": size,
            "quality": quality,
        }
        if background is not None:
            kwargs["background"] = background
        result = client.images.edit(**kwargs)
    output = OUTPUT_DIR / output_name
    output.write_bytes(base64.b64decode(result.data[0].b64_json))
    print(f"saved {output}")


def example_style_transfer() -> None:
    edit_assets(
        "Use the same style from the input image and generate a man riding a motorcycle on a white background.",
        ["pixels.png"],
        "motorcycle_gpt-image-2.png",
    )


def example_virtual_try_on() -> None:
    prompt = """Edit the image to dress the woman using the provided clothing images. Do not change her face, facial features, skin tone, body shape, pose, or identity in any way. Preserve her exact likeness, expression, hairstyle, and proportions. Replace only the clothing, fitting the garments naturally to her existing pose and body geometry with realistic fabric behavior. Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on. Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks."""
    edit_assets(prompt, ["woman_in_museum.png", "tank_top.png", "jacket.png", "boots.png"], "outfit_gpt-image-2.png")


def example_drawing_to_image() -> None:
    prompt = """Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text."""
    edit_assets(prompt, ["drawings.png"], "realistic_valley_gpt-image-2.png")


def example_product_mockup() -> None:
    prompt = """Extract the product from the input image and place it on a plain white opaque background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing and a subtle realistic contact shadow.
Do not restyle the product; only remove background and lightly polish."""
    edit_assets(prompt, ["shampoo.png"], "extract_product_gpt-image-2.png", background="opaque")


def example_marketing_creative() -> None:
    prompt = """Create a realistic billboard mockup of the shampoo on a highway scene during sunset.
Billboard text (EXACT, verbatim, no extra characters):
"Fresh and clean"
Typography: bold sans-serif, high contrast, centered, clean kerning.
Ensure text appears once and is perfectly legible.
No watermarks, no logos."""
    edit_assets(prompt, ["shampoo.png"], "billboard_gpt-image-2.png")


def example_lighting_weather() -> None:
    edit_assets(
        "Make it look like a winter evening with snowfall.",
        ["billboard_gpt-image-2.png"],
        "billboard_winter_gpt-image-2.png",
    )


def example_object_removal() -> None:
    edit_assets(
        "Remove the flower from man's hand. Do not change anything else.",
        ["man_with_blue_hat.png"],
        "man_with_no_flower_gpt-image-2.png",
    )


def example_insert_person() -> None:
    prompt = """Generate a highly realistic action scene where this person is running away from a large, realistic brown bear attacking a campsite. The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
She is centered in the image but looking away from the camera, wearing outdoorsy camping attire, with dirt on her face and tears in her clothing. She is clearly afraid but focused on escaping, running away from the bear as it destroys the campsite behind her.
The campsite is in Yosemite National Park, with believable natural details. The time of day is dusk, with natural lighting and realistic colors. Everything should feel grounded, authentic, and unstyled, as if captured in a real moment. Avoid cinematic lighting, dramatic color grading, or stylized composition."""
    edit_assets(prompt, ["woman_in_museum.png"], "scene_gpt-image-2.png")


def example_multi_image_compositing() -> None:
    prompt = "Place the dog from the second image into the setting of image 1, right next to the woman, use the same style of lighting, composition and background. Do not change anything else."
    edit_assets(prompt, ["test_woman.png", "test_woman_2.png"], "test_woman_with_dog_gpt-image-2.png")


if __name__ == "__main__":
    for function in [
        example_style_transfer,
        example_virtual_try_on,
        example_drawing_to_image,
        example_product_mockup,
        example_marketing_creative,
        example_lighting_weather,
        example_object_removal,
        example_insert_person,
        example_multi_image_compositing,
    ]:
        function()
