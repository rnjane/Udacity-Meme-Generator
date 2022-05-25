"""A class to parse a text file and return a list of QuoteModel objects."""
from QuoteEngine.quote_ingestor_interface import IngestorInterface
from QuoteEngine.quote_model import QuoteModel


class TextFileIngestor(IngestorInterface):
    """A class to parse a text file and return a list of QuoteModel objects."""
    
    allowed_file_extensions = ['txt']

    @classmethod
    def parse(cls, file_path) -> list:
        """
        Given a text file, return a list of QuoteModel objects.

        :param file_path: The path to the file to be parsed
        :return: A list of QuoteModel objects
        """
        if not cls.can_ingest(file_path):
            raise Exception(
                f'File type not supported. Only {cls.allowed_file_extensions} are supported.')
        quotes = []

        with open(file_path, 'r') as text_file:
            qtes = text_file.readlines()
            for quote in qtes:
                if quote.strip():
                    quote_body = quote.split('-')[0].strip().strip('\"')
                    quote_author = quote.split('-')[1]
                    quotes.append(QuoteModel(quote_body, quote_author))
        return quotes
