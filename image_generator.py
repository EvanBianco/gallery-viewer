import os
import random
from PIL import Image

# Set the directory where the images will be saved
image_dir = "images"

# Set the number of images to generate
num_images = 50

# Set the image size to 1600x900 pixels (16:9 aspect ratio)
width = 1600
height = 900

# Set the maximum color value for each RGB channel
max_color = 255

# Loop through the number of images to generate
for i in range(num_images):
    # Generate a random hue value between 0 and 255
    hue = random.randint(0, 255)
    
    # Create a new image with the specified size and background color
    img = Image.new("RGB", (width, height), (hue, hue, hue))
    
    # Loop through each pixel in the image and set a random RGB value
    for x in range(width):
        for y in range(height):
            r = random.randint(0, max_color)
            g = random.randint(0, max_color)
            b = random.randint(0, max_color)
            img.putpixel((x, y), (r, g, b))
    
    # Save the image with a random file name in the specified directory
    file_name = f"image_{i}.png"
    file_path = os.path.join(image_dir, file_name)
    
    # Compress the image to the target file size using PNG compression level
    img.save(file_path, "PNG")    
    print(f"Saved image {i+1} to {file_path}")
