"""A class to parse a pdf file and return a list of QuoteModel objects."""
import subprocess
import tempfile

from QuoteEngine.quote_ingestor_interface import IngestorInterface
from QuoteEngine.quote_model import QuoteModel
from QuoteEngine.text_file_ingestor import TextFileIngestor


class PDFFileIngestor(IngestorInterface):
    """Class to parse a pdf file and return a list of QuoteModel objects."""
    
    allowed_file_extensions = ['pdf']

    @classmethod
    def parse(cls, file_path) -> list:
        """
        Given a pdf file, return a list of QuoteModel objects. We create a temporary text file from the pdf file and then parse that text file.

        :param file_path: The path to the file to be parsed
        :return: A list of QuoteModel objects
        """
        if not cls.can_ingest(file_path):
            raise Exception(
                f'File type not supported. Only {cls.allowed_file_extensions} are supported.')

        # create a temporary text file from the pdf file
        temporary_text_file = tempfile.NamedTemporaryFile(suffix='.txt')

        # use subprocess to convert pdf to text
        subprocess.call(['pdftotext', file_path, temporary_text_file.name])

        # parse the temporary text file
        return TextFileIngestor.parse(temporary_text_file.name)
