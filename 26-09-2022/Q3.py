# Create two classes:
# A:- Author: authorName ,age,place
# B:- Book: name ,price
# C:- relationship: Book has-an Author
# D:-add print method in Both class

class Author:
    def __init__(self, author_name, age, place):
        self.author_name = author_name
        self.age = age
        self.place = place

    def print_details(self):
        print(f"Name of the Author: {self.author_name}")
        print(f"Age of the Author: {self.age}")
        print(f"Place of the Author: {self.place}")


class Book:
    def __init__(self, name, price, author_name, age, place):
        self.name = name
        self.price = price
        self.author = Author(author_name, age, place)

    def print_details(self):
        print(f"Name of the Book: {self.name}")
        print(f"Price of the Book: {self.price} Rs")
        self.author.print_details()


Sapiens = Book('Sapiens', 500, "Yuval Noah Harari", '50', "Israel")
Sapiens.print_details()



