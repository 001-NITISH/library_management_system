class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.quantity > 0:
            self.borrowed_books.append(book)
            book.quantity -= 1
        else:
            raise Exception(f"No copies of {book.name} are available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.quantity += 1
        else:
            raise Exception(f"{self.name} has not borrowed {book.name}.")

    def __str__(self):
        return f'ID: {self.user_id}, Name: {self.name}'


class Student(User):
    MAX_BORROW_LIMIT = 3

    def borrow_book(self, book):
        if len(self.borrowed_books) < Student.MAX_BORROW_LIMIT:
            super().borrow_book(book)
        else:
            raise Exception(f"Student {self.name} has reached the maximum borrow limit.")


class Faculty(User):
    MAX_BORROW_LIMIT = 5

    def borrow_book(self, book):
        if len(self.borrowed_books) < Faculty.MAX_BORROW_LIMIT:
            super().borrow_book(book)
        else:
            raise Exception(f"Faculty {self.name} has reached the maximum borrow limit.")
