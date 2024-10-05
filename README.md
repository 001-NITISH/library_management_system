# Library Management System

The Library Management System is a Python-based command-line application designed to streamline library operations. It utilizes object-oriented programming (OOP) principles to manage books, users, and borrowing activities efficiently.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Library Management System simplifies library tasks through a user-friendly interface. It includes three main classes:

- **Book**: Represents a book in the library.
- **User**: Represents a library user.
- **Admin**: Manages the library system and provides various functionalities.

### Example Usage:

```plaintext
Program Options:
 1) Add book
 2) Print library books
 3) Print books by prefix
 4) Add user
 5) Borrow book
 6) Return book
 7) Print users borrowed book
 8) Print users

Enter your choice from 1 to 8: 1

Please Enter the book id: 100
Please Enter the book name: The Lord of the Rings
Please Enter the book quantity: 3

Book is added successfully!
```

## Features

- **Add Books**: Easily add new books to the library with unique IDs.
- **Manage Users**: Add new users to the system for tracking borrowing activities.
- **Search Books**: Search for books by name using a prefix.
- **Borrow and Return**: Borrow books from the library and return them when done.
- **Track Borrowers**: Keep track of users who have borrowed books.
- **User Interface**: Simple command-line interface for user interaction.


## Installation

To set up the Library Management System on your local machine, follow these steps:

1. **Clone the Repository**: Start by cloning the repository to your local machine using the following command:
    ```bash
    git clone https://github.com/yourusername/library_management_system.git
    ```

2. **Navigate to the Project Directory**: Change into the project directory:
    ```bash
    cd library_management_system
    ```

3. **Install Dependencies**: If your project has any dependencies (none are required for this project), you can install them using:
    ```bash
    pip install -r requirements.txt
    ```

    *Note: If there is no `requirements.txt` file, you can skip this step.*

4. **Run the Application**: You are now ready to run the Library Management System. Use the following command:
    ```bash
    python main.py
    ```

Follow the on-screen prompts to manage your library.


## Contributing
Contributions are welcome! If you would like to contribute, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


### Summary
- Make sure to correctly open and close your code blocks.
- For plaintext, use the same triple backticks format as for code, just specify `plaintext` right after the opening backticks if desired.
  
Feel free to ask if you have any more questions or need further assistance!
