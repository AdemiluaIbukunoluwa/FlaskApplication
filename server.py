'''
implements library.py function to the web frontend
'''
from flask import Flask, request, redirect, url_for
import jinja2
import requests

from models.note import Note

from functions import *


app = Flask(__name__)

env = jinja2.Environment( loader=jinja2.FileSystemLoader('.'))

filepath = './notes.csv'

notes = get_notes(filepath)

Note.id = notes[-1].id

@app.route('/')
def home():
    indexcss =  url_for('static', filename='css/index.css')
    template = env.get_template('/templates/homepage.html')
    return template.render(notes = notes, csslink = indexcss)

@app.route('/viewnote/<int:id>')
def view_note(id):
    css =  url_for('static', filename='css/notepage.css')
    note = get_note(notes, id)
    return env.get_template('/templates/viewnote.html').render(note=note, csslink = css)

@app.route('/addnote')
def add_note_page():
    template = env.get_template('/templates/newnote.html')
    return template.render()


@app.route('/postnote', methods=['GET', 'POST'])
def add():
    subject = request.form['subject']
    content = request.form["content"]
    new_note = Note(subject, content)
    notes.append(new_note)
    return redirect(url_for('home'))

app.run(host="0.0.0.0", port=3000, debug=True)
