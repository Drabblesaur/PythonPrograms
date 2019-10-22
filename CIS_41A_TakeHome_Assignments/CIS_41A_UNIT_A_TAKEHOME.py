'''
Johnny To
CIS 41A   Fall 2019
Unit A take-home assignment
'''

from math import sqrt
from math import log10

print("Basic Math and String Functions")
a = 3**2.5
print("a:"+str(a))
b = 2
b += 3
print("b:"+ str(b))
c=12
c /= 4
print ("c:"+str(c))
d = 5%3
print ("d:"+str(d))

print("Built-in Functions abs, round, and min")
print(abs(5-7))
print(round(3.14159,4))
print(round(186282,-2))
print(min(6, -9, -3, 0))

print("Functions from the math module")
num = float(input("A) Number?"))
print("B) Square root rounded by 2")
print(round(sqrt(num),2))
print("C) Base-10 Log")
print(round(log10(num),2))

print("Complex Numbers")
z1 = 4+3j
z2 = 2+2j
z3 = z1 * z2
print(z3)

'''
Execution results:
Basic Math and String Functions
a:15.588457268119896
b:5
c:3.0
d:2
Built-in Functions abs, round, and min
2
3.1416
186300
-9
Functions from the math module
A) Number?7.6
B) Square root rounded by 2
2.76
C) Base-10 Log
0.88
Complex Numbers
(2+14j)

'''

