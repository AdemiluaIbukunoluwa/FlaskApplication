import time
from datetime import datetime
class Note:
    id = 0
    def __init__(self,subject, content, updated_time=None):
        self.id = Note.id
        self.subject = subject
        self.content = content
        if updated_time is None:
            updated_time = datetime.now().strftime('%Y-%m-%d%H:%M')
        self.updated_time = updated_time
        Note.id += 1
    
    def __format__(self, format_spec):
        match format_spec.lower():
            case "short":
                return f"{self.subject} {self.updated_time}"
            case "long":
                return f"{self.subject} {self.content} {self.updated_time}"
            case "object":
                return {
                    "id": self.id,
                    "subject": self.subject,
                    "content": self.content,
                    "updated_time": self.updated_time
                }