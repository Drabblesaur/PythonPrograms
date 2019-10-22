integers = int(input())
evenSum = 0
oddSum = 0
while integers > 0:
    if integers % 2 == 0:
        evenSum += integers
    if integers % 2 == 1:
        oddSum += integers
    integers = int(input())
print (str(evenSum)+" "+str(oddSum))