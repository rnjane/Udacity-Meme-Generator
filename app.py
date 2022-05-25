"""Flask web app."""
import os
import random
import tempfile

import requests
from flask import Flask, abort, render_template, request
from PIL import Image

from MemeGenerator.MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    all_quotes = list()
    for f in quote_files:
        all_quotes.append(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    images = []
    for root, dirs, files in os.walk(images_path):
        images = [os.path.join(root, name) for name in files]

    return all_quotes, images


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(random.choice(quotes))
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_stream = requests.get(
        request.form.get('image_url'),
        stream=True,
        allow_redirects=True
    )
    temporary_image = tempfile.NamedTemporaryFile(
        suffix='.jpg', delete=False).name

    try:
        Image.open(image_stream.raw).save(temporary_image)
    except Exception as e:
        print(e)
        return abort(400)

    quote = QuoteModel(
        body=request.form.get('body'),
        author=request.form.get('author')
    )
    path = meme.make_meme(temporary_image, quote.body, quote.author)

    os.remove(temporary_image)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
