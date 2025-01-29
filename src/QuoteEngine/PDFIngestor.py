import subprocess
import os
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

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
        """read PDF file, extract quotes and convert them to QuoteModel list"""

        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest file type: {path}')

        tmp_txt = f'./temp.txt'  # temporary file saving path

        # execute pdftotext using subprocess (PDF → TXT)
        subprocess.run(['pdftotext', path, tmp_txt], check=True)

        quotes = []
        with open(tmp_txt, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(' - ')
                    if len(parts) == 2:
                        body, author = parts
                        quotes.append(QuoteModel(body.strip(), author.strip()))

        os.remove(tmp_txt)  # delete after temporary use

        return quotes
