#CIS_40 Johnny To
First_Num = int(input("Enter first Integer:"))
Second_Num = int(input("Enter second Integer:"))
Sum = (First_Num + Second_Num)
Difference = (First_Num - Second_Num)
Product = (First_Num*Second_Num)
Average = Sum/2
Distance = abs(Difference)
Max = max(First_Num,Second_Num)
Min = min(First_Num,Second_Num)

print("Sum:%12d" % Sum)
print("Difference:%5d" % Difference)
print("Product:%8d" % Product)
print("Average:%8d" % Average)
print("Distance:%7d" % Difference)
print("Max:%12d" % Max)
print("Min:%12d" % Min)

'''
OUTPUT
Enter first Integer:4
Enter second Integer:2
Sum:           6
Difference:    2
Product:       8
Average:       3
Distance:      2
Max:           4
Min:           2
'''