# CIS_40 MIDTERM 1 JOHNNY TO
# Burger Application Menu using functions

# GLOBAL VARIABLES
ITEM_1 = 5.25
ITEM_2 = 5.75
ITEM_3_To_5 = 5.95


def show_menu():
    # Show Menu
    print("BURGER CLUB MENU")
    print("--------------------------------------------------")
    print("1) De Anza Burger                            $5.25")
    print("2) Bacon Cheese                              $5.75")
    print("3) Mushroom Swiss                            $5.95")
    print("4) Western Burger                            $5.95")
    print("5) Don Cali Burger                           $5.95")
    print("--------------------------------------------------")
    print("0) END SELECTION")


def user_prompt_menu():
    # Selection is stored as a tuple
    # ALL ERROR CHECKS ARE HERE! (IF EVERYTHING HERE PASSES, THEN I DON'T NEED TO CHECK STUFF)
    EXCEPTION_CHECK_SELECTION = False
    QUANTITY_INPUT = False
    show_menu()
    while EXCEPTION_CHECK_SELECTION == False:
        try:
            selection = int(input("Welcome! What would you like? (INPUT):").strip())
            if selection >= 0 and selection <= 5:
                    if selection >0:
                        while QUANTITY_INPUT == False:
                                quantity = int(input("How much would you like? (INPUT):").strip())
                                if quantity >0:
                                    QUANTITY_INPUT = True
                                else:
                                    print("INVALID RES (QUANTITY IS NEGATIVE)")
                        EXCEPTION_CHECK_SELECTION = True
                    elif(selection == 0):
                        quantity = 0
                        EXCEPTION_CHECK_SELECTION = True
            else:
                print("INVALID RES (SELECTION IS OUT OF BOUNDS)")
        except:
            print("INVALID RESPONSE")
    return selection, quantity


def user_prompt_type():
    # Prompt the user for which type they are.
    # ERROR CHECK HERE!
        EXCEPTION_CHECK_TYPE = False
        while EXCEPTION_CHECK_TYPE == False:
            try:
                userType =input("Are you a staff member or a student? [STAFF] [STUDENT] (INPUT):").replace(" ", "").upper()
                if userType == "STAFF" or userType == "STUDENT":
                    EXCEPTION_CHECK_TYPE = True
                else:
                    print("INVALID RES (NOT ACCEPTABLE STRING)")
            except:
                print("INVALID RESPONSE")
        return (userType)


def compute_pay(user_type, order):
    # Given List with tuples and the Usertype, compute the pay.
    STAFF_TAX = 0.09
    Total_Price_Nontax = 0
    for userSelection in order:
        if userSelection[0] == 1:
            Total_Price_Nontax += ITEM_1*userSelection[1]
        if userSelection[0] == 2:
            Total_Price_Nontax += ITEM_2*userSelection[1]
        if userSelection[0]== 3 or userSelection[0]== 4 or userSelection[0]== 5 :
            Total_Price_Nontax += ITEM_3_To_5*userSelection[1]
        if user_type == "STAFF":
            Tax_Ammnt = Total_Price_Nontax*STAFF_TAX
            Total_Price = round(Total_Price_Nontax +(Tax_Ammnt),2)
        else:
            Tax_Ammnt = 0
            Total_Price = Total_Price_Nontax
    return Total_Price_Nontax,Tax_Ammnt,Total_Price


def print_receipt(user_type, total, order):
    # Print the receipt duh
    print("==================================================")
    print("DE ANZA BURGER CLUB RECEIPT")
    print("--------------------------------------------------")
    print("CUSTOMER TYPE: " + user_type)
    print("--------------------------------------------------")
    print("ITEM(S) PURCHASED")
    for userSelection in order:
        if userSelection[0] == 1:
            print("De Anza Burger                          $5.25")
            print("QUANTITY:                               x"+str(userSelection[1]))
            print("CHARGED:                                     $"+str(ITEM_1*userSelection[1]))
        if userSelection[0] == 2:
            print("Bacon Cheese                            $5.75")
            print("QUANTITY:                               x" + str(userSelection[1]))
            print("CHARGED:                                     $" + str(ITEM_2 * userSelection[1]))
        if userSelection[0] == 3:
            print("Mushroom Swiss                          $5.95")
            print("QUANTITY:                               x" + str(userSelection[1]))
            print("CHARGED:                                     $" + str(ITEM_3_To_5 * userSelection[1]))
        if userSelection[0] == 4:
            print("Western Burger                          $5.95")
            print("QUANTITY:                               x" + str(userSelection[1]))
            print("CHARGED:                                     $" + str(ITEM_3_To_5 * userSelection[1]))
        if userSelection[0] == 5:
            print("Don Cali Burger                         $5.95")
            print("QUANTITY:                               x" + str(userSelection[1]))
            print("CHARGED:                                     $" + str(ITEM_3_To_5 * userSelection[1]))
        print("----------------")
    print("==================================================")
    print("SUBTOTAL:                                    $" + str(round(total[0],2)))
    if user_type == "STAFF":
        print("TAX PERCENT:                                 %9")
    else:
        print("TAX PERCENT:                                 %0")
    print("TAX CHARGED:                                 $" + str(round(total[1],2)))
    print("TOTAL:                                       $" + str(round(total[2],2)))


def main():
    # Exit Code Trigger is a Flag that will stop the menu process and move to compute_pay/print_receipt
    # Store Selection Data into a List and append every time time selection is a value that isn't 0
    exit_code_trigger = False
    item_selection_exist = False
    userType = user_prompt_type()
    order = []
    while exit_code_trigger == False:
        user_selection1 = user_prompt_menu()
        if user_selection1[0] != 0:
            order.append(user_selection1)
            item_selection_exist = True
        else:
            exit_code_trigger = True
    if item_selection_exist:
        Total = compute_pay(userType, order)
        print_receipt(userType, Total, order)



main()

