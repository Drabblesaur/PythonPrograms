# CIS40 Johnny To Chapter 6 Exercise 3
# Word Counter from text
count = dict()
# Convert all word to Uppercase
line = input('Enter text:').upper()
words = line.split()
# print all words in the text
print ('Words:',words)
for x in words:
    count[x] = count.get(x,0)+1
# print all words counted
print('Counts:',count)

'''
OUTPUT
Enter text:blah Blah why hello there i didn't really see you there
Words: ['BLAH', 'BLAH', 'WHY', 'HELLO', 'THERE', 'I', "DIDN'T", 'REALLY', 'SEE', 'YOU', 'THERE']
Counts: {'BLAH': 2, 'WHY': 1, 'HELLO': 1, 'THERE': 2, 'I': 1, "DIDN'T": 1, 'REALLY': 1, 'SEE': 1, 'YOU': 1}
'''