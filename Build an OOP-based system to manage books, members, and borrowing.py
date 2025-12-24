#  Book Class 
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_book(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"ID: {self.book_id} | {self.title} by {self.author} | {status}")


# Member Class
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def display_member(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print("No books borrowed.")


# Library Class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    # Add book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    # Add member
    def add_member(self, member):
        self.members.append(member)
        print("Member added successfully.")

    # Display all books
    def show_books(self):
        print(f"\n--- {self.name} Book List ---")
        for book in self.books:
            book.display_book()

    # Display all members
    def show_members(self):
        print("\n--- Members List ---")
        for member in self.members:
            member.display_member()

    # Borrow book
    def borrow_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return
        if not book.is_available:
            print("Book is already borrowed.")
            return

        book.is_available = False
        member.borrow_book(book)
        print(f"{member.name} borrowed '{book.title}'")

    # Return book
    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not member or not book:
            print("Invalid member or book.")
            return
        if book not in member.borrowed_books:
            print("This book was not borrowed by the member.")
            return

        book.is_available = True
        member.return_book(book)
        print(f"{member.name} returned '{book.title}'")


# Using the System 
library = Library("City Central Library")

# Add books
book1 = Book(101, "Python Programming", "Guido van Rossum")
book2 = Book(102, "Clean Code", "Robert C. Martin")
book3 = Book(103, "Data Structures", "Mark Allen Weiss")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add members
member1 = Member(1, "Rachit")
member2 = Member(2, "Aman")

library.add_member(member1)
library.add_member(member2)

# Display data
library.show_books()
library.show_members()

# Borrow & Return operations
library.borrow_book(1, 101)
library.borrow_book(2, 102)

library.show_books()
library.show_members()

library.return_book(1, 101)

library.show_books()
library.show_members()
