from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """Ingestor for .txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest file: {path}')
        
        quotes = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if " - " in line:
                    body, author = line.strip().split(" - ")
                    quotes.append(QuoteModel(body, author))
        return quotes