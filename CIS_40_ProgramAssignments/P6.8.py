# P6.8 JOHNNY TO
# Add Alternating Sums
def altSum(list):
    Sum = 0
    for i in range(len(list)):
        if i % 2 == 0:
            Sum += list[i]
        else:
            Sum -= list[i]
    return Sum

numList = []
endListTrigger = False
print("Finish Input-->(E)")
while endListTrigger == False:
    inputInt = input("Enter a Number:")
    if inputInt.upper() == "E":
        endListTrigger = True
    else:
        numList.append(int(inputInt))
print (numList)
sum = altSum(numList)
print("SUM:"+str(sum))

'''
OUTPUT
Finish Input-->(E)
Enter a Number:1
Enter a Number:4
Enter a Number:9
Enter a Number:16
Enter a Number:9
Enter a Number:7
Enter a Number:4
Enter a Number:9
Enter a Number:11
Enter a Number:e
[1, 4, 9, 16, 9, 7, 4, 9, 11]
SUM:-2

'''