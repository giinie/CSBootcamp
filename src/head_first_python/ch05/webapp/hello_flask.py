from flask import Flask
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4')
def do_search(phrase: str = 'life, the universe, and everything', letters: str = 'eiru,') -> str:
    return str(search4letters(phrase=phrase, letters=letters))


app.run()
