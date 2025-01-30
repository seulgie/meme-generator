"""CSV Ingestor Module.

This module provides functionality to parse CSV files and extract data.
"""
import pandas as pd
from typing import List
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel

class CSVIngestor(IngestorInterface):
    """A class to ingest and parse CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a CSV file and return its contents as a list of dictionaries.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            list: A list of dictionaries where keys are column names and values are row data.
        """
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest file: {path}')
        
        df = pd.read_csv(path)
        quotes = [QuoteModel(row['body'], row['author']) for _, row in df.iterrows()]
        return quotes
    