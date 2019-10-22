#P7.2 Johnny To
#Line Lister
openFile = str(input("File to open: "))
savedFile = str(input("File to save into: "))
inputF = open(openFile, "r")
outputF = open(savedFile, "w")
number = 1
for line in inputF:
    outputF.write("/* %s */ %s" % (number, line))
    number += 1
inputF.close()
outputF.close()
print("Written")

'''
OUTPUT
File to open: text.txt
File to save into: new.txt
Written
'''
