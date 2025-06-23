import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# configuration
TEMPLATE_PATH = 'templates/certificate_template.jpg'  #JPG template
FONT_PATH = 'DejaVuSans.ttf'
FONT_SIZE_NAME = 65
FONT_SIZE_COLLEGE = 65
OUTPUT_DIR = 'output/'

# creating output directory 
os.makedirs(OUTPUT_DIR, exist_ok=True)

# loading student data
data = pd.read_csv('data/students.csv')

# loading font
try:
    font_name = ImageFont.truetype(FONT_PATH, FONT_SIZE_NAME)
    font_college = ImageFont.truetype(FONT_PATH, FONT_SIZE_COLLEGE)
except:
    print("Font file not found. Please place DejaVuSans.ttf in the folder.")
    exit()

# generating certificates
for index, row in data.iterrows():
    name = row['Name']
    college = row['College']

    print(f"Generating certificate for: {name} | {college}")

    # Load the certificate template
    img = Image.open(TEMPLATE_PATH).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Text placement coordinates
    name_position = (1555,1089)
    college_position = (1161, 1230)

    # Draw text on the image 
    draw.text(name_position, name, fill="black", font=font_name)
    draw.text(college_position, college, fill="black", font=font_college)

    # Save the certificate as PDF
    output_filename = f"{OUTPUT_DIR}/{name.replace(' ', '_')}.pdf"
    img.save(output_filename, "PDF")
    print(f"Saved: {output_filename}")

print(" All certificates generated successfully!")

