# CIS40 -Chapter 4 Excercise 2, Johnny To
# Computes Pay by user input (Hours and Pay Rate)
# Includes a +40 hours worked logic
# Includes logic and while loop.
from random import randint
def reportMaker(name,Hours,Remainder_Hours,Pay_Rate,OVERTIME_PAY_RATE,pay) :
                    Doc_Num = randint(1000,2000)
                    print("----------------------")
                    print(name.upper() + " PAY REPORT DOC:" +str(Doc_Num))
                    print("TOTAL HOURS:"+ str(Hours + Remainder_Hours))
                    print("PAY RATE:"+ str(Pay_Rate))
                    if Hours >= 40:
                        print("OVERTIME PAY RATE:"+ str(OVERTIME_PAY_RATE))
                    print("Your Pay is:", pay) 

EXCEPTION_CHECK = False
name = input("Company name:")
while EXCEPTION_CHECK == False :
    try:
        Hours = round(float(input("Enter Hours Worked:").strip()),2)
        if Hours > 0 :
            try:
                Pay_Rate = round(float(input("Enter Pay Rate:").strip()),2)
                if Pay_Rate > 0 :
                    OVERTIME_PAY_RATE = round(Pay_Rate * 1.5,2)
                    Remainder_Hours = 0
                    if Hours >= 40:
                        print("Worked 40+ Hours")
                        Remainder_Hours = Hours - 40
                        Hours = 40                
                    pay = round((Hours * Pay_Rate) + (Remainder_Hours * (OVERTIME_PAY_RATE)),2)
                    reportMaker(name,Hours,Remainder_Hours,Pay_Rate,OVERTIME_PAY_RATE,pay)
                    EXCEPTION_CHECK = True
                else :
                    print("PAY RATE IS NEGATIVE")
            except :
                print ("INVALID RATE")            
        else:
            print ("HOURS ARE NEGATIVE")
    except:
        print("INVALID HOURS")    

'''
VALID ANS
Company name:Facebook
Enter Hours Worked:45
Enter Pay Rate:10
Worked 40+ Hours
----------------------
FACEBOOK PAY REPORT DOC:1102
TOTAL HOURS:45.0
PAY RATE:10.0
OVERTIME PAY RATE:15.0
Your Pay is: 475.0

Company name:Google
Enter Hours Worked:20
Enter Pay Rate:10
----------------------
GOOGLE PAY REPORT DOC:1414
TOTAL HOURS:20.0
PAY RATE:10.0
Your Pay is: 200.0

Company name:Nintendo
Enter Hours Worked:     35
Enter Pay Rate:     20
----------------------
NINTENDO PAY REPORT DOC:1187
TOTAL HOURS:35.0
PAY RATE:20.0
Your Pay is: 700.0

Company name:Googl
Enter Hours Worked:10.12345
Enter Pay Rate:10.365
----------------------
GOOGL PAY REPORT DOC:1752
TOTAL HOURS:10.12
PAY RATE:10.37
Your Pay is: 104.94

INVALID ANS

Company name:Facebook
Enter Hours Worked:-30
HOURS ARE NEGATIVE
Enter Hours Worked:45
Enter Pay Rate:-20
PAY RATE IS NEGATIVE
Enter Hours Worked:35
Enter Pay Rate:1
----------------------
FACEBOOK PAY REPORT DOC:1546
TOTAL HOURS:35.0
PAY RATE:1.0
Your Pay is: 35.0

Company name:Google
Enter Hours Worked:hello
INVALID HOURS
Enter Hours Worked:45
Enter Pay Rate:hello
INVALID RATE
Enter Hours Worked:45
Enter Pay Rate:10
Worked 40+ Hours
----------------------
GOOGLE PAY REPORT DOC:1030
TOTAL HOURS:45.0
PAY RATE:10.0
OVERTIME PAY RATE:15.0
Your Pay is: 475.0

'''

