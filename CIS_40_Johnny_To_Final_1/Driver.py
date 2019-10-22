#CIS 40 Final Johnny To
#Driver Code to Demo Order class
from CIS_40_Johnny_To_Final_1 import Order

if  __name__ == "__main__":

     while True:
         order = Order()
         order.display_menu()
         order.prompt_type()
         order.prompt_menu()
         order.calculate()
         order.print_bill()
         order.save_to_file()

         help(order)

         userInputToContinue = input("Continue for another order(Any keys= Yes, n= No)?")

         if userInputToContinue.lower() == 'n':

              print("The system is shutting down!")
              break
'''
OUTPUT(Negative)
BURGER CLUB MENU
--------------------------------------------------
1.De Anza Burger     5.25
2.Bacon Cheese       5.75
3.Mushroom Swiss     5.95
4.Western Burger     5.95
5.Don Cali Burger    5.95
--------------------------------------------------
0) END SELECTION
Are you a staff member or a student? [STAFF] [STUDENT] (INPUT):0
INVALID RES (NOT ACCEPTABLE STRING)
Are you a staff member or a student? [STAFF] [STUDENT] (INPUT):hello
INVALID RES (NOT ACCEPTABLE STRING)
Are you a staff member or a student? [STAFF] [STUDENT] (INPUT):staff
Welcome! What would you like? (INPUT):-5
INVALID RES (SELECTION IS OUT OF BOUNDS)
Welcome! What would you like? (INPUT):40
INVALID RES (SELECTION IS OUT OF BOUNDS)
Welcome! What would you like? (INPUT):1
How much would you like? (INPUT):0
INVALID RES (QUANTITY IS NEGATIVE)
How much would you like? (INPUT):2
Welcome! What would you like? (INPUT):4
How much would you like? (INPUT):5
Welcome! What would you like? (INPUT):0
==================================================
DE ANZA BURGER CLUB RECEIPT
--------------------------------------------------
CUSTOMER TYPE: STAFF
--------------------------------------------------
ITEM(S) PURCHASED
NAME              AMMNT            PRICE   CHARGED
--------------------------------------------------
1.De Anza Burger  2                $5.25    $10.50
2.Western Burger  5                $5.95    $29.75
==================================================
SUBTOTAL:                                   $40.25
TAX PERCENT:                                %9
TAX CHARGED:                                $3.62
TOTAL:                                      $43.87

OUTPUT(Positive)
BURGER CLUB MENU
--------------------------------------------------
1.De Anza Burger     5.25
2.Bacon Cheese       5.75
3.Mushroom Swiss     5.95
4.Western Burger     5.95
5.Don Cali Burger    5.95
--------------------------------------------------
0) END SELECTION
Are you a staff member or a student? [STAFF] [STUDENT] (INPUT):student
Welcome! What would you like? (INPUT):1
How much would you like? (INPUT):1
Welcome! What would you like? (INPUT):2
How much would you like? (INPUT):1
Welcome! What would you like? (INPUT):3
How much would you like? (INPUT):1
Welcome! What would you like? (INPUT):4
How much would you like? (INPUT):1
Welcome! What would you like? (INPUT):5
How much would you like? (INPUT):1
Welcome! What would you like? (INPUT):0
==================================================
DE ANZA BURGER CLUB RECEIPT
--------------------------------------------------
CUSTOMER TYPE: STUDENT
--------------------------------------------------
ITEM(S) PURCHASED
NAME              AMMNT            PRICE   CHARGED
--------------------------------------------------
1.De Anza Burger  1                $5.25    $5.25
2.Bacon Cheese    1                $5.75    $5.75
3.Mushroom Swiss  1                $5.95    $5.95
4.Western Burger  1                $5.95    $5.95
5.Don Cali Burger 1                $5.95    $5.95
==================================================
SUBTOTAL:                                   $28.85
TAX PERCENT:                                %0
TOTAL:                                      $28.85
'''