"""Model of a quote."""
class QuoteModel:
    """A representation of a quote and its author."""

    def __init__(self, body, author):
        """
        Initialize a QuoteModel object with a body and author.

        :param body: The body of the quote.
        :param author: The author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """
        Return a string representation of the QuoteModel object.

        :return: A string representation of the QuoteModel object.
        """
        return f'{self.body} - {self.author}'
