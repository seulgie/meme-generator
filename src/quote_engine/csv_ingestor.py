import pandas as pd
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel

class CSVIngestor(IngestorInterface):
    """Ingestor for .csv files using pandas."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest file: {path}')
        
        df = pd.read_csv(path)
        quotes = [QuoteModel(row['body'], row['author']) for _, row in df.iterrows()]
        return quotes
    