from typing import List
import docx
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingestor for .docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest file: {path}')
        
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if " - " in para.text:
                body, author = para.text.strip().split(" - ")
                quotes.append(QuoteModel(body, author))
        return quotes
