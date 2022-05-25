"""A class to parse a docx file and return a list of QuoteModel objects."""
import docx

from QuoteEngine.quote_ingestor_interface import IngestorInterface
from QuoteEngine.quote_model import QuoteModel


class DOCXFileIngester(IngestorInterface):
    """Class to parse a docx file and return a list of QuoteModel objects."""
    
    allowed_file_extensions = ['docx']

    @classmethod
    def parse(cls, file_path) -> list:
        """
        Given a docx file, return a list of QuoteModel objects.

        :param file_path: The path to the file to be parsed
        :return: A list of QuoteModel objects
        """
        if not cls.can_ingest(file_path):
            raise Exception(
                f'File type not supported. Only {cls.allowed_file_extensions} are supported.')
        quotes = []

        quotes_document = docx.Document(file_path)
        for quote in quotes_document.paragraphs:
            if quote.text:
                quote_body = quote.text.split('-')[0].strip().strip('\"')
                quote_author = quote.text.split('-')[1].strip()
                quotes.append(QuoteModel(quote_body, quote_author))
        return quotes
