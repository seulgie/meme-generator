import subprocess
import os
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel

class PDFIngestor(IngestorInterface):
    """Quotes Ingestor from PDF files"""

    allowed_extensions = ['pdf']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the format is PDF"""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Converts PDF to text using pdftotext CLI tool."""

        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest file type: {path}')

        # Define the temporary file for the output text
        tmp_txt = './temp.txt'

        # Execute pdftotext using subprocess (PDF → TXT)
        try:
            subprocess.run(['C:/Users/gkstm/Downloads/Release-24.08.0-0/poppler-24.08.0/Library/bin/pdftotext.exe', path, tmp_txt], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during PDF to text conversion: {e}")
            raise

        # Read the content of the temporary text file
        with open(tmp_txt, 'r') as file:
            text = file.read()

        # Clean up temporary file
        os.remove(tmp_txt)

        # Parse the text into QuoteModel objects
        quotes = []
        for line in text.splitlines():
            if line.strip():
                body, author = line.strip().rsplit(' - ', 1)
                quotes.append(QuoteModel(body, author))

        return quotes
