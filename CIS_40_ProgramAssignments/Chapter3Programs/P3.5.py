#CIS_40 Johnny To
Number1 = float(input("Enter number 1:"))
Number2 = float(input("Enter number 2:"))
Number3 = float(input("Enter number 3:"))
if(Number1<Number2<Number3):
    Number_State = "INCREASING"
elif(Number3<Number2<Number1):
    Number_State = "DECREASING"
else:
    Number_State = "NEITHER"

print("Numbers are "+ Number_State)

'''
OUTPUT
Enter number 1:1
Enter number 2:2
Enter number 3:3
Numbers are INCREASING

Enter number 1:5
Enter number 2:4
Enter number 3:3
Numbers are DECREASING

Enter number 1:3
Enter number 2:4
Enter number 3:4
Numbers are NEITHER
'''