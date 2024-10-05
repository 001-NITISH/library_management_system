import pytest
from models.book import Book

def test_create_book():
    book = Book(1, "Harry Potter", 3)
    assert book.book_id == 1
    assert book.name == "Harry Potter"
    assert book.quantity == 3

def test_book_string_representation():
    book = Book(1, "Harry Potter", 3)
    assert str(book) == 'ID: 1, Title: Harry Potter, Quantity: 3'
