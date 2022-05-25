"""An abstract interface for ingesting quotes. Extend this class to implement a new ingestor."""
from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    """An abstract interface for ingesting quotes. Extend this class to implement a new ingestor."""

    allowed_file_extensions = list()

    @classmethod
    def can_ingest(cls, file_path) -> bool:
        """
        Check if the file can be ingested by this Ingestor.

        :param file_path: The path to the file to be ingested.
        :return: True if the file can be ingested, False otherwise.
        """
        try:
            file_extension = file_path.split('.')[-1]
        except IndexError:
            return False
        return file_extension in cls.allowed_file_extensions

    @classmethod
    @abstractmethod
    def parse(cls, file_path) -> list:
        """
        Return a list of quotes from the given file.
        
        This method is overridden by the child classes with the appropriate implementation of parsing different file types.

        :param file_path: The path to the file to be parsed
        :return: A list of QuoteModel objects
        """
        pass
