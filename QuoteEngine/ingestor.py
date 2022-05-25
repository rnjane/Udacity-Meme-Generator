"""Ingestor class to realize the ingestor interface, and encapsulate the logic of parsing different file types."""
from QuoteEngine.csv_file_ingestor import CSVFileIngestor
from QuoteEngine.docx_file_ingestor import DOCXFileIngester
from QuoteEngine.pdf_ingestor import PDFFileIngestor
from QuoteEngine.quote_ingestor_interface import IngestorInterface
from QuoteEngine.quote_model import QuoteModel
from QuoteEngine.text_file_ingestor import TextFileIngestor


class Ingestor(IngestorInterface):
    """This class is responsible for parsing a file and returning a list of QuoteModel objects."""

    allowed_file_extensions = ['txt', 'csv', 'docx', 'pdf']

    @classmethod
    def parse(cls, file_path) -> list:
        """
        Given a file, return a list of QuoteModel objects.

        :param file_path: The path to the file to be parsed
        :return: A list of QuoteModel objects
        """
        if not cls.can_ingest(file_path):
            raise Exception(
                f'File type not supported. Only {cls.allowed_file_extensions} are supported.')

        file_extension = file_path.split('.')[-1]
        if file_extension == 'csv':
            return CSVFileIngestor.parse(file_path)
        elif file_extension == 'txt':
            return TextFileIngestor.parse(file_path)
        elif file_extension == 'pdf':
            return PDFFileIngestor.parse(file_path)
        elif file_extension == 'docx':
            return DOCXFileIngester.parse(file_path)
