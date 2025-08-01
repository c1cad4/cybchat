#!/usr/bin/env python3
"""
Generate CYB logo with neon green text on cosmic eye background
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

def create_cosmic_eye_background(size):
    """Create a more laconic and smaller cosmic eye background"""
    
    # Create a new image with black background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    
    # Calculate center and radius - make eye smaller
    center = size // 2
    radius = int(size * 0.25)  # Much smaller for laconic look
    
    # Create the main eye shape (elongated oval) - more compact
    eye_width = int(radius * 1.4)  # More compact
    eye_height = int(radius * 0.9)  # More compact
    
    # Draw the outer white glow/outline - simplified and smaller
    for i in range(3):  # Fewer layers for laconic look
        glow_radius = radius + i * 2
        alpha = max(0, 120 - i * 40)
        draw.ellipse([
            center - glow_radius, 
            center - glow_radius * 0.6,
            center + glow_radius, 
            center + glow_radius * 0.6
        ], fill=(255, 255, 255, alpha))
    
    # Draw the main eye outline (white)
    draw.ellipse([
        center - eye_width, 
        center - eye_height,
        center + eye_width, 
        center + eye_height
    ], fill=(255, 255, 255, 80), outline=(255, 255, 255, 200), width=2)
    
    # Draw the iris (dark reddish-brown) - smaller
    iris_width = int(eye_width * 0.8)
    iris_height = int(eye_height * 0.8)
    draw.ellipse([
        center - iris_width, 
        center - iris_height,
        center + iris_width, 
        center + iris_height
    ], fill=(80, 30, 20, 200))
    
    # Add subtle iris texture - simplified
    for i in range(3):
        texture_radius = max(5, iris_width - i * 5)  # Ensure minimum size
        alpha = 100 - i * 30
        draw.ellipse([
            center - texture_radius, 
            center - texture_radius * 0.6,
            center + texture_radius, 
            center + texture_radius * 0.6
        ], fill=(60, 20, 15, alpha))
    
    # Draw the pupil (bright green) - smaller and more centered
    pupil_radius = int(radius * 0.3)  # Much smaller pupil
    draw.ellipse([
        center - pupil_radius, 
        center - pupil_radius,
        center + pupil_radius, 
        center + pupil_radius
    ], fill=(0, 255, 150, 255))
    
    # Add pupil glow - simplified
    for i in range(2):
        glow_radius = pupil_radius + i * 3
        alpha = 150 - i * 50
        draw.ellipse([
            center - glow_radius, 
            center - glow_radius,
            center + glow_radius, 
            center + glow_radius
        ], fill=(0, 255, 150, alpha))
    
    return img

def create_cyb_neon_logo(size):
    """Create CYB logo with neon green text on cosmic eye background"""
    
    # Create the cosmic eye background
    img = create_cosmic_eye_background(size)
    draw = ImageDraw.Draw(img)
    
    # Try to use a system font, fallback to default if not available
    try:
        # Use larger font size for bigger letters
        font_size = int(size * 0.5)  # Keep letters big
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", font_size)
    except:
        try:
            # Fallback to Arial
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
        except:
            # Final fallback to default font
            font = ImageFont.load_default()
    
    # Calculate text position to center it
    text = "CYB"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Draw neon green text with glow effect
    neon_color = (0, 255, 150)  # Bright neon green
    
    # Draw glow effect
    for i in range(5):
        glow_offset = i * 2
        alpha = max(0, 100 - i * 20)
        draw.text((x + glow_offset, y + glow_offset), text, 
                 fill=(*neon_color, alpha), font=font)
        draw.text((x - glow_offset, y + glow_offset), text, 
                 fill=(*neon_color, alpha), font=font)
        draw.text((x + glow_offset, y - glow_offset), text, 
                 fill=(*neon_color, alpha), font=font)
        draw.text((x - glow_offset, y - glow_offset), text, 
                 fill=(*neon_color, alpha), font=font)
    
    # Draw main text
    draw.text((x, y), text, fill=(*neon_color, 255), font=font)
    
    return img

def generate_all_sizes():
    """Generate CYB logos for all required sizes"""
    
    # Create output directory
    output_dir = "cyb_neon_logos"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Standard icon sizes for macOS
    sizes = [16, 32, 128, 256, 512, 1024]
    
    print("Generating CYB logos...")
    
    for size in sizes:
        print(f"Generating {size}x{size} logo...")
        logo = create_cyb_neon_logo(size)
        logo.save(f"{output_dir}/icon_{size}x{size}.png")
        
        # Save @2x version for smaller sizes
        if size <= 128:
            logo_2x = create_cyb_neon_logo(size * 2)
            logo_2x.save(f"{output_dir}/icon_{size}x{size}@2x.png")
        
        # Save @3x version for iOS sizes
        if size in [20, 29, 40, 60]:
            logo_3x = create_cyb_neon_logo(size * 3)
            logo_3x.save(f"{output_dir}/icon_{size}x{size}@3x.png")
    
    print(f"All CYB logos generated in {output_dir}/ directory")

if __name__ == "__main__":
    generate_all_sizes() 