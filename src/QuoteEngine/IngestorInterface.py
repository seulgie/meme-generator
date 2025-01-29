from abc import ABC, abstractmethod
from typing import List
from QuoteEngine.QuoteModel import QuoteModel

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
