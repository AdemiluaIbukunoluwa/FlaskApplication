'''
implements library.py function to the web frontend
'''
from flask import Flask, request, redirect, url_for
import jinja2
import requests

from functions import get_notes

app = Flask(__name__)

env = jinja2.Environment( loader=jinja2.FileSystemLoader('.'))

filepath = './notes.csv'


@app.route('/')
def home():
    indexcss =  url_for('static', filename='css/index.css')
    notes = get_notes(filepath)
    template = env.get_template('/templates/homepage.html')
    return template.render(notes = notes, csslink = indexcss)

@app.route('/viewnote/:id')
def view_note():
    pass

@app.route('/addnote')
def add():
    pass

app.run(host="0.0.0.0", port=3000, debug=True)
