class Book:
    def __init__(self, book_id, book_name, book_title, book_author, available=True):
        self.book_id = book_id
        self.book_name = book_name
        self.book_title = book_title
        self.book_author = book_author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True

    def __repr__(self):
        status = "Available" if self.available else "Not Available"
        return f"ID: {self.book_id}, Name: {self.book_name}, Title: {self.book_title}, Author: {self.book_author}, Status: {status}"


class Library:
    book_list = []

    @classmethod
    def add_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def show_books(cls):
        if not cls.book_list:
            print("No books in the library!")
        else:
            for book in cls.book_list:
                print(book)

    @classmethod
    def borrow_book(cls, book_id):
        for book in cls.book_list:
            if book.book_id == book_id:
                if book.borrow():
                    print(f"Book '{book.book_name}' borrowed successfully!")
                else:
                    print(f"Book '{book.book_name}' is already borrowed.")
                return
        print(f"No book found with ID: {book_id}")

    @classmethod
    def return_book(cls, book_id):
        for book in cls.book_list:
            if book.book_id == book_id:
                book.return_book()
                print(f"Book '{book.book_name}' returned successfully!")
                return
        print(f"No book found with ID: {book_id}")


# Menu-driven system
while True:
    print("\n1. Enter a new book")
    print("2. Show all books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        book_name = input("Enter book name: ")
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        new_book = Book(book_id, book_name, book_title, book_author)
        Library.add_book(new_book)
        print("\nBook added successfully!")

    elif choice == 2:
        print("\nBooks in the library:")
        Library.show_books()

    elif choice == 3:
        book_id = int(input("Enter the book ID to borrow: "))
        Library.borrow_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter the book ID to return: "))
        Library.return_book(book_id)

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
