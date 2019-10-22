#CIS 40 Final Johnny To
#Order Class
import datetime
import time
class Order:
    """
    CLASS: ORDER
    ATTRIBUTES:
        customerType (String)
        priceBtax (Float)
        priceAtax (Float)
        priceCtax (Float)
        tax (Float)
        priceMenu (Dictionary)
        order (Dictionary)
        pricePerItem (Dictionary)
    """
    def __init__(self):
        """
        CONSTRUCTOR:
        - No parameters (All private VARS)
        """
        self.__customerType = "NULL"
        self._priceBtax = 0
        self._priceAtax = 0
        self._priceCtax = 0
        self._tax = 0
        self.__priceMenu = {"De Anza Burger": 5.25, "Bacon Cheese": 5.75,
                            "Mushroom Swiss": 5.95, "Western Burger": 5.95,
                            "Don Cali Burger": 5.95}
        self.__order = {"De Anza Burger": 0, "Bacon Cheese": 0,
                        "Mushroom Swiss": 0, "Western Burger": 0,
                        "Don Cali Burger": 0}
        self._pricePerItem = {"De Anza Burger": 0.0, "Bacon Cheese": 0.0,
                        "Mushroom Swiss": 0.0, "Western Burger": 0.0,
                        "Don Cali Burger": 0.0}

    def display_menu(self):
        """
        METHOD
        Prints the Menu

        :return NONE
        """
        __menuNum = 1
        print("BURGER CLUB MENU")
        print("--------------------------------------------------")
        for key in self.__priceMenu:
            print("{a}.{b:15s}{c:8.2f}".format(a=__menuNum, b=key, c=self.__priceMenu[key]))
            __menuNum += 1
        print("--------------------------------------------------")
        print("0) END SELECTION")

    def prompt_menu(self):
        """
        METHOD
        Prompt the User for their selection and adds the quantity to order (VAR)
        :return: NONE
        """
        Exit_Code = False
        while Exit_Code == False:
            EXCEPTION_CHECK_SELECTION = False
            QUANTITY_INPUT = False
            while EXCEPTION_CHECK_SELECTION == False:
                try:
                    selection = int(input("Welcome! What would you like? (INPUT):").strip())
                    if selection >= 0 and selection <= 5:
                        if selection > 0:
                            while QUANTITY_INPUT == False:
                                quantity = int(input("How much would you like? (INPUT):").strip())
                                if quantity > 0:
                                    QUANTITY_INPUT = True
                                else:
                                    print("INVALID RES (QUANTITY IS NEGATIVE)")
                            EXCEPTION_CHECK_SELECTION = True
                        elif (selection == 0):
                            quantity = 0
                            EXCEPTION_CHECK_SELECTION = True
                            Exit_Code = True
                    else:
                        print("INVALID RES (SELECTION IS OUT OF BOUNDS)")
                except:
                    print("INVALID RESPONSE")
            if selection == 1:
                self.__order["De Anza Burger"] += quantity
            if selection == 2:
                self.__order["Bacon Cheese"] += quantity
            if selection == 3:
                self.__order["Mushroom Swiss"] += quantity
            if selection == 4:
                self.__order["Western Burger"] += quantity
            if selection == 5:
                self.__order["Don Cali Burger"] += quantity

    def prompt_type(self):
        """
        METHOD
        Prompt the user for their type status (STAFF / STUDENT)
        :return: NONE
        """
        EXCEPTION_CHECK_TYPE = False
        while EXCEPTION_CHECK_TYPE == False:
            try:
                self.__customerType = input("Are you a staff member or a student? [STAFF] [STUDENT] (INPUT):").replace(
                    " ",
                    "").upper()
                if self.__customerType == "STAFF" or self.__customerType == "STUDENT":
                    EXCEPTION_CHECK_TYPE = True
                else:
                    print("INVALID RES (NOT ACCEPTABLE STRING)")
            except TypeError:
                print("INVALID RESPONSE")

    def calculate(self):
        """
        METHOD
        Calculate the data (Fills: priceBtax, priceAtax, priceCtax, and tax )
        - Internal VAR: STAFF_TAX = 0.09
        :return: NONE
        """
        __STAFF_TAX = 0.09
        for key in self.__priceMenu:
            self._pricePerItem[key] = self.__order[key]*self.__priceMenu[key]
            self._priceBtax += self.__order[key]*self.__priceMenu[key]
        if self.__customerType == "STAFF":
            self._tax = __STAFF_TAX
        self._priceCtax = self._priceBtax * self._tax
        self._priceAtax = self._priceBtax + self._priceCtax
        self.__purge_data()

    def __purge_data(self):
        """
        METHOD
        SHOULD NOT BE CALLED
        calculate() auto calls __purge_data()
        Cleans up Dictionaries order{} and pricePerItem{} for printing

        :return: NONE
        """
        deleteList = []
        for key in self.__order:
            if self.__order[key] == 0:
                deleteList.append(key)
        for delValue in deleteList:
            self.__order.pop(delValue, None)
            self._pricePerItem.pop(delValue, None)

    def print_bill(self):
        """
        METHOD
        prints the Bill
        :return: NONE
        """
        __orderNum = 1
        print("==================================================")
        print("DE ANZA BURGER CLUB RECEIPT")
        print("--------------------------------------------------")
        print("CUSTOMER TYPE: " + self.__customerType)
        print("--------------------------------------------------")
        print("ITEM(S) PURCHASED")
        print("NAME              AMMNT            PRICE   CHARGED")
        print("--------------------------------------------------")
        for key in self.__order:
            print("{a}.{b:15s} {c}                ${d:1.2F}    ${e:1.2f}".format(a=__orderNum, b=key, c=self.__order[key],
                                                               d=self.__priceMenu[key],e=self._pricePerItem[key]))
            __orderNum += 1
        print("==================================================")
        print("SUBTOTAL:                                   ${a:1.2F}".format(a=self._priceBtax))
        if self.__customerType == "STAFF":
            print("TAX PERCENT:                                %9")
            print("TAX CHARGED:                                ${a:1.2F}".format(a=self._priceCtax))
        else:
            print("TAX PERCENT:                                %0")
        print("TOTAL:                                      ${a:1.2F}".format(a=self._priceAtax))

    def save_to_file(self):
        """
        METHOD
        Writes a bill to a Timestamped file.
        :return: NONE
        """
        __orderNum = 1
        timeStamp = time.time()
        billTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
        billTimeStamp = billTimeStamp + '.txt'
        with open(billTimeStamp, 'w') as bill:
            bill.write("==================================================\n")
            bill.write("DE ANZA BURGER CLUB RECEIPT\n")
            bill.write("--------------------------------------------------\n")
            bill.write("CUSTOMER TYPE: " + self.__customerType+"\n")
            bill.write("--------------------------------------------------\n")
            bill.write("ITEM(S) PURCHASED\n")
            bill.write("NAME              AMMNT            PRICE   CHARGED\n")
            bill.write("--------------------------------------------------\n")
            for key in self.__order:
                bill.write("{a}.{b:15s} {c}                ${d:1.2F}    ${e:1.2f}\n".format(a=__orderNum, b=key,
                                                                                     c=self.__order[key],
                                                                                     d=self.__priceMenu[key],
                                                                                     e=self._pricePerItem[key]))
                __orderNum += 1
            bill.write("==================================================\n")
            bill.write("SUBTOTAL:                                   ${a:1.2F}\n".format(a=self._priceBtax))
            if self.__customerType == "STAFF":
                bill.write("TAX PERCENT:                                %9\n")
                bill.write("TAX CHARGED:                                ${a:1.2F}\n".format(a=self._priceCtax))
            else:
                bill.write("TAX PERCENT:                                %0\n")
            bill.write("TOTAL:                                      ${a:1.2F}\n".format(a=self._priceAtax))