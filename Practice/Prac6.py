#CREATING A CLASS WHICH CONTAINS THE NAME OF BOOKS AND WILL STORE THEIR NAMES

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showinfo(self):
        print(f"The Library has {self.no_of_books} Books. \nBooks are: ")
        for book in self.books:
            print(book)


lib = Library()
lib.addbook("Wings of Fire")
lib.addbook("Harry Potter")
lib.addbook("Dragon Ball")
lib.addbook("Bleach")
lib.addbook("Attack on Titan")
lib.showinfo()