# Project Overview
Meme Generator Project.
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. The quotes are in a variety of filetypes, which are parsed and combined with the image to create the final image(meme).

# Setup Instructions
- Before you can proceed with setup, you need to have python3 and virtualenv(or your preffered tool of managing python environments) installed in your machine.
1. Clone this repository.
2. Create a virtual environment - virtualenv venv
3. Activate the virtual environment - source venv/bin/activate
4. Install dependencies - pip install -r requirements.txt
5. Run the flask server:
    - export FLASK_APP=app
    - flask run
- access the app at http://127.0.0.1:5000/

The app is also available on Command Line Interface (CLI)
- Run the  to generate a random quote:
    - python meme.py
- To generate a meme with a specific quote(must specify author as well):
    - python meme.py --body [Quote body] --author [Quote author]
- To generate a meme with a specific image:
    - python meme.py --path [Image path]

# Project Modules
- app: Flask application. Contains the routes and logic for the web app.
Example usage: flask run
Depedencies:
  - flask: Flask web framework
  - Python: Python 3.6

- meme.py: Contains the logic for generating a meme in command line interface.  
Example usage: python meme.py
Depedencies:
  - Python: Python 3.6
  
- MemeGenerator: Contains the logic for generating memes. It is responsible for parsing the quote and image files, and combining them to create the final image. It also contains the logic for generating a random quote. This module is used through the make_meme() function in the app module.

Example usage: MemeGenerator.MemeEngine.make_meme("_data/photos/dog/xander_1.jpg", "this is a quote", "author name")
Dependencies:
  - Python 3.6
  - Pillow package

- QuoteEngine: Contains the logic for parsing quotes from various filetypes. There are different ingestors for different filetypes. All ingestors are inheriting from an abstract IngestorInterface. This module is used through the Ingestor class which is able to use the correct ingestor for different file types.

Example usage: QuoteEngine.Ingestor("_data/quotes/quotes.txt")
Dependencies:
1. Python 3.6
2. python-docx