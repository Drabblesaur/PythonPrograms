#CIS_40 Johnny To
Lenient_Mode = int(input("ENTER LENIENT MODE (True=1)(False=0):"))
Number1 = float(input("Enter number 1:"))
Number2 = float(input("Enter number 2:"))
Number3 = float(input("Enter number 3:"))
if (Lenient_Mode == 1):
    if (Number1 == Number2 == Number3):
        Number_State = "INCREASING & DECREASING"
    elif (Number3 <= Number2 <= Number1):
        Number_State = "DECREASING"
    elif (Number1 <= Number2 <= Number3):
        Number_State = "INCREASING"

else:
    if (Number1 < Number2 < Number3):
        Number_State = "INCREASING"
    elif (Number3 < Number2 < Number1):
        Number_State = "DECREASING"
    else:
        Number_State = "NEITHER"

print("Numbers are "+ Number_State)

'''
OUTPUT
ENTER LENIENT MODE (True=1)(False=0):1
Enter number 1:3
Enter number 2:3
Enter number 3:3
Numbers are INCREASING & DECREASING

ENTER LENIENT MODE (True=1)(False=0):1
Enter number 1:3
Enter number 2:4
Enter number 3:4
Numbers are INCREASING

ENTER LENIENT MODE (True=1)(False=0):0
Enter number 1:3
Enter number 2:3
Enter number 3:3
Numbers are NEITHER

ENTER LENIENT MODE (True=1)(False=0):0
Enter number 1:3
Enter number 2:4
Enter number 3:4
Numbers are NEITHER
'''