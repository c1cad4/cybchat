#!/usr/bin/env python3
"""
Generate CybChat icon with cosmic eye design
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

def create_cosmic_eye_icon(size):
    """Create a cosmic eye icon with the specified size"""
    
    # Create a new image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calculate center and radius
    center = size // 2
    radius = int(size * 0.4)
    
    # Create the main eye shape (elongated oval)
    eye_width = int(radius * 1.8)  # Make it more horizontal
    eye_height = int(radius * 1.2)
    
    # Draw the outer white glow
    for i in range(5):
        glow_radius = radius + i * 3
        alpha = max(0, 100 - i * 20)
        draw.ellipse([
            center - glow_radius, 
            center - glow_radius * 0.7,
            center + glow_radius, 
            center + glow_radius * 0.7
        ], fill=(255, 255, 255, alpha))
    
    # Draw the main eye outline (white)
    draw.ellipse([
        center - eye_width, 
        center - eye_height,
        center + eye_width, 
        center + eye_height
    ], outline=(255, 255, 255, 200), width=3)
    
    # Create iris with swirling patterns
    iris_radius = int(radius * 0.8)
    
    # Draw iris background (dark reddish-brown)
    draw.ellipse([
        center - iris_radius, 
        center - iris_radius,
        center + iris_radius, 
        center + iris_radius
    ], fill=(80, 30, 20, 180))
    
    # Add swirling patterns in the iris
    for i in range(8):
        angle = i * math.pi / 4
        swirl_radius = iris_radius * 0.6
        x = center + int(math.cos(angle) * swirl_radius)
        y = center + int(math.sin(angle) * swirl_radius * 0.7)
        swirl_size = int(iris_radius * 0.3)
        
        # Draw swirl with gradient colors
        colors = [(120, 60, 40), (100, 40, 30), (80, 30, 20)]
        for j, color in enumerate(colors):
            size_offset = j * 2
            alpha = 150 - j * 30
            current_size = max(1, swirl_size - size_offset)
            draw.ellipse([
                x - current_size, 
                y - current_size,
                x + current_size, 
                y + current_size
            ], fill=(*color, alpha))
    
    # Draw the bright green pupil/core
    pupil_radius = int(radius * 0.4)
    
    # Create glowing effect for the green core
    for i in range(8):
        glow_radius = pupil_radius + i * 2
        alpha = max(0, 200 - i * 25)
        green_intensity = max(0, 255 - i * 30)
        draw.ellipse([
            center - glow_radius, 
            center - glow_radius,
            center + glow_radius, 
            center + glow_radius
        ], fill=(0, green_intensity, 0, alpha))
    
    # Draw the main green pupil
    draw.ellipse([
        center - pupil_radius, 
        center - pupil_radius,
        center + pupil_radius, 
        center + pupil_radius
    ], fill=(0, 255, 0, 255))
    
    # Add a bright center highlight
    highlight_radius = int(pupil_radius * 0.3)
    draw.ellipse([
        center - highlight_radius, 
        center - highlight_radius,
        center + highlight_radius, 
        center + highlight_radius
    ], fill=(150, 255, 150, 255))
    
    # Apply a slight blur for the ethereal effect
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    return img

def generate_all_sizes():
    """Generate icons for all required sizes"""
    
    # iOS/macOS icon sizes
    sizes = [
        16, 20, 29, 32, 40, 60, 76, 83, 128, 256, 512, 1024
    ]
    
    # Create output directory
    output_dir = "cybchat_icons"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating CybChat cosmic eye icons...")
    
    for size in sizes:
        print(f"Generating {size}x{size} icon...")
        icon = create_cosmic_eye_icon(size)
        
        # Save regular size
        filename = f"icon_{size}x{size}.png"
        icon.save(os.path.join(output_dir, filename))
        
        # Save @2x version for smaller sizes
        if size <= 128:
            icon_2x = create_cosmic_eye_icon(size * 2)
            filename_2x = f"icon_{size}x{size}@2x.png"
            icon_2x.save(os.path.join(output_dir, filename_2x))
        
        # Save @3x version for iOS sizes
        if size in [20, 29, 40, 60]:
            icon_3x = create_cosmic_eye_icon(size * 3)
            filename_3x = f"icon_{size}x{size}@3x.png"
            icon_3x.save(os.path.join(output_dir, filename_3x))
    
    print(f"All icons generated in {output_dir}/ directory")
    print("You can now copy these files to replace the existing icons in:")
    print("cybchat/Assets.xcassets/AppIcon.appiconset/")

if __name__ == "__main__":
    generate_all_sizes() 