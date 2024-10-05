import pytest
from models.user import Student, Faculty
from models.book import Book

def test_create_student():
    student = Student(1, "John Doe")
    assert student.user_id == 1
    assert student.name == "John Doe"
    assert len(student.borrowed_books) == 0

def test_student_borrow_book():
    student = Student(1, "John Doe")
    book = Book(101, "Python Programming", 2)

    student.borrow_book(book)
    assert len(student.borrowed_books) == 1
    assert book.quantity == 1

def test_student_borrow_limit():
    student = Student(1, "John Doe")
    book1 = Book(101, "Python Programming", 2)
    book2 = Book(102, "Java Programming", 2)
    book3 = Book(103, "C++ Programming", 2)
    book4 = Book(104, "Ruby Programming", 2)

    student.borrow_book(book1)
    student.borrow_book(book2)
    student.borrow_book(book3)

    with pytest.raises(Exception):
        student.borrow_book(book4)

def test_faculty_borrow_limit():
    faculty = Faculty(1, "Dr. Smith")
    book1 = Book(101, "Data Science", 2)
    book2 = Book(102, "Machine Learning", 2)
    book3 = Book(103, "AI", 2)
    book4 = Book(104, "Big Data", 2)
    book5 = Book(105, "Deep Learning", 2)
    book6 = Book(106, "Cloud Computing", 2)

    faculty.borrow_book(book1)
    faculty.borrow_book(book2)
    faculty.borrow_book(book3)
    faculty.borrow_book(book4)
    faculty.borrow_book(book5)

    with pytest.raises(Exception):
        faculty.borrow_book(book6)

def test_return_book():
    student = Student(1, "John Doe")
    book = Book(101, "Python Programming", 2)

    student.borrow_book(book)
    student.return_book(book)

    assert len(student.borrowed_books) == 0
    assert book.quantity == 2
