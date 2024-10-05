from models.book import Book
from models.user import Student, Faculty
from models.admin import Admin
from utils.input_handlers import get_validated_input
from utils.display import display_books, display_users, display_borrowed_books

def main():
    admin = Admin()
    
    print("Predefined books in the library:")
    admin.print_books()

    while True:
        print("\nProgram Options:")
        print(" 1) Add book")
        print(" 2) Print library books")
        print(" 3) Print books by prefix")
        print(" 4) Add user")
        print(" 5) Borrow book")
        print(" 6) Return book")
        print(" 7) Print users borrowed book")
        print(" 8) Print users")
        print(" 9) Exit")

        choice = get_validated_input("Enter your choice from 1 to 9: ", int, range(1, 10))

        try:
            if choice == 1:
                book_id = get_validated_input("Enter the book id: ", int)
                name = input("Enter the book name: ")
                quantity = get_validated_input("Enter the book quantity: ", int)
                admin.add_book(book_id, name, quantity)
            elif choice == 2:
                display_books(admin.books)
            elif choice == 3:
                prefix = input("Enter the book name prefix: ")
                display_books(admin.search_books_by_prefix(prefix))
            elif choice == 4:
                user_type = input("Enter the user type (student/faculty): ").lower()
                user_id = get_validated_input("Enter the user id: ", int)
                name = input("Enter the user name: ")
                admin.add_user(user_type, user_id, name)
            elif choice == 5:
                user_id = get_validated_input("Enter the user id: ", int)
                book_id = get_validated_input("Enter the book id: ", int)
                admin.borrow_book(user_id, book_id)
            elif choice == 6:
                user_id = get_validated_input("Enter the user id: ", int)
                book_id = get_validated_input("Enter the book id: ", int)
                admin.return_book(user_id, book_id)
            elif choice == 7:
                user_id = get_validated_input("Enter the user id: ", int)
                display_borrowed_books(admin, user_id)
            elif choice == 8:
                display_users(admin.users)
            elif choice == 9:
                print("Exiting program.")
                break
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
