# CIS 40 Johnny To P.4.12
# reads a word and prints all substrings
inputString = str(input("Enter a word: "))
subLength = 1
start = 0
for i in range(len(inputString)):
    start = 0
    while start + subLength <= len(inputString):
        print(inputString[start:start + subLength])
        start += 1
    subLength += 1

'''
OUTPUT

Enter a word: rum
r
u
m
ru
um
rum

Enter a word: hello
h
e
l
l
o
he
el
ll
lo
hel
ell
llo
hell
ello
hello
'''