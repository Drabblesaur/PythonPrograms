#CIS_40 Johnny To
float_Size = "null"
Input_Float = float(input("Enter a number:"))
if (Input_Float == 0.0):
    Float_State = "0"
elif(Input_Float<0.0):
    Float_State = "NEGATIVE"
elif(Input_Float>0.0):
    Float_State = "POSITIVE"
if(abs(Input_Float)<1 and abs(Input_Float)>0):
    float_Size = "SMALL"
elif(abs(Input_Float)>1000000):
    float_Size = "LARGE"
print(("Number given is "+Float_State),end="")
if(not(float_Size == "null")):
    print(" and is "+float_Size)

'''
OUTPUT
Enter a number:0
Number given is 0

Enter a number:-0.1
Number given is NEGATIVE and is SMALL

Enter a number:-1000001
Number given is NEGATIVE and is LARGE

Enter a number:0.5
Number given is POSITIVE and is SMALL

Enter a number:20000000
Number given is POSITIVE and is LARGE



'''