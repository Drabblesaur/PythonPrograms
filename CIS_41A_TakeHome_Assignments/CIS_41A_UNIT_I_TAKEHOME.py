'''
Johnny To
CIS 41A   Fall 2019
Unit I take-home assignment
'''

# The LibraryPatron class has the following four methods: __init__, checkOutBook, returnBook, and printCheckedOutBooks.
class LibraryPatron:
    # The __init__ method should have the parameters self and name, and should store the name as an attribute (name is the name of the patron). 
    # There should also be an additional attribute called booksCheckedOut which should be initialized as an empty list. 
    def __init__(self,name):
        self.name = name
        self.booksCheckedOut = []
    # The checkOutBook method should have the parameters self, checkOutLimit and bookTitle. 
    def checkOutBook(self, checkOutLimit, bookTitle):
        if len(self.booksCheckedOut) >= checkOutLimit:
            # If the patron is at their checkout limit, print a "Sorry" message to the patron. 
            print("Sorry", self.name,'you are at your limit of',checkOutLimit,'books')
        else:
            # Otherwise, append the bookTitle to the patron's booksCheckedOut list and print a "Checkout" message, as shown below.
            self.booksCheckedOut.append(bookTitle)
            print(self.name, "has checked out" ,bookTitle)
    # The returnBook method should have the parameters self and book.
    def returnBook(self,book):
        # You will need to extract the book title from the list. 
        # Remove the book title from the patron's list of checked out book titles and print a "returned" message.
        self.booksCheckedOut.remove(book[0])
        print(self.name,"has returned",book[0])
    # The printCheckedOutBooks method should have the parameter self.
    def printCheckedOutBooks(self):
        # Print a message along and print all the patron's checked out book titles, as shown below.
        print(self.name,"has the following books checked out:")
        for i in self.booksCheckedOut:
            print(i)

# The AdultPatron class inherits from the LibraryPatron class and has the following two methods: __init__, checkOutBook.
class AdultPatron(LibraryPatron):
    # The __init__ method should have the parameters self and name. 
    def __init__(self,name):
        # Call LibraryPatron's __init__ to store the name. 
        LibraryPatron.__init__(self, name)
        # There should also be an additional attribute called checkOutLimit which should be initialized with a value of 4.
        self.checkOutLimit=4
    # The checkOutBook method should have the parameters self and book.
    def checkOutBook(self,book):
        # Call LibraryPatron's checkOutBook method, using the patron's checkOutLimit and the book title as arguments.
        LibraryPatron.checkOutBook(self, self.checkOutLimit, book[0])

# The JuvenilePatron class inherits from the LibraryPatron class and has the following two methods: __init__, checkOutBook.
class JuvenilePatron(LibraryPatron):
    # The __init__ method should have the parameters self and name.
    def __init__(self,name):
        # Call LibraryPatron's __init__ to store the name. 
        LibraryPatron.__init__(self,name)
        # There should also be an additional attribute called checkOutLimit which should be initialized with a value of 2.
        self.checkOutLimit=2
    # The checkOutBook method should have the parameters self and book. 
    def checkOutBook(self,book):
        # If the book is not a a juvenile book, print a "Sorry" message as shown below.
        if book[1]!="Juvenile":
            print("Sorry",self.name,book[0],"is an adult book")
        else:
            # call LibraryPatron's checkOutBook method, using the patron's checkOutLimit and the book title as arguments.
            LibraryPatron.checkOutBook(self,self.checkOutLimit,book[0])

# Test with the following code:
book1 = ["Alice in Wonderland", "Juvenile"]
book2 = ["The Cat in the Hat", "Juvenile"]
book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
book4 = ["The Hobbit", "Juvenile"]
book5 = ["The Da Vinci Code", "Adult"]
book6 = ["The Girl with the Dragon Tattoo", "Adult"]

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
Execution Results:
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