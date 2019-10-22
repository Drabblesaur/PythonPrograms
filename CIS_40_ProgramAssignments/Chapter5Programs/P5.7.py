# P5.7 Johnny To
# Displays Word Count
count = 0
line = input('Enter text:')
words = line.split()
for x in words:
    count += 1
print('words:'+str(count))

'''
OUTPUT
Enter text:Mary had a little lamb
words:5

'''