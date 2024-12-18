from ..library import * 
import pytest


@pytest.fixture
def fetch_data():
    return load_books('./mock_books.csv')

def test_books_length():
    '''
    text that the correct length of books are returned
    '''
    assert len(load_books('./mock_books.csv')) == 3