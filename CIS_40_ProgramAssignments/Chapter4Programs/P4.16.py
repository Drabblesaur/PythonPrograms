# CIS 40 Johnny To P.4.16
# print all factors of the input
inputInt = int(input("Enter an integer: "))
i = 2
while i <= inputInt:
    if inputInt % i == 0:
        print(i)
        inputInt = inputInt/i
    else:
        i += 1

'''
OUTPUT

Enter an integer: 10
2
5

Enter an integer: 5
5

'''