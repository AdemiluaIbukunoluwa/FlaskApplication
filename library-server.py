'''
implements library.py function sto the web frontend
'''
from flask import Flask, request, redirect
import jinja2

from library import load_books

app = Flask(__name__)

env = jinja2.Environment( loader=jinja2.FileSystemLoader('.'))

book_data = 'books.csv'

@app.route('/')
def index():
    return "Index page..."

@app.route('/viewbooks')
def viewbooks():
    books = load_books(book_data)
    template = env.get_template('/templates/viewbooks.html.j2')
    return template.render(books=books)

app.run(host="0.0.0.0", port=3000, debug=True)
