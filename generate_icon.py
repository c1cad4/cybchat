#!/usr/bin/env python3
"""
Generate cybchat app icon based on cosmic eye design
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

def create_cybchat_icon(size):
    """Create cybchat icon at specified size"""
    # Create a new image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calculate center and radius
    center = size // 2
    radius = int(size * 0.4)
    
    # Create the white oval border
    border_width = int(size * 0.08)
    border_rect = [
        center - radius - border_width,
        center - radius - border_width,
        center + radius + border_width,
        center + radius + border_width
    ]
    
    # Draw white border with slight transparency
    draw.ellipse(border_rect, fill=(255, 255, 255, 200))
    
    # Create the dark cosmic background
    cosmic_rect = [
        center - radius,
        center - radius,
        center + radius,
        center + radius
    ]
    
    # Create gradient-like cosmic background
    for i in range(radius):
        alpha = int(255 * (1 - i / radius) * 0.8)
        color = (40, 20, 30, alpha)  # Dark brown/purple
        x1 = max(center - radius + i, 0)
        y1 = max(center - radius + i, 0)
        x2 = min(center + radius - i, size - 1)
        y2 = min(center + radius - i, size - 1)
        if x1 < x2 and y1 < y2:
            draw.ellipse([x1, y1, x2, y2], fill=color)
    
    # Add some cosmic swirls
    for i in range(5):
        angle = i * 2 * math.pi / 5
        swirl_radius = radius * 0.6
        x = center + int(swirl_radius * math.cos(angle))
        y = center + int(swirl_radius * math.sin(angle))
        swirl_size = int(size * 0.1)
        draw.ellipse([
            x - swirl_size,
            y - swirl_size,
            x + swirl_size,
            y + swirl_size
        ], fill=(60, 30, 40, 100))
    
    # Create the bright green center
    center_radius = int(radius * 0.3)
    center_rect = [
        center - center_radius,
        center - center_radius,
        center + center_radius,
        center + center_radius
    ]
    
    # Draw bright green center with glow effect
    for i in range(center_radius + 5):
        alpha = int(255 * (1 - i / (center_radius + 5)))
        green_intensity = int(255 * (1 - i / center_radius))
        color = (0, green_intensity, 100, alpha)
        x1 = max(center - center_radius + i, 0)
        y1 = max(center - center_radius + i, 0)
        x2 = min(center + center_radius - i, size - 1)
        y2 = min(center + center_radius - i, size - 1)
        if x1 < x2 and y1 < y2:
            draw.ellipse([x1, y1, x2, y2], fill=color)
    
    # Add a bright green core
    core_radius = int(center_radius * 0.6)
    core_rect = [
        center - core_radius,
        center - core_radius,
        center + core_radius,
        center + core_radius
    ]
    draw.ellipse(core_rect, fill=(0, 255, 150, 255))
    
    # Apply slight blur for glow effect
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    return img

def main():
    """Generate all required icon sizes"""
    # iOS icon sizes
    ios_sizes = [
        16, 20, 29, 32, 40, 60, 76, 83.5, 128, 256, 512, 1024
    ]
    
    # Create output directory
    output_dir = "cybchat/Assets.xcassets/AppIcon.appiconset"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate icons
    for size in ios_sizes:
        # Handle @2x and @3x variants
        base_size = int(size)
        if size == 83.5:
            filename = "icon_83.5x83.5@2x.png"
            actual_size = 167
        elif size == 60:
            # Generate both @2x and @3x
            for multiplier in [2, 3]:
                actual_size = base_size * multiplier
                filename = f"icon_{base_size}x{base_size}@{multiplier}x.png"
                icon = create_cybchat_icon(actual_size)
                icon.save(os.path.join(output_dir, filename))
            continue
        elif size == 20:
            # Generate @2x and @3x
            for multiplier in [2, 3]:
                actual_size = base_size * multiplier
                filename = f"icon_{base_size}x{base_size}@{multiplier}x.png"
                icon = create_cybchat_icon(actual_size)
                icon.save(os.path.join(output_dir, filename))
            continue
        elif size == 29:
            # Generate @2x and @3x
            for multiplier in [2, 3]:
                actual_size = base_size * multiplier
                filename = f"icon_{base_size}x{base_size}@{multiplier}x.png"
                icon = create_cybchat_icon(actual_size)
                icon.save(os.path.join(output_dir, filename))
            continue
        elif size == 40:
            # Generate @2x and @3x
            for multiplier in [2, 3]:
                actual_size = base_size * multiplier
                filename = f"icon_{base_size}x{base_size}@{multiplier}x.png"
                icon = create_cybchat_icon(actual_size)
                icon.save(os.path.join(output_dir, filename))
            continue
        else:
            filename = f"icon_{base_size}x{base_size}.png"
            actual_size = base_size
        
        icon = create_cybchat_icon(actual_size)
        icon.save(os.path.join(output_dir, filename))
        print(f"Generated {filename} ({actual_size}x{actual_size})")

if __name__ == "__main__":
    main() 