'''
implements library.py function to the web frontend
'''
from flask import Flask, request, redirect, url_for
import jinja2
import requests
from models.note import Note
from functions import *
import mysql.connector


app = Flask(__name__)
env = jinja2.Environment( loader=jinja2.FileSystemLoader('.'))

filepath = './notes.csv'

DATASOURCE = os.getenv("DATASOURCE", "file")
DATABASE = os.getenv("DATABASE","notesdb")
HOST = os.getenv("HOST", "db")
USER = os.getenv("USER", "root")
PASSWORD = os.getenv("PASSWORD", "password")
TABLE = os.getenv("TABLE", "notes")

def create_db():
    db = mysql.connector.connect(
          host=HOST,
        user=USER,
        password=PASSWORD
    )
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
    db.commit()
    cursor.execute(f"USE {DATABASE}")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE}(id INT AUTO_INCREMENT PRIMARY KEY,subject VARCHAR(50),content TEXT,updated_time DATETIME)")
    db.commit()
    db.close

def db_connection():
    create_db()
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database = DATABASE
    )
    return db


@app.route('/')
def home():
    data = []
    if DATASOURCE == "db":
        try:
            db = db_connection()
            cursor = db.cursor()
            cursor.execute("SELECT id,subject,content,updated_time from notes")
            data = cursor.fetchall()
            for i in range(len(data)):
                Note.id = data[i][0]
                note = Note(data[i][1], data[i][2], data[i][3])
                data[i] = note
        except mysql.connector.Error as e:
            print("Error: ", e)
    else:
        data = get_notes(filepath)
    indexcss =  url_for('static', filename='css/index.css')
    template = env.get_template('/templates/homepage.html')
    return template.render(notes = data, csslink = indexcss)


@app.route('/viewnote/<int:id>')
def view_note(id):
    if DATASOURCE == "db":
        try:
            db = db_connection()
            cursor = db.cursor()
            cursor.execute(f"SELECT id,subject,content,updated_time from notes where id = {id}")
            data = cursor.fetchall()
            Note.id = data[0][0]
            note = Note(data[0][1], data[0][2], data[0][3])
        except mysql.connector.Error as e:
            print("Error: ", e)
    else:
        notes = get_notes(filepath)
        note = get_note(notes, id)
    css =  url_for('static', filename='css/notepage.css')
    return env.get_template('/templates/viewnote.html').render(note=note, csslink = css)

@app.route('/addnote')
def add_note_page():
    template = env.get_template('/templates/newnote.html')
    return template.render()


@app.route('/postnote', methods=['GET','POST'])
def add():
    subject = request.form['subject']
    content = request.form["content"]
    Note.id = len(get_notes(filepath)) + 1
    new_note = Note(subject, content)
    
    if DATASOURCE == "db":
        try:
            db = db_connection()
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO notes (subject, content, updated_time) VALUES (%s, %s, %s)", (request.form['subject'], request.form["content"], new_note.updated_time))
            db.commit()
        except mysql.connector.Error as e:
            print("Error: ", e)
    else:
        notes = get_notes(filepath)
        notes.append(new_note)   
    return redirect(url_for('home'))

app.run(host="0.0.0.0", port=3000, debug=True)
