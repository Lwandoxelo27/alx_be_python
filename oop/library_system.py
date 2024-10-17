class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (EBook, {self.file_size} MB)"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (PrintBook, {self.page_count} pages)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (EBook, {self.file_size} MB)"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (PrintBook, {self.page_count} pages)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


from library_system import Book, EBook, PrintBook, Library

def main():
    library = Library()

    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    ebook1 = EBook("1984", "George Orwell", 5)
    printbook1 = PrintBook("Pride and Prejudice", "Jane Austen", 300)

    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)

    print("Library Catalog:")
    library.list_books()

if __name__ == "__main__":
    main()
