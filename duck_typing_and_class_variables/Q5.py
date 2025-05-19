"""Create a class Book with a class variable library = "City Library".
Create a book object and try to change library using the object
(e.g., book.library = "Community Library").
Print the library value using the object and 
the class name and explain why they are different."""


class Book:
    library = "City Library"

book1 = Book()

book1.library = "Community Library"

print(book1.library)
print(Book.library)


# print(book1.__dict__)

"""
When we assign book1.library = "Community Library", 
we are not modifying the class variable. Instead,
Python creates a new instance variable library for book1. 
This shadows the class variable. So, accessing book1.
library returns the instances value,
while Book.library still returns the original class value.
To modify a class variable, we should do:
Book.library = "New Library" instead of modifying through an instance."""