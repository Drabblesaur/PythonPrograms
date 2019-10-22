Integer1 = int(input("Enter integer 1:"))
Integer2 = int(input("Enter integer 2:"))
Integer3 = int(input("Enter integer 3:"))
if (Integer1 == Integer2 == Integer3):
    Number_State = "in order"
elif (Integer3 <= Integer2 <= Integer1):
    Number_State = "in order"
elif (Integer1 <= Integer2 <= Integer3):
    Number_State = "in order"
else:
    Number_State = "not in order"
print(Integer1,Integer2,Integer3,Number_State)

'''
OUTPUT
Enter integer 1:1
Enter integer 2:2
Enter integer 3:5
1 2 5 in order

Enter integer 1:1
Enter integer 2:5
Enter integer 3:2
1 5 2 not in order

Enter integer 1:5
Enter integer 2:2
Enter integer 3:1
5 2 1 in order

Enter integer 1:1
Enter integer 2:2
Enter integer 3:2
1 2 2 in order

Enter integer 1:2
Enter integer 2:2
Enter integer 3:2
2 2 2 in order

'''