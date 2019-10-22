#CIS_40 Johnny To
from math import sqrt
Height = float(input("ENTER HEIGHT:"))
Length = float(input("ENTER LENGTH:"))
Area = Height*Length
Diagonal = round(sqrt((Height**2)+(Length**2)),2)

print("GIVEN HEIGHT:"+str(Height))
print("GIVEN LENGTH:" +str(Length))
print("Area:"+str(Area))
print("Diagonal:"+str(Diagonal))

'''
OUTPUT
ENTER HEIGHT:6
ENTER LENGTH:8
GIVEN HEIGHT:6.0
GIVEN LENGTH:8.0
Area:48.0
Diagonal:10.0
'''