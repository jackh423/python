"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit J In-Class Assignment

"""
class LibraryPatron:

    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = []

    def checkOutBook(self, checkOutLimit, book):
        # print(f"I am in checkoutBoot {book}")
        if len(self.booksCheckedOut) >= checkOutLimit:
            print(f"Sorry {self.name} you are at your limit of {checkOutLimit} books")
        else:
            # print(f"I am in else")
            self.booksCheckedOut.append(book)
            print(f"{self.name} has checked out {book.title}")

    def returnBook(self, book):
        self.booksCheckedOut.remove(book)
        print(f"{self.name} has returned {book.title}")

    def printCheckedOutBooks(self):
        print(f"{self.name} has the following books checked out:")
        for ele in self.booksCheckedOut:
            print(ele.title)


class AdultPatron(LibraryPatron):

    def __init__(self, name):
        LibraryPatron.__init__(self, name)
        self.checkOutLimit = 4

    def checkOutBook(self, book):
        LibraryPatron.checkOutBook(self, self.checkOutLimit, book)


class JuvenilePatron(LibraryPatron):

    def __init__(self, name):
        LibraryPatron.__init__(self, name)
        self.checkOutLimit = 2

    def checkOutBook(self, book):
        if book.bookType != "Juvenile":
            print(f"Sorry {self.name} {book.title} is an {book.bookType.lower()} book")
        else:
            # print("I am on LibraryPatron.checkOutBook method")
            LibraryPatron.checkOutBook(self, self.checkOutLimit, book)
