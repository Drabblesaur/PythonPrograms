#CIS_40 Johnny To
from math import sqrt
Letter_Size_Height_In = 11
Letter_Size_Width_In = 8.5

Letter_Size_Diagonal_In = sqrt((Letter_Size_Height_In**2)+(Letter_Size_Width_In**2))
print("US LETTER DIAGONAL IN MILLIMETERS:" + str(round(Letter_Size_Diagonal_In,2)))

'''
OUTPUT
US LETTER DIAGONAL IN MILLIMETERS:13.9

'''