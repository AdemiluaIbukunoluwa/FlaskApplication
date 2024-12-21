from models.note import Note
import os

filepath = './notes.csv'

STORAGE = os.getenv("STORAGE", "file")



def get_notes():
    if STORAGE == "file":
        data = []
        with open(filepath) as file:
            lines = file.readlines()
            for line in lines:
                line = line.split("%%")
                id, subject, content, time, date = line
                note = {"id": id, "subject": subject, "content": content, "time": time, "date": date}
                data.append(note)
            return data