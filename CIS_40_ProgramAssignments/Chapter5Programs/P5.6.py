# P5.6 Johnny To
# Displays Vowels
def countVowels(string):
    strList = list(string)
    for char in strList:
        if char == "a" or char == "A":
            print(char)
        if char == "e" or char == "E":
            print(char)
        if char == "i" or char == "I":
            print(char)
        if char == "o" or char == "O":
            print(char)
        if char == "u" or char == "U":
            print(char)

string = input('Enter a String:')
countVowels(string)

'''
OUTPUT
Enter a String:this is a long string
i
i
a
o
i
'''