#Part Three – How Python function arguments are treated
#There can be some confusion as to how Python functions treat their arguments - is it by reference or by value? Explore this for yourself.

#Now create a function called byVal which has one argument. In the function, add 7 to the argument. Print the ID of the argument before and after the change.
def byVal(value):
    print('Original ID of parameter in byVal',id(value))
    value += 7
    print('ID of parameter in byVal after change',id(value))

#Create a second function called byRef which has one argument. In the function, add 7 to the last element in the list. Print the ID of the argument and the ID of the last element of the argument before and after the change.
def byRef(myList):
    print('Original ID of parameter in byRef',id(myList))
    print('Original ID of parameter\'s last element in byRef', id(myList[2]))
    myList[2] +=7
    print('ID of parameter in byRef after change', id(myList))
    print('ID of parameter\'s last element in byRef after change', id(myList[2]))
    
    
#From main, create a myInt variable and give it the value 3. Also create a myList list with elements 0, 1, 2.
def main():
    myInt = 3
    myList = [0,1,2]
    #Print the IDs of myInt and myList. Also print the ID of the last element of myList.
    print('Original ID of myInt in main is',id(myInt))
    print('Original ID of myList in main is',id(myList))
    print('Original ID of myList\'s last element in main is',id(myList[2]))
    #Now call byVal with myInt and then call byRef with myList. 
    byVal(myInt)
    byRef(myList)
    # Next, again print the IDs of MyInt, myList, and the last element of myList.
    print('ID of myInt in main is',id(myInt))
    print('ID of myList in main is',id(myList))
    print('ID of myList\'s last element in main is',id(myList[2]))
    # Finally, print myInt and MyList from main. Can you explain the results?
    print('myInt is now:',myInt)
    print('Mylist is now:',myList)
main()

'''
Execution
Original ID of myInt in main is 9079072
Original ID of myList in main is 140464766075080
Original ID of myList's last element in main is 9079040
Original ID of parameter in byVal 9079072
ID of parameter in byVal after change 9079296
Original ID of parameter in byRef 140464766075080
Original ID of parameter's last element in byRef 9079040
ID of parameter in byRef after change 140464766075080
ID of parameter's last element in byRef after change 9079264
ID of myInt in main is 9079072
ID of myList in main is 140464766075080
ID of myList's last element in main is 9079264
myInt is now: 3
Mylist is now: [0, 1, 9]
'''
