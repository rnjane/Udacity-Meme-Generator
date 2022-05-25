"""Class to parse a csv file and return a list of QuoteModel objects."""
import csv

from QuoteEngine.quote_ingestor_interface import IngestorInterface
from QuoteEngine.quote_model import QuoteModel


class CSVFileIngestor(IngestorInterface):
    """Class to parse a csv file and return a list of QuoteModel objects."""
    
    allowed_file_extensions = ['csv']

    @classmethod
    def parse(cls, file_path) -> list:
        """
        Given a csv file, return a list of QuoteModel objects.

        :param file_path: The path to the file to be parsed
        :return: A list of QuoteModel objects
        """
        if not cls.can_ingest(file_path):
            raise Exception(
                f'File type not supported. Only {cls.allowed_file_extensions} are supported.')

        quotes = []
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                quotes.append(QuoteModel(row[0], row[1]))
        return quotes
