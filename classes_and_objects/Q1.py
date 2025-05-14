"""Create a class called Book that has title and author as attributes. 
Add a method show_details()
that prints the book's title and author."""

class Book:
    def __init__(self, title , author):
        self.title= title
        self.author = author

    def show_details(self):
        print(f"Titile of the book is {self.title} and the author is {self.author}")


book1= Book("habitat", "john welt")
book1.show_details()




            


