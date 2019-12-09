# ONLY FOR UNIT J

class LibraryPatron:
    def __init__(self,name):
        self.name = name
        self.booksCheckedOut = []
    def checkOutBook(self, checkOutLimit, bookTitle):
        if len(self.booksCheckedOut) >= checkOutLimit:
            print("Sorry", self.name,'you are at your limit of',checkOutLimit,'books')
        else:
            self.booksCheckedOut.append(bookTitle)
            print(self.name, "has checked out" ,bookTitle)
    def returnBook(self,book):
        self.booksCheckedOut.remove(book.title)
        print(self.name,"has returned",book.title)
    def printCheckedOutBooks(self):
        print(self.name,"has the following books checked out:")
        for i in self.booksCheckedOut:
            print(i)
class AdultPatron(LibraryPatron):
    def __init__(self,name):
        LibraryPatron.__init__(self, name)
        self.checkOutLimit=4
    def checkOutBook(self,book):
        LibraryPatron.checkOutBook(self, self.checkOutLimit, book.title)

class JuvenilePatron(LibraryPatron):
    def __init__(self,name):
        LibraryPatron.__init__(self,name)
        self.checkOutLimit=2
    def checkOutBook(self,book):
        if book.bookType !="Juvenile":
            print("Sorry",self.name,book.title,"is an adult book")
        else:
            LibraryPatron.checkOutBook(self,self.checkOutLimit,book.title)