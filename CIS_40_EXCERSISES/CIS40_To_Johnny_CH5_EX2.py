#CIS_40 Johnny To
# Return pay using checked user input (hours & input)
# Uses Functions
def get_input():
        EXCEPTION_CHECK = False
        while EXCEPTION_CHECK == False :
                try:
                        Hours = round(float(input("Enter Hours Worked:").strip()),2)
                        if Hours > 0 :
                                try:
                                        Pay_Rate = round(float(input("Enter Pay Rate:").strip()),2)
                                        if Pay_Rate > 0 :
                                                EXCEPTION_CHECK = True
                                        else :
                                                print("PAY RATE IS NEGATIVE")                                        
                                except :
                                        print ("INVALID RATE")
                        else:
                                print ("HOURS ARE NEGATIVE")                        
                except:
                        print("INVALID HOURS")                 
        return(Hours,Pay_Rate)

def compute_pay(the_hours,the_rate):
        OVERTIME_PAY_RATE = round(the_rate * 1.5,2)
        Remainder_Hours = 0
        if the_hours >= 40:
                print("Worked 40+ Hours")
                Remainder_Hours = the_hours - 40
                the_hours = 40                
        pay = round((the_hours * the_rate) + (Remainder_Hours * (OVERTIME_PAY_RATE)),2)
        return (pay)

def print_output(pay):
        print("----------------------")
        print("Your Pay is:", pay)
    
def main():
        the_hours, the_rate = get_input()
        pay = compute_pay(the_hours,the_rate)
        print_output(pay)        

main()

'''
TEST 1
Enter Hours Worked:hwllo
INVALID HOURS
Enter Hours Worked:45
Enter Pay Rate:hello
INVALID RATE
Enter Hours Worked:-45
HOURS ARE NEGATIVE
Enter Hours Worked:45
Enter Pay Rate:-10
PAY RATE IS NEGATIVE
Enter Hours Worked:45
Enter Pay Rate:10
Worked 40+ Hours
----------------------
Your Pay is: 475.0
'''