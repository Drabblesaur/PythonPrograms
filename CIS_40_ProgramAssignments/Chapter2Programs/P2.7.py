# CIS_40 Johnny To
from math import pi
Input_Radius = float(input("Enter a radius:"))
Area = round((pi*(Input_Radius**2)),2)
Circumference = round((2*pi*Input_Radius),2)
Volume = round(((4/3)*pi*(Input_Radius**3)),2)
Surface_Area = round((4*pi*(Input_Radius**2)),2)

print("Radius Given:"+str(Input_Radius))
print("Area:"+str(Area))
print("Circumference:"+str(Circumference))
print("Volume:"+str(Volume))
print("Surface_Area:"+str(Surface_Area))

'''
OUTPUT
Enter a radius:5
Radius Given:5.0
Area:78.54
Circumference:31.42
Volume:523.6
Surface_Area:314.16
'''
