"""DOCX Ingestor Module.

This module provides functionality to parse DOCX files and extract data.
"""
from typing import List
import docx
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingestor for .docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a DOCX file and return its contents as a list of dictionaries.

        Args:
            file_path (str): The path to the DOCX file.

        Returns:
            list: A list of dictionaries where keys are column names and values are row data.
        """
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest file: {path}')
        
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if " - " in para.text:
                body, author = para.text.strip().split(" - ")
                quotes.append(QuoteModel(body, author))
        return quotes
