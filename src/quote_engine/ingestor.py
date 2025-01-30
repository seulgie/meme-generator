"""Ingestor Module.

This module provides functionalities to parse various file types
and extract text data for meme gneeration.
"""
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.text_ingestor import TextIngestor
from quote_engine.docx_ingestor import DocxIngestor
from quote_engine.pdf_ingestor import PDFIngestor
from quote_engine.csv_ingestor import CSVIngestor
from quote_engine.quote_model import QuoteModel

class Ingestor(IngestorInterface):
    """Main ingestor that selects the appropriate strategy."""
    
    ingestors = [TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given file and return extracted text.
        
        Args:
            file_path (str): The path to the file.

        Returns:
            List[str]: A list of extracted text strings.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f'Unsupported file format: {path}')
