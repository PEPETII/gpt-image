"""Official Cookbook generation examples for sections 4.1-4.10."""

import base64
from pathlib import Path

from openai import OpenAI


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "docs" / "assets" / "official-cookbook"
OUTPUT_DIR = ROOT / "output_images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
client = OpenAI()


def save_images(result, stem: str) -> None:
    for index, item in enumerate(result.data, start=1):
        suffix = f"_{index}" if len(result.data) > 1 else ""
        path = OUTPUT_DIR / f"{stem}{suffix}.png"
        path.write_bytes(base64.b64decode(item.b64_json))
        print(f"saved {path}")


def example_infographic() -> None:
    prompt = """Create a detailed Infographic of the functioning and flow of an automatic coffee machine like a Jura.
From bean basket, to grinding, to scale, water tank, boiler, etc.
I'd like to understand technically and visually the flow."""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1024x1536", quality="medium")
    save_images(result, "infographic_coffee_machine")


def example_translation() -> None:
    prompt = "Translate the text in the infographic to Spanish. Do not change any other aspect of the image."
    with (ASSET_DIR / "infographic_coffee_machine_gpt-image-2.png").open("rb") as image:
        result = client.images.edit(
            model="gpt-image-2",
            image=[image],
            prompt=prompt,
            size="1024x1536",
            quality="medium",
        )
    save_images(result, "infographic_coffee_machine_sp")


def example_photorealistic() -> None:
    prompt = """Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.
He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.
He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching."""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1024x1536", quality="medium")
    save_images(result, "photorealism")


def example_world_knowledge() -> None:
    prompt = """Create a realistic outdoor crowd scene in Bethel, New York on August 16, 1969.
Photorealistic, period-accurate clothing, staging, and environment."""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1024x1536", quality="medium")
    save_images(result, "world_knowledge")


def example_logo_generation() -> None:
    prompt = """Create an original, non-infringing logo for a company called Field & Flour, a local bakery.
The logo should feel warm, simple, and timeless. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential.
Plain background. Deliver a single centered logo with generous padding. No watermark."""
    result = client.images.generate(
        model="gpt-image-2",
        prompt=prompt,
        size="1024x1536",
        quality="medium",
        n=4,
    )
    save_images(result, "logo_generation")


def example_ads_generation() -> None:
    prompt = """Give me a cool in culture ad / fashion shot for a brand called Thread.
It's a hip young street brand. The ad shows a group of friends hanging out together with the tagline "Yours to Create."
Make it feel like a polished campaign image for a youth streetwear audience: stylish, contemporary, energetic, and tasteful.
Use clean composition, strong color direction, natural poses, and premium fashion photography cues.
Render the tagline exactly once, clearly and legibly, integrated into the ad layout.
No extra text, no watermarks, no unrelated logos."""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1024x1536", quality="medium")
    save_images(result, "thread_ad")


def example_comic_strip() -> None:
    prompt = """Create a short vertical comic-style reel with 4 equal-sized panels.
Panel 1: The owner leaves through the front door. The pet is framed in the window behind them, small against the glass, eyes wide, paws pressed high, the house suddenly quiet.
Panel 2: The door clicks shut. Silence breaks. The pet slowly turns toward the empty house, posture shifting, eyes sharp with possibility.
Panel 3: The house transformed. The pet sprawls across the couch like it owns the place, crumbs nearby, sunlight cutting across the room like a spotlight.
Panel 4: The door opens. The pet is seated perfectly by the entrance, alert and composed, as if nothing happened."""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1024x1536", quality="medium")
    save_images(result, "comic_reel")


def example_ui_mockup() -> None:
    prompt = """Create a realistic mobile app UI mockup for a local farmers market.
Show today's market with a simple header, a short list of vendors with small photos and categories, a small "Today's specials" section, and basic information for location and hours.
Design it to be practical, and easy to use. White background, subtle natural accent colors, clear typography, and minimal decoration.
It should look like a real, well-designed, beautiful app for a small local market.
Place the UI mockup in an iPhone frame."""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1024x1536", quality="medium")
    save_images(result, "ui_farmers_market")


def example_scientific_educational() -> None:
    prompt = """Create a simple biology diagram titled "Cellular Respiration at a Glance" for high school students.
Show how glucose turns into energy inside a cell. Include glycolysis, the Krebs cycle, and the electron transport chain.
Use arrows to connect the steps, and label the main molecules: glucose, pyruvate, ATP, NADH, FADH2, CO2, O2, and H2O.
Make it look like a clean classroom handout or slide, with a white background, simple icons, clear labels, and easy-to-read text.
Avoid tiny text, extra decoration, or anything that makes the diagram hard to understand."""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1536x1024", quality="high")
    save_images(result, "scientific_educational_cellular_respiration")


def example_slides_charts() -> None:
    prompt = """Create one pitch-deck slide titled **"Market Opportunity"** that feels like a real Series A fundraising slide from a YC-backed startup.

Use a clean white background, modern sans-serif typography like Inter, and a crisp, minimal layout. The slide should include:

* A TAM/SAM/SOM concentric-circle diagram in muted blues and grays
* Specific, believable market sizing numbers:
  * **TAM:** $42B
  * **SAM:** $8.7B
  * **SOM:** $340M
* A clean bar chart below showing market growth from **2021 to 2026**, with a subtle upward trend
* Small footnotes: **"AGI Research, 2024"** and **"Internal analysis"**
* A company logo placeholder in the bottom-right corner

The design should look like it belongs in a deck that actually raised money: highly readable text, clear data hierarchy, polished spacing, and professional startup-style visual language.

Avoid clip art, stock photography, gradients, shadows, decorative elements, or anything that feels generic or overdesigned."""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1536x864", quality="high")
    save_images(result, "market_opportunity_slide")


if __name__ == "__main__":
    for function in [
        example_infographic,
        example_translation,
        example_photorealistic,
        example_world_knowledge,
        example_logo_generation,
        example_ads_generation,
        example_comic_strip,
        example_ui_mockup,
        example_scientific_educational,
        example_slides_charts,
    ]:
        function()
