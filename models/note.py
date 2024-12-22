import time
from datetime import date
class Note:
    id = 0
    def __init__(self,subject, content):
        self.id = Note.id+1
        self.subject = subject
        self.content = content
        self.updated_time = time.strftime("%H:%M:%S", time.localtime())
        self.date = date.today()