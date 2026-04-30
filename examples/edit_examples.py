"""
GPT Image 2 编辑类案例示例 | Edit Use Case Examples
包含 5.1-5.9 全部9个编辑类案例
注意：编辑类案例需要输入图像，请将图片放在 images/ 目录下
"""

import os
import base64
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
MODEL = "gpt-image-2"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output_images")
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "images")


def save_image(result, filename: str) -> None:
    """保存生成的图像到文件"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for idx, image_data in enumerate(result.data):
        image_bytes = base64.b64decode(image_data.b64_json)
        filepath = os.path.join(OUTPUT_DIR, f"{filename}_{idx}.png")
        with open(filepath, "wb") as f:
            f.write(image_bytes)
        print(f"✅ 图像已保存: {filepath}")


def load_image(filename: str) -> str:
    """读取图像文件并返回base64编码"""
    filepath = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"图像文件不存在: {filepath}\n请将图片放在 {IMAGES_DIR} 目录下")
    with open(filepath, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def example_style_transfer() -> None:
    """5.1 风格迁移 - 使用参考图像的风格生成新图像"""
    prompt = "Use the same style from the input image and generate a man riding a motorcycle on a white background."

    image_data = load_image("pixels.png")  # 替换为你的风格参考图

    result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}],
        prompt=prompt,
        size="1024x1536",
    )
    save_image(result, "style_transfer_motorcycle")


def example_virtual_try_on() -> None:
    """5.2 虚拟服装试穿 - 为人物换装"""
    prompt = """Edit the image to dress the woman using the provided clothing images. Do not change her face, facial features, skin tone, body shape, pose, or identity in any way. Preserve her exact likeness, expression, hairstyle, and proportions. Replace only the clothing, fitting the garments naturally to her existing pose and body geometry with realistic fabric behavior. Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on. Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks."""

    # 传入人物照片和多张服装图片
    images = []
    for filename in ["woman_in_museum.png", "jacket.png", "tank_top.png", "boots.png"]:
        data = load_image(filename)
        images.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{data}"}})

    result = client.images.edit(
        model=MODEL,
        image=images,
        prompt=prompt,
        size="1024x1536",
        input_fidelity="high",
    )
    save_image(result, "virtual_try_on_outfit")


def example_drawing_to_image() -> None:
    """5.3 素描转图像 - 将手绘草图渲染为照片级图像"""
    prompt = """Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text."""

    image_data = load_image("drawings.png")

    result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}],
        prompt=prompt,
        size="1536x1024",
        input_fidelity="high",
        quality="high",
    )
    save_image(result, "drawing_to_realistic_valley")


def example_product_mockups() -> None:
    """5.4 产品模型 - 提取产品到干净背景"""
    prompt = """Extract the product from the input image and place it on a plain white opaque background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing and a subtle realistic contact shadow.
Do not restyle the product; only remove background and lightly polish."""

    image_data = load_image("shampoo.png")

    result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}],
        prompt=prompt,
        size="1024x1024",
        background="opaque",
        input_fidelity="high",
    )
    save_image(result, "product_mockup_shampoo")


def example_marketing_creatives() -> None:
    """5.5 营销创意 - 带真实文字的广告牌"""
    prompt = """Create a realistic billboard mockup of the shampoo on a highway scene during sunset.
Billboard text (EXACT, verbatim, no extra characters):
"Fresh and clean"
Typography: bold sans-serif, high contrast, centered, clean kerning.
Ensure text appears once and is perfectly legible.
No watermarks, no logos."""

    image_data = load_image("shampoo.png")

    result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}],
        prompt=prompt,
        size="1536x1024",
        quality="high",
    )
    save_image(result, "marketing_billboard_shampoo")


def example_lighting_weather() -> None:
    """5.6 光照天气变换 - 将场景变为冬夜降雪"""
    prompt = "Make it look like a winter evening with snowfall."

    image_data = load_image("billboard_gpt-image-2.png")  # 使用之前生成的广告牌图

    result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}],
        prompt=prompt,
        size="1536x1024",
        input_fidelity="high",
    )
    save_image(result, "lighting_weather_winter")


def example_object_removal() -> None:
    """5.7 物品移除 - 移除手中的花"""
    prompt = "Remove the flower from man's hand. Do not change anything else."

    image_data = load_image("man_with_blue_hat.png")

    result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}],
        prompt=prompt,
        size="1024x1536",
        input_fidelity="high",
    )
    save_image(result, "object_removal_no_flower")


def example_insert_person_scene() -> None:
    """5.8 人物插入场景 - 将人物放入优胜美地营地场景"""
    prompt = """Generate a highly realistic action scene where this person is running away from a large, realistic brown bear attacking a campsite. The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
She is centered in the image but looking away from the camera, wearing outdoorsy camping attire, with dirt on her face and tears in her clothing. She is clearly afraid but focused on escaping, running away from the bear as it destroys the campsite behind her.
The campsite is in Yosemite National Park, with believable natural details. The time of day is dusk, with natural lighting and realistic colors. Everything should feel grounded, authentic, and unstyled, as if captured in a real moment. Avoid cinematic lighting, dramatic color grading, or stylized composition."""

    image_data = load_image("woman_in_museum.png")

    result = client.images.edit(
        model=MODEL,
        image=[{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}],
        prompt=prompt,
        size="1536x1024",
        input_fidelity="high",
        quality="high",
    )
    save_image(result, "insert_person_yosemite")


def example_multi_image_compositing() -> None:
    """5.9 多图合成 - 将狗从一张图合成到另一张图"""
    prompt = "Place the dog from the second image into the setting of image 1, right next to the woman, use the same style of lighting, composition and background. Do not change anything else."

    images = []
    for filename in ["test_woman.png", "test_woman_2.png"]:
        data = load_image(filename)
        images.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{data}"}})

    result = client.images.edit(
        model=MODEL,
        image=images,
        prompt=prompt,
        size="1024x1536",
        input_fidelity="high",
    )
    save_image(result, "multi_image_compositing_dog")


if __name__ == "__main__":
    print("🔧 GPT Image 2 编辑类案例示例")
    print("=" * 50)
    print("⚠️ 编辑类案例需要输入图像，请将图片放在 images/ 目录下")
    print(f"   图像目录: {os.path.abspath(IMAGES_DIR)}")
    print()

    examples = {
        "5.1 风格迁移": example_style_transfer,
        "5.2 虚拟试穿": example_virtual_try_on,
        "5.3 素描转图像": example_drawing_to_image,
        "5.4 产品模型": example_product_mockups,
        "5.5 营销创意": example_marketing_creatives,
        "5.6 光照天气变换": example_lighting_weather,
        "5.7 物品移除": example_object_removal,
        "5.8 人物插入场景": example_insert_person_scene,
        "5.9 多图合成": example_multi_image_compositing,
    }

    for name, func in examples.items():
        print(f"\n▶ 运行 {name}...")
        try:
            func()
        except FileNotFoundError as e:
            print(f"⚠️ {name} 跳过: {e}")
        except Exception as e:
            print(f"❌ {name} 失败: {e}")

    print("\n✅ 所有案例运行完成！")
