from models.note import Note
import os


STORAGE = os.getenv("STORAGE", "file")

id = 0

def get_notes(filepath):
    if STORAGE == "file":
        data = []
        with open(filepath) as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip().split("%%")
                id, subject, content, time, date = line
                note = Note(subject, content)
                note.updated_time = date + time
                note.id = int(id)
                data.append(note)
    return data

def get_note(notes, id):
    '''
        get the note with the specified id
    '''
    for note in notes:
        if note.id == id:
            return note
        