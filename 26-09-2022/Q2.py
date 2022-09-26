# Define a Book class with the following attributes: Title, Author (Full name), Price.
# A:- Define a constructor used to initialize the attributes of the method with values entered by
# the user.
# B:-The View() method to display information for the current book.
# C:-Write a program to testing the Book class.


title = input("Enter the Title of the Book: ")
author = input("Enter the Author of the Book: ")
price = float(input("Enter the Price of the Book: "))


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def View(self):
        print(f"Title of the Book is {self.title}")
        print(f"Author (Full name) of the Book is {self.author}")
        print(f"Price of the Book is {self.price} Rs")


book = Book(title, author, price)
book.View()
