from functions import * 
import pytest

book_file = 'tests/mock_notes.csv'

@pytest.fixture
def fetch_data():
    return (book_file)

def test_books_length():
    '''
    text that the correct length of books are returned
    '''
    assert len(get_notes(book_file)) == 4

