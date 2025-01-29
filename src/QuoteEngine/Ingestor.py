from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    """Main ingestor that selects the appropriate strategy."""
    
    ingestors = [TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f'Unsupported file format: {path}')
