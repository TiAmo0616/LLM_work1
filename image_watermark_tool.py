import os
import argparse
from PIL import Image, ImageDraw, ImageFont
import piexif

def extract_exif_date(image_path):
    try:
        exif_data = piexif.load(image_path)
        date_taken = exif_data['Exif'][piexif.ExifIFD.DateTimeOriginal].decode('utf-8')
        return date_taken.split(' ')[0].replace(':', '-')  # Format as YYYY-MM-DD
    except (KeyError, ValueError, piexif.InvalidImageDataError):
        return None

def add_watermark(image_path, output_path, text, font_size, font_color, position):
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", font_size)

        text_width, text_height = draw.textsize(text, font=font)
        width, height = img.size

        if position == "top-left":
            text_position = (10, 10)
        elif position == "center":
            text_position = ((width - text_width) // 2, (height - text_height) // 2)
        elif position == "bottom-right":
            text_position = (width - text_width - 10, height - text_height - 10)
        else:
            raise ValueError("Invalid position. Choose from 'top-left', 'center', 'bottom-right'.")

        draw.text(text_position, text, fill=font_color, font=font)
        img.save(output_path)

def process_images(input_path, font_size, font_color, position):
    if not os.path.exists(input_path):
        print(f"Error: Path '{input_path}' does not exist.")
        return

    if not os.path.isdir(input_path):
        print(f"Error: Path '{input_path}' is not a directory.")
        return

    output_dir = f"{input_path}_watermark"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_path):
        file_path = os.path.join(input_path, filename)

        if not os.path.isfile(file_path):
            continue

        try:
            exif_date = extract_exif_date(file_path)
            if not exif_date:
                print(f"Skipping '{filename}': No EXIF date found.")
                continue

            output_path = os.path.join(output_dir, filename)
            add_watermark(file_path, output_path, exif_date, font_size, font_color, position)
            print(f"Processed '{filename}' -> '{output_path}'")
        except Exception as e:
            print(f"Error processing '{filename}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Add EXIF date as watermark to images.")
    parser.add_argument("input_path", help="Path to the directory containing images.")
    parser.add_argument("--font-size", type=int, default=20, help="Font size for the watermark (default: 20).")
    parser.add_argument("--font-color", default="black", help="Font color for the watermark (default: black).")
    parser.add_argument("--position", choices=["top-left", "center", "bottom-right"], default="bottom-right",
                        help="Position of the watermark (default: bottom-right).")

    args = parser.parse_args()
    process_images(args.input_path, args.font_size, args.font_color, args.position)

if __name__ == "__main__":
    main()