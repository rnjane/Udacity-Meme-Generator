"""Given an image, a quote and an author, generate a meme."""
import random

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Load image and text from file and create a meme. Resize image to a max of 500px width."""

    def __init__(self, output_dir):
        """
        Initialize meme creator.

        :param output_dir: The directory to save the meme.
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create a meme from an image and quote.

        :param image_path: The path to the image to be used as the background.
        :param quote_body: The body of the quote.
        :param quote_author: The author of the quote.
        :return: The path to the meme image.
        """
        # load image
        try:
            image = Image.open(img_path)
        except Exception as e:
            print(f'Error loading image: {e}')
            return None

        # resize image
        image_width, image_height = image.size
        image_width = image.size[0]
        if image_width > width:
            image = image.resize(
                (
                    width,
                    int(width / image_width * image.size[1])
                ),
                Image.ANTIALIAS
            )

        # overlay text to the image
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(
            "MemeGenerator/fonts/Montserrat-Italic.ttf", int(image.size[1] / 25))
        text_width, text_height = draw.textsize(text, font=font)
        draw.text(((image.size[0] - text_width) / 2, (image.size[1] - text_height) / 2),
                  f'{text} \n- {author}', font=font, fill=(255, 255, 255))

        # save image
        image_name = f'{self.output_dir}/{random.randint(0, 100)}.jpg'
        image.save(image_name)
        return image_name
