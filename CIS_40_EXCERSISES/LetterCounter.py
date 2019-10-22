string = input("Enter a String:")
letter = input("What letter are you looking for:")
count = 0
for i in string:
    if letter == i :
        count = count+1
print("There are ", count , (letter + "'s in \""+ string+"\""))
'''
Enter a String:hello
What letter are you looking for:l
There are  2 l's in "hello"

'''