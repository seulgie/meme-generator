"""Meme Generator Command Line Tool.

This module allows users to generate memes from the command line
by providing an image, a quote, and an author. If no arguments
are provided, random values will be used.
"""

import os
import random
import argparse
from PIL import Image
from meme_engine.meme_engine import MemeEngine
from quote_engine.ingestor import Ingestor
from pathlib import Path

# Define paths
OUTPUT_DIR = "./static/memes/"
QUOTES_DIR = "./_data/DogQuotes"

def generate_meme(path=None, body=None, author=None):
    """Generate a meme and return the generated image path.
    
    Args:
        image_path (str, optional): Path to the input image.
        body (str, optional): Quote text for the meme.
        author (str, optional): Author of the quote.

    Returns:
        str: Path to the generated meme image.
    """
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # If no image is provided, select a random one
    if not path:
        image_folder = "./_data/photos/dog/"
        image_path = random.choice(list(Path(image_folder).glob("*.jpg")))

    # If no quote is provided, select a random one
    if not body or not author:
        quote_files = list(Path(QUOTES_DIR).glob("*.txt"))
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(str(file)))

        if quotes:
            random_quote = random.choice(quotes)
            body = body or random_quote.body
            author = author or random_quote.author

    # Create meme
    meme_generator = MemeEngine(OUTPUT_DIR)
    output_path = meme_generator.make_meme(str(path), body, author)

    return output_path


def main():
    """Parse command-line arguments and generate a meme."""
    parser = argparse.ArgumentParser(description="Meme Generator CLI")
    parser.add_argument("--path", type=str, help="Path to an image file")
    parser.add_argument("--body", type=str, help="Quote text")
    parser.add_argument("--author", type=str, help="Author of the quote")

    args = parser.parse_args()

    meme_path = generate_meme(args.path, args.body, args.author)
    print(f"Meme generated: {meme_path}")


if __name__ == "__main__":
    main()
            