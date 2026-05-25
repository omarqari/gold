#!/usr/bin/env python3
"""
Aging pipeline for the Hiro Nakamura Wikipedia page.
Drop coin/barrel photos into the Gold folder, then run this script.
It will produce aged versions ready to embed in the HTML.
"""

import os, sys, random, base64
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageOps

# ── CONFIG ────────────────────────────────────────────────────────────────────
GOLD_DIR   = Path(__file__).parent
OUTPUT_DIR = GOLD_DIR / "aged_images"
OUTPUT_DIR.mkdir(exist_ok=True)

# Map source filenames → output name + style
# Edit these to match whatever filenames you dropped in
JOBS = {
    # coin images → daguerreotype style
    "coin_front": "style_daguerreotype",
    "coin_back":  "style_daguerreotype",
    # barrel images → sepia documentary style
    "barrel_1":   "style_sepia",
    "barrel_2":   "style_sepia",
    "barrel_3":   "style_sepia",
    "barrel_4":   "style_sepia",
}

def find_images(directory):
    """Auto-detect image files in Gold folder (excluding already-aged ones)."""
    exts = {".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"}
    return [
        f for f in Path(directory).iterdir()
        if f.suffix in exts
        and f.name != __file__
        and "aged_" not in f.name
        and f.parent != OUTPUT_DIR
    ]

def add_sepia(img):
    """Convert to warm sepia tone."""
    gray = img.convert("L")
    sepia = Image.new("RGB", gray.size)
    pixels = gray.load()
    sepia_px = sepia.load()
    for y in range(gray.height):
        for x in range(gray.width):
            v = pixels[x, y]
            sepia_px[x, y] = (
                min(255, int(v * 1.08)),
                min(255, int(v * 0.85)),
                min(255, int(v * 0.62)),
            )
    return sepia

def add_noise(img, intensity=18):
    """Add film grain noise."""
    import numpy as np
    arr = np.array(img).astype(float)
    noise = np.random.normal(0, intensity, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)

def add_vignette(img, strength=0.55):
    """Darken edges like an old lens."""
    w, h = img.size
    vignette = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(vignette)
    steps = 80
    for i in range(steps):
        ratio = i / steps
        alpha = int(255 * (1 - ratio) * strength)
        margin_x = int(w * ratio / 2)
        margin_y = int(h * ratio / 2)
        draw.ellipse(
            [margin_x, margin_y, w - margin_x, h - margin_y],
            fill=min(255, alpha + int(255 * ratio * (1 - strength)))
        )
    # Invert: bright center, dark edges
    vignette = ImageOps.invert(vignette)
    vignette_rgb = Image.merge("RGB", [vignette, vignette, vignette])
    return Image.blend(img.convert("RGB"), vignette_rgb, alpha=0.35)

def add_scratches(img, count=18):
    """Add faint horizontal/diagonal scratches."""
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for _ in range(count):
        y = random.randint(0, h)
        x1 = random.randint(0, w // 2)
        x2 = random.randint(w // 2, w)
        alpha = random.randint(30, 80)
        draw.line([(x1, y), (x2, y + random.randint(-3, 3))],
                  fill=(alpha, alpha, alpha), width=1)
    return img

def add_spots(img, count=12):
    """Add age spots / foxing."""
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for _ in range(count):
        x = random.randint(0, w)
        y = random.randint(0, h)
        r = random.randint(2, 8)
        v = random.randint(100, 160)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(v, int(v*0.8), int(v*0.55)))
    return img

def style_sepia(img):
    """Classic warm sepia documentary photograph."""
    img = img.convert("RGB")
    # Slight desaturation first
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(0.3)
    # Soften
    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    # Sepia tone
    img = add_sepia(img)
    # Lower contrast slightly (aged fade)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(0.80)
    # Brighten slightly (faded look)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.08)
    # Grain
    img = add_noise(img, intensity=14)
    # Vignette
    img = add_vignette(img, strength=0.5)
    # Scratches
    img = add_scratches(img, count=20)
    # Age spots
    img = add_spots(img, count=8)
    return img

def style_daguerreotype(img):
    """High-contrast silvery daguerreotype for the coin close-ups."""
    img = img.convert("RGB")
    # Convert to grayscale
    img = img.convert("L").convert("RGB")
    # Boost contrast strongly
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.6)
    # Slight sharpen for metallic look
    img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=120, threshold=3))
    # Add cool silver tint
    arr_list = img.split()
    r = ImageEnhance.Brightness(arr_list[0]).enhance(0.95)
    g = ImageEnhance.Brightness(arr_list[1]).enhance(0.97)
    b = ImageEnhance.Brightness(arr_list[2]).enhance(1.05)
    img = Image.merge("RGB", [r, g, b])
    # Grain
    img = add_noise(img, intensity=20)
    # Strong vignette
    img = add_vignette(img, strength=0.65)
    # Scratches
    img = add_scratches(img, count=30)
    return img

def process(src_path, style_fn, out_name):
    print(f"  Processing {src_path.name} → {out_name} ({style_fn.__name__})")
    img = Image.open(src_path)
    # Resize to reasonable Wikipedia width
    max_w = 800
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.LANCZOS)
    aged = style_fn(img)
    out_path = OUTPUT_DIR / out_name
    aged.save(out_path, "JPEG", quality=78)
    return out_path

def to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ── MAIN ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    images = find_images(GOLD_DIR)
    if not images:
        print("❌  No images found in Gold folder. Drop your coin/barrel photos in and re-run.")
        sys.exit(1)

    print(f"Found {len(images)} image(s): {[f.name for f in images]}")
    print()

    # Auto-assign styles based on count / order
    coin_imgs   = [f for f in images if "coin" in f.name.lower()]
    barrel_imgs = [f for f in images if "barrel" in f.name.lower()]
    other_imgs  = [f for f in images if f not in coin_imgs + barrel_imgs]

    # If user didn't name them, split first 2 as coin, rest as barrel
    if not coin_imgs and not barrel_imgs:
        coin_imgs   = images[:2]
        barrel_imgs = images[2:]

    results = []

    for i, src in enumerate(coin_imgs):
        out = process(src, style_daguerreotype, f"aged_coin_{i+1}.jpg")
        results.append(("coin", i+1, out))

    for i, src in enumerate(barrel_imgs + other_imgs):
        out = process(src, style_sepia, f"aged_barrel_{i+1}.jpg")
        results.append(("barrel", i+1, out))

    print()
    print(f"✅  Done! {len(results)} aged image(s) saved to aged_images/")
    print()

    # Print base64 embed tags for copy-paste into HTML
    print("── Base64 src strings for HTML embedding ──────────────────────────")
    for kind, idx, path in results:
        b64 = to_base64(path)
        tag = f'data:image/jpeg;base64,{b64[:60]}...'
        print(f"  aged_{kind}_{idx}.jpg  →  (base64, {len(b64)//1024}KB)")
    print()
    print("Run embed_into_html.py next to automatically patch the Wikipedia page.")
