#!/usr/bin/env python3
"""
Generate CYB logo with cosmic eye for GitHub README
"""

from PIL import Image, ImageDraw, ImageFont
import math
import random

def create_cosmic_eye_cyb_logo(size=512):
    """Create CYB logo with cosmic eye background"""
    
    # Create base image with dark background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calculate dimensions
    center = size // 2
    radius = int(size * 0.4)
    
    # Create cosmic eye background
    # Outer glow
    for i in range(20):
        alpha = int(255 * (1 - i/20) * 0.3)
        color = (0, 255, 0, alpha)  # Green glow
        draw.ellipse([center-radius-i, center-radius-i, center+radius+i, center+radius+i], 
                    fill=color, outline=None)
    
    # Main eye background (cosmic space)
    draw.ellipse([center-radius, center-radius, center+radius, center+radius], 
                fill=(20, 20, 40, 255))
    
    # Add cosmic texture (stars and nebula)
    for _ in range(100):
        x = random.randint(center-radius+20, center+radius-20)
        y = random.randint(center-radius+20, center+radius-20)
        if (x-center)**2 + (y-center)**2 < (radius-20)**2:
            brightness = random.randint(100, 255)
            size_star = random.randint(1, 3)
            color = (brightness, brightness, brightness, 255)
            draw.ellipse([x-size_star, y-size_star, x+size_star, y+size_star], fill=color)
    
    # Add nebula swirls
    for i in range(5):
        start_angle = random.uniform(0, 2*math.pi)
        for j in range(50):
            angle = start_angle + j * 0.1
            r = random.uniform(radius*0.3, radius*0.8)
            x = center + int(r * math.cos(angle))
            y = center + int(r * math.sin(angle))
            if 0 <= x < size and 0 <= y < size:
                alpha = int(255 * (1 - j/50) * 0.4)
                color = (0, 100 + random.randint(0, 155), 100 + random.randint(0, 155), alpha)
                draw.point((x, y), fill=color)
    
    # Create iris (cosmic eye)
    iris_radius = int(radius * 0.6)
    draw.ellipse([center-iris_radius, center-iris_radius, center+iris_radius, center+iris_radius], 
                fill=(0, 50, 100, 255))
    
    # Add iris texture
    for _ in range(30):
        x = random.randint(center-iris_radius+10, center+iris_radius-10)
        y = random.randint(center-iris_radius+10, center+iris_radius-10)
        if (x-center)**2 + (y-center)**2 < (iris_radius-10)**2:
            color = (0, 150 + random.randint(0, 105), 200 + random.randint(0, 55), 255)
            draw.point((x, y), fill=color)
    
    # Create pupil
    pupil_radius = int(iris_radius * 0.4)
    draw.ellipse([center-pupil_radius, center-pupil_radius, center+pupil_radius, center+pupil_radius], 
                fill=(0, 0, 0, 255))
    
    # Add pupil highlight
    highlight_radius = int(pupil_radius * 0.3)
    highlight_x = center - int(pupil_radius * 0.3)
    highlight_y = center - int(pupil_radius * 0.3)
    draw.ellipse([highlight_x-highlight_radius, highlight_y-highlight_radius, 
                  highlight_x+highlight_radius, highlight_y+highlight_radius], 
                fill=(255, 255, 255, 200))
    
    # Add CYB text with neon effect
    try:
        # Try to use a system font
        font_size = int(size * 0.15)
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    text = "CYB"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Position text at bottom of logo
    text_x = center - text_width // 2
    text_y = center + radius + 20
    
    # Add neon glow effect
    for i in range(10):
        alpha = int(255 * (1 - i/10) * 0.6)
        color = (0, 255, 0, alpha)  # Neon green
        draw.text((text_x-i, text_y-i), text, font=font, fill=color)
        draw.text((text_x+i, text_y-i), text, font=font, fill=color)
        draw.text((text_x-i, text_y+i), text, font=font, fill=color)
        draw.text((text_x+i, text_y+i), text, font=font, fill=color)
    
    # Main text
    draw.text((text_x, text_y), text, font=font, fill=(0, 255, 0, 255))
    
    return img

def main():
    """Generate the logo"""
    print("Generating CYB logo with cosmic eye...")
    
    # Generate different sizes
    sizes = [256, 512, 1024]
    
    for size in sizes:
        logo = create_cosmic_eye_cyb_logo(size)
        filename = f"cyb_logo_{size}x{size}.png"
        logo.save(filename, "PNG")
        print(f"Generated {filename}")
    
    print("Logo generation complete!")

if __name__ == "__main__":
    main() 