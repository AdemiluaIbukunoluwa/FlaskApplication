from functions import * 
import pytest

book_file = 'tests/mock_books.csv'
@pytest.fixture
def fetch_data():
    return load_books(book_file)

def test_books_length():
    '''
    text that the correct length of books are returned
    '''
    assert len(load_books(book_file)) == 3