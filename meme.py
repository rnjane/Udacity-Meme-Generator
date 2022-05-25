"""Command Line Interface for the Meme Generator."""
import argparse
import os
import random

from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor, QuoteModel


def generate_meme(path=None, body=None, author=None):
    """
    Generate a meme, given a path and a quote.

    :param path: The path to the image to be used as the meme background
    :param body: The body of the quote
    :param author: The author of the quote
    :return: The path to the meme image
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help='Path to an image file')
    parser.add_argument('-b', '--body', help='Quote body to add to the image')
    parser.add_argument(
        '-a', '--author', help='Quote author to add to the image')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
