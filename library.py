from models.book import Book

def load_books(book_data):
    with open(book_data, 'r') as f:
        books = []
        for line in f:
            isbn, title, author = line.strip().split('%%')
            books.append(Book(isbn, title, author))
    return books    
