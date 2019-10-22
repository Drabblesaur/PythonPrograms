'''
Johnny To
CIS 41A   Fall 2019
Unit B take-home assignment
'''

# SCRIPT 1

# String Type Tests
#  a. Ask the user for a string (test with "ABC123").
strName = input("String? :")
# b. Use method isupper to test the string, print the result.
print(strName.isupper())
# c. Use method isdigit to test the string, print the result.
print(strName.isdigit())
# d. Use method isalpha to test the string, print the result.
print(strName.isalpha())

# Escape Characters within a string
# a. Assign the text
var1 = "Type, type, type away.\nCompile. Run. Hip hip hooray!\nNo error today!"
# b. Print the text
print(var1)

# Slicing a string
# a. Assign the text
var2 = "And now for something completely different"
# b. Slice quote to obtain the text "And no" from the beginning of the quote, print the results.
print(var2[0:6])
# c. Slice quote to obtain the text "rent" from the end of the quote, print the results.
print(var2[(len(var2)-4):])
# d. Slice quote to obtain the text "me" from the middle of the quote, print the results.
print(var2[14:16])
# e. Slice quote to obtain the text "Adnwf..." by extracting every other letter, print the results.
print(var2[::2])
# f. Slice quote to obtain the text "tnere..." by reversing the quote, print the results.
print(var2[::-1])

# Using string operators + and *
# a. Assign the text ".~*'" to a variable called pattern1.
pattern1 = ".~*'"
# b. Create a variable called pattern2, assign to it pattern1 combined with pattern1 reversed. pattern2 should now contain the string ".~*''*~."
pattern2 = pattern1+pattern1[::-1]
# c. Print pattern2 repeated five times. The output should appear as follows: .~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.
print(pattern2*5)

'''
Execution results:

String? :ABC123
True
False
False
Type, type, type away.
Compile. Run. Hip hip hooray!
No error today!
And no
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.
'''
