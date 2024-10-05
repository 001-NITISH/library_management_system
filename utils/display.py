def display_books(books):
    if books:
        print("\nBooks in the library:")
        for book in books:
            print(book)
    else:
        print("No books available.")

def display_users(users):
    if users:
        print("\nRegistered users:")
        for user in users:
            print(user)
    else:
        print("No users registered.")

def display_borrowed_books(admin, user_id):
    user = admin.find_user_by_id(user_id)
    if user.borrowed_books:
        print(f"\n{user.name} has borrowed:")
        for book in user.borrowed_books:
            print(f'- {book.name}')
    else:
        print(f"{user.name} has not borrowed any books.")
