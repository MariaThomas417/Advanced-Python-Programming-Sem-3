
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_book(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print("ID: ",self.book_id)
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Status: ",status)
        


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display_patron(self):
        print("Patron ID: ",self.patron_id)
        print(f"Name: ",self.name)


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    def borrow_book(self, patron_id, book_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if not book.is_borrowed:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print("Book is already borrowed.")
    
    def return_book(self, patron_id, book_id):
        if book_id not in self.books or patron_id not in self.patrons:
            print("Invalid Book ID or Patron ID.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.title in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book.title)
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("This patron did not borrow this book.")

    def display_books(self):
        print("\nLibrary Books")
        for book in self.books.values():
            book.display_book()

    def display_patrons(self):
        print("\nRegistered Patrons")
        for patron in self.patrons.values():
            patron.display_patron()


library = Library()

book1 = Book(101, "Python Programming", "John Smith")
book2 = Book(102, "Data Structures", "Jane Doe")
book3 = Book(103, "Machine Learning", "Andrew Ng")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

patron1 = Patron(1, "Alice")
patron2 = Patron(2, "Bob")

library.register_patron(patron1)
library.register_patron(patron2)

library.borrow_book(1, 101)
library.borrow_book(2, 102)

library.return_book(1, 101)

library.display_books()
library.display_patrons()
