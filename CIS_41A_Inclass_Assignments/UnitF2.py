'''
Johnny To
CIS 41A Fall 2019
In-Class Assignment 5
'''
#Part Two – Error Handling
#Write a function called printListElement. The function has two arguments and no return value. The first argument is a list, and the second argument is a list index. The function will print an element from the list as determined by the list index. If the list index is invalid, print an error message.
#We could accomplish this with a logic test, but instead, we will manage this with error handling.
#Write a try block that attempts to print the list element. Catch any errors with an except block, print an error message.
def printListElement(listvar,index):
    try:
        print(listvar[index])
    except IndexError:
        print('ERROR: Index Out of Bounds')
    except:
        print('Error occured')


#From main, create a myList list with elements 0, 1, 2 by using the list and range commands.
#Then, call printListElement with your list and a list index value of 3.
def main():
    myList = []
    for i in range(0,3):
        myList.append(i)
    printListElement(myList,3)

main()
'''
Execution Results
ERROR: Index Out of Bounds
'''