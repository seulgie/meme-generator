"""Quote Model Module.

This module defines the QuoteModel class, which is used to represent a quote.
"""


class QuoteModel:
    """A class to represent a quote with a body and an author."""

    def __init__(self, body: str, author: str):
        """Initialize a QuoteModel instance.
        
        Args:
            body (str): The quote text.
            author (str): The author of the quote.
        """
        self.body = body.strip('\"')
        self.author = author

    def __str__(self):
        """Return a human-readable string representation of the quote."""
        return f'{self.body}" - {self.author}'
    
    def __repr__(self):
        """Return an unambiguous string representation of the quote."""
        return self.__str__()
    