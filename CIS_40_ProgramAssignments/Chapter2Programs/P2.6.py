#CIS_40 Johnny To
CONVERSION_MILES_CONSTANT = 1609.344
CONVERSION_FEET_CONSTANT = 3.281
CONVERSION_INCHES_CONSTANT = 39.37
Input_Meters = float(input("ENTER MEASUREMENT IN METERS:"))
Convert_Miles = Input_Meters/CONVERSION_MILES_CONSTANT
Convert_Feet = Input_Meters*CONVERSION_FEET_CONSTANT
Convert_Inches = Input_Meters*CONVERSION_INCHES_CONSTANT
print("Meter(s):"+ str(Input_Meters))
print("Mile(s):"+str(Convert_Miles))
print("Foot(s)"+str(Convert_Feet))
print("Inch(s)"+str(Convert_Inches))

'''
OUTPUT
ENTER MEASUREMENT IN METERS:5
Meter(s):5.0
Mile(s):0.0031068559611866697
Foot(s)16.405
Inch(s)196.85

'''