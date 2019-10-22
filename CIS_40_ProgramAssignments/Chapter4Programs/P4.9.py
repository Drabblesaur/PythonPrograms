# CIS 40 Johnny To P.4.9
# Reverses a word
inputString = str(input("Enter a word: "))
for i in range(len(inputString) - 1, -1, -1):
    print(inputString[i], end = "")

'''
OUTPUT

Enter a word: ekans
snake

Enter a word: arbok
kobra
'''