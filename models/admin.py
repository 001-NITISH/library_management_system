from .book import Book
from .user import Student, Faculty
from utils.exceptions import BookNotFoundException, UserNotFoundException

class Admin:
    def __init__(self):
        self.books = []
        self.users = []
        self._initialize_books()
        
    def _initialize_books(self):
        predefined_books = [
            {"book_id": 1, "name": "The Lord of the Rings", "quantity": 5},
            {"book_id": 2, "name": "Harry Potter", "quantity": 3},
            {"book_id": 3, "name": "Python Programming", "quantity": 4},
            {"book_id": 4, "name": "Data Structures and Algorithms", "quantity": 6},
            {"book_id": 5, "name": "Artificial Intelligence", "quantity": 2},
            {"book_id": 6, "name": "Machine Learning", "quantity": 3},
            {"book_id": 7, "name": "Database Management Systems", "quantity": 5},
            {"book_id": 8, "name": "Computer Networks", "quantity": 4},
            {"book_id": 9, "name": "Operating Systems", "quantity": 5},
            {"book_id": 10, "name": "Cloud Computing", "quantity": 3},
            {"book_id": 11, "name": "Deep Learning", "quantity": 4},
            {"book_id": 12, "name": "Software Engineering", "quantity": 2},
            {"book_id": 13, "name": "Data Science", "quantity": 3},
            {"book_id": 14, "name": "Distributed Systems", "quantity": 2},
            {"book_id": 15, "name": "Cryptography and Network Security", "quantity": 4},
        ]
        
        for book in predefined_books:
            self.add_book(book["book_id"], book["name"], book["quantity"])

    def add_book(self, book_id, name, quantity):
        for book in self.books:
            if book.book_id == book_id:
                raise Exception(f"Book with ID {book_id} already exists.")
        new_book = Book(book_id, name, quantity)
        self.books.append(new_book)
        print(f'Book "{name}" added successfully.')

    def print_books(self):
        """Print all books in the library."""
        if not self.books:
            print("No books available in the library.")
            return
        
        print("Books available in the library:")
        for book in self.books:
            print(f'ID: {book.book_id}, Title: "{book.name}", Quantity: {book.quantity}')

    def add_user(self, user_type, user_id, name):
        for user in self.users:
            if user.user_id == user_id:
                raise Exception(f"User with ID {user_id} already exists.")
        
        if user_type == 'student':
            new_user = Student(user_id, name)
        elif user_type == 'faculty':
            new_user = Faculty(user_id, name)
        else:
            raise Exception("Invalid user type. Choose 'student' or 'faculty'.")
        
        self.users.append(new_user)
        print(f'User "{name}" added successfully.')

    def borrow_book(self, user_id, book_id):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)

        if user and book:
            user.borrow_book(book)
            print(f'Book "{book.name}" borrowed successfully by {user.name}.')

    def return_book(self, user_id, book_id):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)

        if user and book:
            user.return_book(book)
            print(f'Book "{book.name}" returned successfully by {user.name}.')

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        raise BookNotFoundException(book_id)

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise UserNotFoundException(user_id)

    def search_books_by_prefix(self, prefix):
        return [book for book in self.books if book.name.startswith(prefix)]
