"""Flask Web Application for Meme Generator.

This module runs a Flask web server that allows users to create
memes by uploading images and adding captions.
"""
import random
import os
import requests
from flask import Flask, render_template, request
from quote_engine.ingestor import Ingestor
from meme_engine.meme_engine import MemeEngine

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))
    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, img) for img in os.listdir(images_path)
            if img.endswith(('jpg', 'png', 'jpeg'))]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    if not image_url or not body or not author:
        return "Error: Missing required fields."

    tmp_path = f'./static/temp_{random.randint(0, 100000)}.jpg'
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(tmp_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    else:
        return "Error: Unable to download image."

    path = meme.make_meme(tmp_path, body, author)
    os.remove(tmp_path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
