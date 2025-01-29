# Meme Generator Project

## Overview

The **Meme Generator** is a Python-based multimedia application that dynamically generates memes by
overlaying quotes on images. The application can:
- Load quotes from various file formats (CSV, DOCX, PDF, TXT)
- Load, manipulate, and save images using Python's Pillow (PIL) library
- Accept dynamic user input via a command-line tool and a web service (Flask)

This project demonstrates proficiency in object-oriented programming (OOP), abstraction, working with
different file types, and image processing.

## Installation & Setup

Ensure you have Python 3.7+ installed on your system. Install required dependencies using a virtual environment.

1. Clone the Repository
```bash
git clone https://github.com/seulgie/meme-generator.git
cd meme-generator
```

2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

1. Run the Command-Line ToolTo generate a meme from a random quote and image:
```bash
python main.py --path ./_data/photos/dog/xander_1.jpg --body "Life is awesome" --author "Susan"
```

2. Run the Flask Web App
Start the Flask server:
```bash
python app.py
```
Then, open http://127.0.0.1:5000/ in your browser to generate memes dynamically.

## Sub-Module Responsibilities

### QuoteEngine
- Parses and extracts quotes from CSV, DOCX, PDF, and TXT files.
- Implements an Ingestor Interface with strategy objects for each file type.
- Example usage:
```bash
from src.QuoteEngine import Ingestor
quotes = Ingestor.parse("./_data/DogQuotes/DogQuotesCSV.csv")
```

### MemeEngine
- Loads, resizes, and overlays text on images.
- Saves the final meme and returns its file path.
- Example usage:
```bash
from src.MemeEngine import MemeEngine
meme = MemeEngine("./static")
meme_path = meme.make_meme("./_data/photos/dogs/xander_1.jpg", "Hello World", "Susan")
```

### Flask Web Application (`app.py`)
- Serves memes dynamically via a web interface.
- Supports user-uploaded images and custom quotes.
- Accessible at http://127.0.0.1:5000/.

## Exception Handling
- Handles invalid file formats in **QuoteEngine**.
- Catches missing or corrupt image files in **MemeEngine**.
- Provides error messages in the Flask UI.

