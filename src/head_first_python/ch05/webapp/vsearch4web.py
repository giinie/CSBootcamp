from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4', methods=['POST'])
def do_search(phrase: str = 'life, the universe, and everything', letters: str = 'eiru,') -> str:
    return str(search4letters(phrase=phrase, letters=letters))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


app.run()
