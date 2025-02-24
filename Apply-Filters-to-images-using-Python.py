# Import necessary libraries
from PIL import Image, ImageEnhance
import os
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Input and output folder paths
input_folder = '/content/drive/MyDrive/your_input_folder'
output_folder = f"{input_folder}_enhanced"  # New folder for enhanced images

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define enhancement parameters
brightness_factor = 1.15  # Adjust brightness (1.0 = original, >1.0 brighter, <1.0 darker)
saturation_factor = 1.0  # Adjust saturation (1.0 = original, >1.0 more saturated, <1.0 desaturated)
contrast_factor = 0.9    # Adjust contrast (1.0 = original, >1.0 higher contrast, <1.0 lower contrast)

# Loop through each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Process .jpg and .png images
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Apply enhancements
        img = ImageEnhance.Brightness(img).enhance(brightness_factor)
        img = ImageEnhance.Color(img).enhance(saturation_factor)
        img = ImageEnhance.Contrast(img).enhance(contrast_factor)
        
        # Save the enhanced image to the output folder
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

print(f"Enhanced images saved in {output_folder}")
