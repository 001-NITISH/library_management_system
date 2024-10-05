import pytest
from models.admin import Admin
from models.book import Book
from models.user import Student, Faculty
from utils.exceptions import BookNotFoundException, UserNotFoundException

def test_add_book():
    admin = Admin()
    admin.add_book(101, "Data Structures", 5)

    assert len(admin.books) == 1
    assert admin.books[0].name == "Data Structures"

def test_add_duplicate_book():
    admin = Admin()
    admin.add_book(101, "Data Structures", 5)

    with pytest.raises(Exception):
        admin.add_book(101, "Data Structures", 5)

def test_add_user_student():
    admin = Admin()
    admin.add_user("student", 1, "Alice")

    assert len(admin.users) == 1
    assert isinstance(admin.users[0], Student)
    assert admin.users[0].name == "Alice"

def test_add_user_faculty():
    admin = Admin()
    admin.add_user("faculty", 2, "Dr. Bob")

    assert len(admin.users) == 1
    assert isinstance(admin.users[0], Faculty)
    assert admin.users[0].name == "Dr. Bob"

def test_borrow_book():
    admin = Admin()
    admin.add_book(101, "Data Structures", 5)
    admin.add_user("student", 1, "Alice")

    admin.borrow_book(1, 101)
    assert admin.books[0].quantity == 4
    assert len(admin.users[0].borrowed_books) == 1

def test_borrow_book_user_not_found():
    admin = Admin()
    admin.add_book(101, "Data Structures", 5)

    with pytest.raises(UserNotFoundException):
        admin.borrow_book(999, 101)

def test_borrow_book_not_found():
    admin = Admin()
    admin.add_user("student", 1, "Alice")

    with pytest.raises(BookNotFoundException):
        admin.borrow_book(1, 999)

def test_return_book():
    admin = Admin()
    admin.add_book(101, "Data Structures", 5)
    admin.add_user("student", 1, "Alice")

    admin.borrow_book(1, 101)
    admin.return_book(1, 101)

    assert admin.books[0].quantity == 5
    assert len(admin.users[0].borrowed_books) == 0

def test_return_book_user_not_found():
    admin = Admin()
    admin.add_book(101, "Data Structures", 5)

    with pytest.raises(UserNotFoundException):
        admin.return_book(999, 101)

def test_return_book_not_found():
    admin = Admin()
    admin.add_user("student", 1, "Alice")

    with pytest.raises(BookNotFoundException):
        admin.return_book(1, 999)

def test_search_books_by_prefix():
    admin = Admin()
    admin.add_book(101, "Data Structures", 5)
    admin.add_book(102, "Database Systems", 3)

    books = admin.search_books_by_prefix("Data")
    assert len(books) == 2

    books = admin.search_books_by_prefix("Database")
    assert len(books) == 1
    assert books[0].name == "Database Systems"
