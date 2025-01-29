from typing import List
import python-docx
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingestor for .docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest file: {path}')
        
        quotes = []
        doc = python-docx.Document(path)
        for para in doc.paragraphs:
            if " - " in para.text:
                body, author = para.text.strip().split(" - ")
                quotes.append(QuoteModel(body, author))
        return quotes
