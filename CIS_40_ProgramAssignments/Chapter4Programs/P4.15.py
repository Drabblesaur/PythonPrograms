# CIS 40 Johnny To P.4.15
# prints the Fibonacci numbers till it reaches the ending integer
nTerm = int(input("Enter an integer: "))
fold1 = 0
fold2 = 0
fnew = 1
while fnew <= nTerm:
    print(fnew)
    fold2 = fold1
    fold1 = fnew
    fnew = fold1 + fold2

'''
OUTPUT
Enter an integer: 12
1
1
2
3
5
8

'''