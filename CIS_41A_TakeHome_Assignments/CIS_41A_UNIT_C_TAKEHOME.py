'''
Johnny To
CIS 41A   Fall 2019
Unit C take-home assignment
'''
# SCRIPT 1 - Working with Lists
# a) Create an empty list called list1
list1 = list()
# b) Populate list1 with the values 1,3,5
list1.append(1)
list1.append(3)
list1.append(5)
# c) Create list2 and populate it with the values 1,2,3,4
list2 = [1,2,3,4]
# d) eate list3 by using + (a plus sign) to combine list1 and list2. Print list3.
list3 = list1+list2
print('d) list3 is:',list3)
# e) Use sequence operator in to test list3 to see if it contains a 3, print True/False result (do with one line of code).
print('e) list3 contains a 3:', 3 in list3)
# f) Count the number of 3s in list3, print the result.
print('f) list3 contains ',list3.count(3),'3s')
# g) Determine the index of the first 3 in list3, print the result.
print('g) The index of the first 3 contained in list3 is ',list3.index(3))
# h) Pop this first 3 and assign it to a variable called first3, print first3.
first3 = list3.pop(list3.index(3))
print('h) first3=',first3)
# i) Create list4, populate it with list3's sorted values, using the sorted built-in function.
list4 = sorted(list3)
# j) Print list3 and list4.
print('j) list3 is now:',list3)
print('j) list4 is:', list4)
# k) Slice list3 to obtain a list of the values 1,2,3 from the middle of list3, print the result.
print('k) Slice of list3 is:', list3[2:5])
# l) Determine the length of list3, print the result.
print('l) Length of list3 is ', len(list3))
# m) Determine the max value of list3, print the result.
print('m) The max value in list3 is',max(list3))
# n) Sort list3 (use the list sort method), print list3.
list3.sort()
print('n) Sorted list3 is:',list3)
# o) Create list5, a list of lists, using list1 and list2 as elements of list5, print list5.
list5 =[list1,list2]
print('o) list5 is:',list5)
# p) Print the value 4 contained within list5.
print('p) Value 4 from list5:', list5[1][3])

#SCRIPT 2 - Binary Operators
# a) Assign the values 9 and 14 to variables a and b respectively.
a=9
b=14
# b) Print the binary values of a and b (use the bin built-in function).
print('b) binary of a =',bin(a))
print('b) binary of b =',bin(b))
# c) Calculate the value of a and b, print the result in binary.
print('c) binary of a & b =',bin(a&b))
# d) Calculate the value of a or b, print the result in binary.
print('c) binary of a | b =',bin(a|b))
# e) Examine the results. Can you see how they were arrived at?
'''
9 in base 2 (binary) is 1001
14 in base 2 (binary) is 1110

'''

'''
Execution Results:
d) list3 is: [1, 3, 5, 1, 2, 3, 4]
e) list3 contains a 3: True
f) list3 contains  2 3s
g) The index of the first 3 contained in list3 is  1
h) first3= 3
j) list3 is now: [1, 5, 1, 2, 3, 4]
j) list4 is: [1, 1, 2, 3, 4, 5]
k) Slice of list3 is: [1, 2, 3]
l) Length of list3 is  6
m) The max value in list3 is 5
n) Sorted list3 is: [1, 1, 2, 3, 4, 5]
o) list5 is: [[1, 3, 5], [1, 2, 3, 4]]
p) Value 4 from list5: 4
b) binary of a = 0b1001
b) binary of b = 0b1110
c) binary of a & b = 0b1000
c) binary of a | b = 0b1111
'''

