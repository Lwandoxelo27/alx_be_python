from library_management import Book, Library

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"'{self.title}' has been checked out."
        return f"'{self.title}' is already checked out."

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"'{self.title}' has been returned."
        return f"'{self.title}' is already available."


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self._books.append(new_book)
        return f"'{title}' by {author} has been added to the library."

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f"'{title}' is not available in the library."

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f"'{title}' is not available in the library."

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        return available_books
