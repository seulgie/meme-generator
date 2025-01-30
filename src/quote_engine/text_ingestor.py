"""TXT Ingestor Module.

This module provides functionality to parse TXT files and extract data.
"""
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel

class TextIngestor(IngestorInterface):
    """Ingestor for .txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a TXT file and return its contents as a list of dictionaries.

        Args:
            file_path (str): The path to the TXT file.

        Returns:
            list: A list of dictionaries where keys are column names and values are row data.
        """
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest file: {path}')
        
        quotes = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if " - " in line:
                    body, author = line.strip().split(" - ")
                    quotes.append(QuoteModel(body, author))
        return quotes