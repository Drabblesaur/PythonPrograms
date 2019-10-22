#CIS_40 Johnny To
CONVERSION_FACTOR = 25.4
Letter_Size_Height_In = 11
Letter_Size_Width_In = 8.5
Letter_Size_Height_Mm = (CONVERSION_FACTOR*Letter_Size_Height_In)
Letter_Size_Width_Mm = (CONVERSION_FACTOR*Letter_Size_Width_In)
print("US LETTER HEIGHT IN MILLIMETERS:"+str(Letter_Size_Height_Mm))
print("US LETTER WIDTH IN MILLIMETERS:"+str(round(Letter_Size_Width_Mm,1)))

'''
OUTPUT
US LETTER HEIGHT IN MILLIMETERS:279.4
US LETTER WIDTH IN MILLIMETERS:215.9

Process finished with exit code 0
'''