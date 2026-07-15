"""Official Cookbook advanced examples for sections 6.1-6.4."""

import base64
from pathlib import Path

from openai import OpenAI


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "docs" / "assets" / "official-cookbook"
OUTPUT_DIR = ROOT / "output_images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
client = OpenAI()


def save_result(result, filename: str) -> Path:
    path = OUTPUT_DIR / filename
    path.write_bytes(base64.b64decode(result.data[0].b64_json))
    print(f"saved {path}")
    return path


def example_interior_design_swap() -> None:
    prompt = """In this room photo, replace ONLY white with chairs made of wood.
Preserve camera angle, room lighting, floor shadows, and surrounding objects.
Keep all other aspects of the image unchanged.
Photorealistic contact shadows and fabric texture."""
    with (ASSET_DIR / "kitchen.jpeg").open("rb") as image:
        result = client.images.edit(
            model="gpt-image-2",
            image=[image],
            prompt=prompt,
            size="1536x1024",
            quality="medium",
        )
    save_result(result, "kitchen-chairs_gpt-image-2.png")


def example_holiday_card() -> None:
    scene_description = (
        "a cozy Christmas scene with an old teddy bear sitting inside a keepsake box, "
        "slightly worn fur, soft stitching repairs, placed near a window with falling snow outside. "
        "The scene suggests the child has grown up, but the memories remain."
    )
    short_copy = "Merry Christmas — some memories never fade."
    prompt = f"""Create a Christmas holiday card illustration.

Scene:
{scene_description}

Mood:
Warm, nostalgic, gentle, emotional.

Style:
Premium holiday card photography, soft cinematic lighting,
realistic textures, shallow depth of field,
tasteful bokeh lights, high print-quality composition.

Constraints:
- Original artwork only
- No trademarks
- No watermarks
- No logos

Include ONLY this card text (verbatim):
"{short_copy}"""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1024x1536", quality="medium")
    save_result(result, "christmas_holiday_card_teddy_gpt-image-2.png")


def example_collectible_figure() -> None:
    character_description = (
        "a vintage-style toy propeller airplane with rounded wings, "
        "a front-mounted spinning propeller, slightly worn paint edges, "
        "classic childhood proportions, designed as a nostalgic holiday collectible"
    )
    short_copy = "Christmas Memories Edition"
    prompt = f"""Create a collectible action figure of {character_description}, in blister packaging.

Concept:
A nostalgic holiday collectible inspired by the simple toy airplanes
children used to play with during winter holidays.
Evokes warmth, imagination, and childhood wonder.

Style:
Premium toy photography, realistic plastic and painted metal textures,
studio lighting, shallow depth of field,
sharp label printing, high-end retail presentation.

Constraints:
- Original design only
- No trademarks
- No watermarks
- No logos

Include ONLY this packaging text (verbatim):
"{short_copy}"""
    result = client.images.generate(model="gpt-image-2", prompt=prompt, size="1024x1536", quality="medium")
    save_result(result, "christmas_collectible_toy_airplane_gpt-image-2.png")


def example_childrens_book() -> None:
    anchor_prompt = """Create a children's book illustration introducing a main character.

Character:
A young, storybook-style hero inspired by a little forest outlaw,
wearing a simple green hooded tunic, soft brown boots, and a small belt pouch.
The character has a kind expression, gentle eyes, and a brave but warm demeanor.
Carries a small wooden bow used only for helping, never harming.

Theme:
The character protects and rescues small forest animals like squirrels, birds, and rabbits.

Style:
Children's book illustration, hand-painted watercolor look,
soft outlines, warm earthy colors, whimsical and friendly.
Proportions suitable for picture books (slightly oversized head, expressive face).

Constraints:
- Original character (no copyrighted characters)
- No text
- No watermarks
- Plain forest background to clearly showcase the character"""
    anchor_result = client.images.generate(
        model="gpt-image-2",
        prompt=anchor_prompt,
        size="1024x1536",
        quality="medium",
    )
    anchor_path = save_result(anchor_result, "childrens_book_illustration_1_gpt-image-2.png")

    story_prompt = """Continue the children's book story using the same character.

Scene:
The same young forest hero is gently helping a frightened squirrel
out of a fallen tree after a winter storm.
The character kneels beside the squirrel, offering reassurance.

Character Consistency:
- Same green hooded tunic
- Same facial features, proportions, and color palette
- Same gentle, heroic personality

Style:
Children's book watercolor illustration,
soft lighting, snowy forest environment,
warm and comforting mood.

Constraints:
- Do not redesign the character
- No text
- No watermarks"""
    with anchor_path.open("rb") as image:
        story_result = client.images.edit(
            model="gpt-image-2",
            image=[image],
            prompt=story_prompt,
            size="1024x1536",
            quality="medium",
        )
    save_result(story_result, "childrens_book_illustration_2_gpt-image-2.png")


if __name__ == "__main__":
    for function in [
        example_interior_design_swap,
        example_holiday_card,
        example_collectible_figure,
        example_childrens_book,
    ]:
        function()
