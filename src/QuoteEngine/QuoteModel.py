class QuoteModel:
    """A class to represent a quote with a body and an author."""

    def __init__(self, body: str, author: str):
        self.body = body.strip('\"')
        self.author = author

    def __str__(self):
        return f'{self.body}" - {self.author}'
    
    def __repr__(self):
        return self.__str__()
    