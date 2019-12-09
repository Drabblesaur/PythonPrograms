from LibraryPatron import JuvenilePatron , AdultPatron
from LibaryBook import LibaryBook

book1 = LibaryBook("Alice in Wonderland", "Juvenile")
book2 = LibaryBook("The Cat in the Hat", "Juvenile")
book3 = LibaryBook("Harry Potter and the Sorcerer's Stone", "Juvenile")
book4 = LibaryBook("The Hobbit", "Juvenile")
book5 = LibaryBook("The Da Vinci Code", "Adult")
book6 = LibaryBook("The Girl with the Dragon Tattoo", "Adult")

patron1 = JuvenilePatron("Jimmy")
patron2 = AdultPatron("Sophia")

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

'''
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
'''