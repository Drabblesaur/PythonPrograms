#CIS_40 Johnny To
Number1 = float(input("Enter number 1:"))
Number2 = float(input("Enter number 2:"))
Number3 = float(input("Enter number 3:"))
if(Number1 == Number2 == Number3):
    Number_State = "SAME"
elif(Number1==Number2 or Number1==Number3 or Number2==Number3):
    Number_State = "NEITHER"
elif (not(Number1 == Number2 == Number3)):
    Number_State = "DIFFERENT"
print("all numbers are:"+Number_State)

'''
OUTPUT
Enter number 1:5
Enter number 2:5
Enter number 3:5
all numbers are:SAME

Enter number 1:1
Enter number 2:2
Enter number 3:3
all numbers are:DIFFERENT

Enter number 1:5
Enter number 2:6
Enter number 3:5
all numbers are:NEITHER
'''