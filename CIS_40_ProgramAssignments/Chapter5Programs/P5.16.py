# P5.16 Johnny To
# Palindrome detector
def isPalindrome(string):
    revString = ''.join(reversed(string))
    if revString == string:
        return True
    else:
        return False


string = input('Enter a String:')
print(isPalindrome(string))

'''
OUTPUT
Enter a String:cat
False

Enter a String:rotor
True

'''