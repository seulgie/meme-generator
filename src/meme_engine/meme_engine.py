"""Meme Engine Module.

This module provides class with functions to generate memes by overlaying quotes on images.
"""
from PIL import Image, ImageDraw, ImageFont
import os
import random

class MemeEngine:
    """A class to generate memes by overlaying quotes on images."""

    def __init__(self, output_dir: str):
        """
        Initialize MemeEngine with an output directory.

        :param output_dir: Dictionary where modified images will be saved.
        """
        self.output_dir = output_dir

        # Ensure that output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """
        Create a meme with a quote on an image.

        :param img_path: Path to the input image.
        :param text: Quote text.
        :param author: Quote author.
        :param width: Desired width of the meme (default=500px).
        :return: Path to the generated meme image.
        """
        try:
            # Load the image
            img = Image.open(img_path)

            # Resize image while maintaining aspect ratio
            aspect_ratio = img.height / img.width
            new_height = int(width * aspect_ratio)
            img = img.resize((width, new_height), Image.Resampling.LANCZOS)

            # Prepare text to overlay
            draw = ImageDraw.Draw(img)
            font_path = "./fonts/LilitaOne-Regular.ttf" # Path to font file
            try:
                font = ImageFont.truetype(font_path, size=int(new_height / 10))
            except IOError:
                font = ImageFont.load_default()

            # Choose a random position for text
            text_position = (random.randint(10, width - 150), random.randint(10, new_height - 50))
            quote_text = f'"{text}"\n - {author}'

            # Add text overlay
            draw.text(text_position, quote_text, font=font, fill="white", stroke_width=2, stroke_fill="black")

            # Generate unique filename
            output_path = os.path.join(self.output_dir, f'meme_{random.randint(0, 10000)}.jpg')

            # Save the modified image
            img.save(output_path)

            return output_path

        except Exception as e:
            print(f"Error creating meme: {e}")
            return None