"""Ingestor Interface Module.

Defines an interface for different ingestor classes to implement.
"""
from abc import ABC, abstractmethod
from typing import List
from quote_engine.quote_model import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for all ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file format is supported."""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse files and return QuoteModel instances."""
        pass
