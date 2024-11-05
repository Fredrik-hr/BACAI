# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:21:45 2024

@author: Mathi
"""

class Book: 
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def printBook(self):
        return f"Book Title: {self.title} the author is {self.author} and the book was released: {self.year}"



class Library: 
    
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []
        
    def add_book(self, book):
             self.available_books.append(book)
        
    def borrow_book(self, title):
        for book in self.available_books:
            if book.title == title:
                self.available_books.remove(book)
                self.borrowed_books.append(book)
                return f"{title} has been borrowed."
        return f"{title} is not available."

    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title == title:
                self.borrowed_books.remove(book)
                self.available_books.append(book)
                return f"{title} has been returned."
        return f"{title} was not borrowed from this library."

    def list_available_books(self):
        for book in self.available_books:
            print(book.printBook())
            
def main():
    library = Library()
    library.add_book(Book("Book Title 1", "Author 1", 2021))
    library.add_book(Book("Book Title 2", "Author 2", 2020))

    while True:
        print("\nPlease make a selection:")
        print("1 - List available books")
        print("2 - Borrow a book")
        print("3 - Return a book")
        print("q - Quit")
        choice = input("Enter your choice: ").lower()

        if choice == "q":
            print("Exiting program.")
            break
        elif choice == "1":
            library.list_available_books()
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            print(library.borrow_book(title))
        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            print(library.return_book(title))
        else:
            print("Invalid choice, please try again.")
main()
