import time
from datetime import date
class Note:
    def __init__(self,subject, content):
        self.subject = subject
        self.content = content
        self.updated_time = time.strftime("%H:%M:%S", time.localtime())
        self.date = date.today()