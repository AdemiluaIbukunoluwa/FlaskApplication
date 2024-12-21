from functions import * 
import pytest

book_file = 'tests/mock_notes.csv'

@pytest.fixture
def fetch_data():
    return (book_file)

def test_books_length():
    '''
    test that the correct length of books are returned
    '''
    assert len(get_notes(book_file)) == 4


def test_get_note():
    '''
        tests the get_note function
        checks that the correct book is retrieved

    '''
    notes = get_notes(book_file)
    book_id = 2
    note =  get_note(notes, book_id)
    expected = {"id": 2, "subject": "Grocery List", "content": "Milk, Eggs, Bread, Butter.", "time": "14:00", "date": "2024-12-21"}
    assert note == expected


