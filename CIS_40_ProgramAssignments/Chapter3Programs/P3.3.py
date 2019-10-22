#CIS_40 Johnny To
Input_Integer = int(input("Enter an integer:"))
if(Input_Integer<0):
    Input_Integer = Input_Integer*-1
if(Input_Integer>0):
    Int_Size = "one"
if(Input_Integer>=10):
    Int_Size = "two"
if(Input_Integer>=100):
    Int_Size = "three"
if(Input_Integer>=1000):
    Int_Size = "four"
if(Input_Integer>=10000):
    Int_Size = "five"
if(Input_Integer>=100000):
    Int_Size = "six"
if(Input_Integer>=1000000):
    Int_Size = "seven"
if(Input_Integer>=10000000):
    Int_Size = "eight"
if(Input_Integer>=100000000):
    Int_Size = "nine"

print("Integer Size:"+Int_Size)

'''
OUTPUT

Enter an integer:252783570
Integer Size:nine

Enter an integer:23456
Integer Size:five
'''