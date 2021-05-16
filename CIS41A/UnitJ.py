"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit J In-Class Assignment

"""
import LibraryBook
import LibraryPatron


def main():
    book1 = LibraryBook.Book("Alice in Wonderland", "Juvenile")
    book2 = LibraryBook.Book("The Cat in the Hat", "Juvenile")
    book3 = LibraryBook.Book("Harry Potter and the Sorcerer's Stone", "Juvenile")
    book4 = LibraryBook.Book("The Hobbit", "Juvenile")
    book5 = LibraryBook.Book("The Da Vinci Code", "Adult")
    book6 = LibraryBook.Book("The Girl with the Dragon Tattoo", "Adult")

    patron1 = LibraryPatron.JuvenilePatron("Jimmy")
    patron2 = LibraryPatron.AdultPatron("Sophia")

    patron1.checkOutBook(book6)
    patron1.checkOutBook(book1)
    patron1.checkOutBook(book2)
    patron1.printCheckedOutBooks()
    patron1.checkOutBook(book3)
    patron1.returnBook(book1)
    patron1.checkOutBook(book3)
    patron1.printCheckedOutBooks()
    patron2.checkOutBook(book5)
    patron2.checkOutBook(book4)
    patron2.printCheckedOutBooks()


if __name__ == '__main__':
    main()

"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/UnitJ.py
Sorry Jimmy The Girl with the Dragon Tattoo is an adult book
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2 books
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out:
The Da Vinci Code
The Hobbit

Process finished with exit code 0

"""