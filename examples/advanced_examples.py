"""
GPT Image 2 高级案例示例 | Advanced Use Case Examples
包含 6.1-6.4 高级用例，含多步骤工作流
"""

import os
import base64
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
MODEL = "gpt-image-2"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output_images")
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "images")


def save_image(result, filename: str) -> str:
    """保存生成的图像到文件，返回保存路径"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, f"{filename}.png")
    image_bytes = base64.b64decode(result.data[0].b64_json)
    with open(filepath, "wb") as f:
        f.write(image_bytes)
    print(f"✅ 图像已保存: {filepath}")
    return filepath


def load_image(filename: str) -> str:
    """读取图像文件并返回base64编码"""
    filepath = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"图像文件不存在: {filepath}")
    with open(filepath, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def example_interior_design_swap() -> None:
    """6.1 室内设计替换 - 将白色椅子替换为木椅"""
    prompt = """In this room photo, replace ONLY white chairs with chairs made of wood.
Preserve camera angle, room lighting, floor shadows, and surrounding objects.
Keep all other aspects of the image unchanged.
Photorealistic contact shadows and fabric texture."""

    image_data = load_image("kitchen.jpeg")

    result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}],
        prompt=prompt,
        size="1536x1024",
        input_fidelity="high",
    )
    save_image(result, "interior_design_chair_swap")


def example_holiday_card() -> None:
    """6.2 3D立体节日贺卡 - 圣诞节泰迪熊纪念品贺卡"""
    prompt = """Create a Christmas holiday card illustration.

Scene:
a cozy Christmas scene with an old teddy bear sitting inside a keepsake box, slightly worn fur, soft stitching repairs, placed near a window with falling snow outside. The scene suggests the child has grown up, but the memories remain.

Mood:
Warm, nostalgic, gentle, emotional.

Style:
Premium holiday card photography, soft cinematic lighting, realistic textures, shallow depth of field, tasteful bokeh lights, high print-quality composition.

Constraints:
- Original artwork only
- No trademarks
- No watermarks
- No logos

Include ONLY this card text (verbatim):
"Merry Christmas -- some memories never fade.\""""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1024x1536",
        quality="high",
    )
    save_image(result, "holiday_card_teddy")


def example_collectible_toy() -> None:
    """6.3 收藏级手办 - 复古螺旋桨玩具飞机"""
    prompt = """Create a collectible action figure of a vintage-style toy propeller airplane with rounded wings, a front-mounted spinning propeller, slightly worn paint edges, classic childhood proportions, designed as a nostalgic holiday collectible, in blister packaging.

Concept:
A nostalgic holiday collectible inspired by the simple toy airplanes children used to play with during winter holidays. Evokes warmth, imagination, and childhood wonder.

Style:
Premium toy photography, realistic plastic and painted metal textures, studio lighting, shallow depth of field, sharp label printing, high-end retail presentation.

Constraints:
- Original design only
- No trademarks
- No watermarks
- No logos

Include ONLY this packaging text (verbatim):
"Christmas Memories Edition\""""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1024x1536",
        quality="high",
    )
    save_image(result, "collectible_toy_airplane")


def example_childrens_book() -> None:
    """6.4 儿童绘本艺术 - 两步法保持角色一致性"""

    # Step 1: 角色锚点 - 建立角色外观
    print("📖 Step 1: 创建角色锚点...")
    character_prompt = """Create a children's book illustration introducing a main character.

Character:
A young, storybook-style hero inspired by a little forest outlaw, wearing a simple green hooded tunic, soft brown boots, and a small belt pouch. The character has a kind expression, gentle eyes, and a brave but warm demeanor. Carries a small wooden bow used only for helping, never harming.

Theme:
The character protects and rescues small forest animals like squirrels, birds, and rabbits.

Style:
Children's book illustration, hand-painted watercolor look, soft outlines, warm earthy colors, whimsical and friendly. Proportions suitable for picture books (slightly oversized head, expressive face).

Constraints:
- Original character (no copyrighted characters)
- No text
- No watermarks
- Plain forest background to clearly showcase the character"""

    character_result = client.images.generate(
        model=MODEL,
        prompt=character_prompt,
        size="1024x1536",
        quality="high",
    )
    character_path = save_image(character_result, "childrens_book_character_anchor")

    # Step 2: 故事延续 - 使用角色锚点保持一致性
    print("📖 Step 2: 使用角色锚点创建续集...")
    story_prompt = """Continue the children's book story using the same character.

Scene:
The same young forest hero is gently helping a frightened squirrel out of a fallen tree after a winter storm. The character kneels beside the squirrel, offering reassurance.

Character Consistency:
- Same green hooded tunic
- Same facial features, proportions, and color palette
- Same gentle, heroic personality

Style:
Children's book watercolor illustration, soft lighting, snowy forest environment, warm and comforting mood.

Constraints:
- Do not redesign the character
- No text
- No watermarks"""

    # 读取Step 1生成的角色图像作为参考
    with open(character_path, "rb") as f:
        character_image_data = base64.standard_b64encode(f.read()).decode("utf-8")

    story_result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{character_image_data}"}}],
        prompt=story_prompt,
        size="1024x1536",
        quality="high",
        input_fidelity="high",
    )
    save_image(story_result, "childrens_book_story_continuation")
    print("✅ 儿童绘本两步工作流完成！")


if __name__ == "__main__":
    print("🚀 GPT Image 2 高级案例示例")
    print("=" * 50)

    examples = {
        "6.1 室内设计替换": example_interior_design_swap,
        "6.2 3D立体节日贺卡": example_holiday_card,
        "6.3 收藏级手办": example_collectible_toy,
        "6.4 儿童绘本艺术": example_childrens_book,
    }

    for name, func in examples.items():
        print(f"\n▶ 运行 {name}...")
        try:
            func()
        except FileNotFoundError as e:
            print(f"⚠️ {name} 跳过: {e}")
        except Exception as e:
            print(f"❌ {name} 失败: {e}")

    print("\n✅ 所有高级案例运行完成！")
