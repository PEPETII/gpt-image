"""
GPT Image 2 生成类案例示例 | Generate Use Case Examples
包含 4.1-4.10 全部10个生成类案例
"""

import os
import base64
from openai import OpenAI

# 初始化客户端
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

MODEL = "gpt-image-2"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output_images")


def save_image(result, filename: str) -> None:
    """保存生成的图像到文件"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for idx, image_data in enumerate(result.data):
        image_bytes = base64.b64decode(image_data.b64_json)
        filepath = os.path.join(OUTPUT_DIR, f"{filename}_{idx}.png")
        with open(filepath, "wb") as f:
            f.write(image_bytes)
        print(f"✅ 图像已保存: {filepath}")


def example_infographic() -> None:
    """4.1 信息图表 - 咖啡机工作流程"""
    prompt = """Create a detailed Infographic of the functioning and flow of an automatic coffee machine like a Jura.
From bean basket, to grinding, to scale, water tank, boiler, etc.
I'd like to understand technically and visually the flow."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1536x1024",
        quality="high",
    )
    save_image(result, "infographic_coffee_machine")


def example_translation() -> None:
    """4.2 图片翻译 - 将信息图文字翻译为西班牙语"""
    # 注意：此案例需要先有信息图图片，这里展示API调用方式
    prompt = "Translate the text in the infographic to Spanish. Do not change any other aspect of the image."
    print("⚠️ 此案例需要输入图像，请参考 edit_examples.py 中的编辑模式调用方式")
    print(f"提示词: {prompt}")


def example_photorealistic() -> None:
    """4.3 照片级写实 - 老水手在渔船上"""
    prompt = """Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.
He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.
He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1024x1536",
        quality="high",
    )
    save_image(result, "photorealistic_sailor")


def example_world_knowledge() -> None:
    """4.4 世界知识 - 1969年伍德斯托克音乐节"""
    prompt = """Create a realistic outdoor crowd scene in Bethel, New York on August 16, 1969.
Photorealistic, period-accurate clothing, staging, and environment."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1536x1024",
        quality="high",
    )
    save_image(result, "world_knowledge_woodstock")


def example_logo_generation() -> None:
    """4.5 Logo生成 - Field & Flour面包店"""
    prompt = """Create an original, non-infringing logo for a company called Field & Flour, a local bakery.
The logo should feel warm, simple, and timeless. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential.
Plain background. Deliver a single centered logo with generous padding. No watermark."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1024x1024",
        n=4,  # 生成4个候选方案
        background="opaque",
    )
    save_image(result, "logo_field_and_flour")


def example_ads_generation() -> None:
    """4.6 广告生成 - Thread街头品牌"""
    prompt = """Give me a cool in culture ad / fashion shot for a brand called Thread.
It's a hip young street brand. The ad shows a group of friends hanging out together with the tagline "Yours to Create."
Make it feel like a polished campaign image for a youth streetwear audience: stylish, contemporary, energetic, and tasteful.
Use clean composition, strong color direction, natural poses, and premium fashion photography cues.
Render the tagline exactly once, clearly and legibly, integrated into the ad layout.
No extra text, no watermarks, no unrelated logos."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1536x1024",
        quality="high",
    )
    save_image(result, "ads_thread_brand")


def example_comic_strip() -> None:
    """4.7 故事转漫画 - 宠物独处4格漫画"""
    prompt = """Create a short vertical comic-style reel with 4 equal-sized panels.
Panel 1: The owner leaves through the front door. The pet is framed in the window behind them, small against the glass, eyes wide, paws pressed high, the house suddenly quiet.
Panel 2: The door clicks shut. Silence breaks. The pet slowly turns toward the empty house, posture shifting, eyes sharp with possibility.
Panel 3: The house transformed. The pet sprawls across the couch like it owns the place, crumbs nearby, sunlight cutting across the room like a spotlight.
Panel 4: The door opens. The pet is seated perfectly by the entrance, alert and composed, as if nothing happened."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1024x1536",
    )
    save_image(result, "comic_strip_pet")


def example_ui_mockups() -> None:
    """4.8 UI模型 - 农贸市场App"""
    prompt = """Create a realistic mobile app UI mockup for a local farmers market.
Show today's market with a simple header, a short list of vendors with small photos and categories, a small "Today's specials" section, and basic information for location and hours.
Design it to be practical, and easy to use. White background, subtle natural accent colors, clear typography, and minimal decoration.
It should look like a real, well-designed, beautiful app for a small local market.
Place the UI mockup in an iPhone frame."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1024x1536",
        quality="high",
    )
    save_image(result, "ui_mockup_farmers_market")


def example_scientific_educational() -> None:
    """4.9 科学/教育 - 细胞呼吸图表"""
    prompt = """Create a simple biology diagram titled "Cellular Respiration at a Glance" for high school students.
Show how glucose turns into energy inside a cell. Include glycolysis, the Krebs cycle, and the electron transport chain.
Use arrows to connect the steps, and label the main molecules: glucose, pyruvate, ATP, NADH, FADH2, CO2, O2, and H2O.
Make it look like a clean classroom handout or slide, with a white background, simple icons, clear labels, and easy-to-read text.
Avoid tiny text, extra decoration, or anything that makes the diagram hard to understand."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1536x1024",
        quality="high",
    )
    save_image(result, "scientific_cellular_respiration")


def example_slides_charts() -> None:
    """4.10 幻灯片/图表 - 市场机会融资幻灯片"""
    prompt = """Create one pitch-deck slide titled "Market Opportunity" that feels like a real Series A fundraising slide from a YC-backed startup.
Use a clean white background, modern sans-serif typography like Inter, and a crisp, minimal layout. The slide should include:
* A TAM/SAM/SOM concentric-circle diagram in muted blues and grays
* Specific, believable market sizing numbers: TAM: $42B, SAM: $8.7B, SOM: $340M
* A clean bar chart below showing market growth from 2021 to 2026, with a subtle upward trend
* Small footnotes: "AGI Research, 2024" and "Internal analysis"
* A company logo placeholder in the bottom-right corner
The design should look like it belongs in a deck that actually raised money: highly readable text, clear data hierarchy, polished spacing, and professional startup-style visual language.
Avoid clip art, stock photography, gradients, shadows, decorative elements, or anything that feels generic or overdesigned."""

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1536x1024",
        quality="high",
    )
    save_image(result, "slide_market_opportunity")


if __name__ == "__main__":
    # 运行所有生成类案例
    print("🎨 GPT Image 2 生成类案例示例")
    print("=" * 50)

    examples = {
        "4.1 信息图表": example_infographic,
        "4.3 照片级写实": example_photorealistic,
        "4.4 世界知识": example_world_knowledge,
        "4.5 Logo生成": example_logo_generation,
        "4.6 广告生成": example_ads_generation,
        "4.7 故事转漫画": example_comic_strip,
        "4.8 UI模型": example_ui_mockups,
        "4.9 科学/教育": example_scientific_educational,
        "4.10 幻灯片/图表": example_slides_charts,
    }

    for name, func in examples.items():
        print(f"\n▶ 运行 {name}...")
        try:
            func()
        except Exception as e:
            print(f"❌ {name} 失败: {e}")

    print("\n✅ 所有案例运行完成！")
