class Book:
    def __init__(self, book_id, name, quantity):
        self.book_id = book_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f'ID: {self.book_id}, Title: {self.name}, Quantity: {self.quantity}'
