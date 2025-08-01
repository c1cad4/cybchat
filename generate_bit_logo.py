#!/usr/bin/env python3
"""
Generate BIT logo with white text on black background
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_cyb_logo(size):
    """Create a CYB logo with white text on black background"""
    
    # Create a new image with black background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    
    # Try to use a system font, fallback to default if not available
    try:
        # Try to use SF Pro Display (macOS system font)
        font_size = int(size * 0.4)
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", font_size)
    except:
        try:
            # Fallback to Arial
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
        except:
            # Use default font
            font = ImageFont.load_default()
    
    # Calculate text position to center it
    text = "CYB"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Draw white text
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    
    return img

def generate_all_sizes():
    """Generate CYB logos for all required sizes"""
    
    # iOS/macOS icon sizes
    sizes = [
        16, 20, 29, 32, 40, 60, 76, 83, 128, 256, 512, 1024
    ]
    
    # Create output directory
    output_dir = "cyb_logos"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating CYB logos...")
    
    for size in sizes:
        print(f"Generating {size}x{size} logo...")
        logo = create_cyb_logo(size)
        
        # Save regular size
        filename = f"icon_{size}x{size}.png"
        logo.save(os.path.join(output_dir, filename))
        
        # Save @2x version for smaller sizes
        if size <= 128:
            logo_2x = create_cyb_logo(size * 2)
            filename_2x = f"icon_{size}x{size}@2x.png"
            logo_2x.save(os.path.join(output_dir, filename_2x))
        
        # Save @3x version for iOS sizes
        if size in [20, 29, 40, 60]:
            logo_3x = create_cyb_logo(size * 3)
            filename_3x = f"icon_{size}x{size}@3x.png"
            logo_3x.save(os.path.join(output_dir, filename_3x))
    
    print(f"All CYB logos generated in {output_dir}/ directory")
    print("You can now copy these files to replace the existing icons in:")
    print("cybchat/Assets.xcassets/AppIcon.appiconset/")

if __name__ == "__main__":
    generate_all_sizes() 