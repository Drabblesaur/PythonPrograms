# CIS 40 Johnny To P.4.17
# Prints all prime numbers till ending integer
from math import sqrt
inputInt = int(input("Enter an integer: "))
i = 2
while i <= inputInt:
    if i == 2 or i == 3:
        print(i)
    else:
        isPrime = True
        limit = int(sqrt(float(i)))
        for j in range(2, limit+1):
            if i % j == 0:
                isPrime = False
        if isPrime:
            print(i)
    i += 1

'''
OUTPUT

Enter an integer: 10
2
3
5
7
'''