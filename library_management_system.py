class Book:
    """Represents a book with a title, author, publication year, and borrow status."""
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False  # Tracks if the book is borrowed

    def borrow(self) -> bool:
        """Marks the book as borrowed if it's not already borrowed."""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self) -> None:
        """Marks the book as returned."""
        self.is_borrowed = False


class Library:
    """Represents a library that can manage a collection of books."""
    def __init__(self):
        self.books = []  # Stores the list of books in the library

    def add_book(self, book: Book) -> None:
        """Adds a new book to the library."""
        self.books.append(book)

    def display_books(self) -> None:
        """Displays all books in the library with their availability status."""
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Checked Out"
            print(f"{book.title} by {book.author} ({book.year}) - {status}")

    def borrow_book(self, title: str) -> None:
        """Allows a user to borrow a book if it's available."""
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"You have borrowed '{title}'.")
                    return
                else:
                    print(f"'{title}' is already borrowed.")
                    return
        print(f"'{title}' is not available in the library.")

    def return_book(self, title: str) -> None:
        """Allows a user to return a borrowed book."""
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.return_book()
                    print(f"You have returned '{title}'.")
                    return
                else:
                    print(f"'{title}' was not borrowed.")
                    return
        print(f"'{title}' is not found in the library.")


def main():
    """Main program to interact with the library system."""
    library = Library()

    # Adding some initial books to the library
    library.add_book(Book("Atomic Habits", "James Clear", 2018))
    library.add_book(Book("Python Crash Course", "Eric Matthes", 2023))

    while True:
        print("\nLibrary Menu")
        print("1: Display Books")
        print("2: Add Book")
        print("3: Borrow Book")
        print("4: Return Book")
        print("5: Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            library.display_books()
        elif choice == 2:
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            year = input("Enter publication year: ").strip()
            library.add_book(Book(title, author, year))
            print("Book added successfully!")
        elif choice == 3:
            title = input("Enter the title of the book to borrow: ").strip()
            library.borrow_book(title)
        elif choice == 4:
            title = input("Enter the title of the book to return: ").strip()
            library.return_book(title)
        elif choice == 5:
            print("Thank you for using the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
