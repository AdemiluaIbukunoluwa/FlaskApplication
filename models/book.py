class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
    
    def __format__(self, format_spec):
        match format_spec.lower():
            case 'short':
                return f'{self.title} ({self.author})'
            case 'long':
                return f'{self.title} by {self.author}'
            case 'file':
                return f'{self.isbn}%%{self.title}%%{self.author}'
            case _:
                raise ValueError(f'Invalid format spec: {format_spec}')