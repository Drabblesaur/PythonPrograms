#CIS_40 Johnny To
TAX_PERCENT = 0.075
Book_Price = float(input("BOOK PRICE:"))
Book_Ammnt = int(input("AMMOUNT OF BOOK(S):"))
Total_Book_Price = Book_Price*Book_Ammnt
Tax_Charged = TAX_PERCENT*Total_Book_Price
Shipping_Charge = 2*Book_Ammnt
Total_Price = Total_Book_Price+Tax_Charged+Shipping_Charge
print("Total Price:"+ str(Total_Price))

'''
OUTPUT
BOOK PRICE:10
AMMOUNT OF BOOK(S):10
Total Price:127.5
'''