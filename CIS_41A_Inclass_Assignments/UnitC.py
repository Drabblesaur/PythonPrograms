'''
Johnny To
CIS 41A Fall 2019
In-Class Assignment 3
'''

import copy
# a. Create a list called list1 that has elements 2, 4.1, 'hello'
list1 = [2, 4.1,'hello']
# b. Copy list1 to list2 so that list2 is an alias of list1 (shallow copy).
list2 = list1
# c. Copy list1 to list3 so that list3 is a new list (true deep copy).
list3 = copy.deepcopy(list1)
# d. Using ==, compare list1 to list2, list 1 to list 3, and list 2 to list3.
print("list1 == list2:", (list1 == list2))
print("list1 == list3:", (list1 == list3))
print("list2 == list3:", (list2 == list3))
# e. Using is, compare list1 to list2, list 1 to list 3, and list 2 to list3.
print("list1 is list2:", (list1 is list2))
print("list1 is list3:", (list1 is list3))
print("list2 is list3:", (list2 is list3))
# f. Print the ids of list 1, list2, and list3.
print("list1 id:", id(list1))
print("list2 id:", id(list2))
print("list3 id:", id(list3))
# g. Append a new element with value 8 to list1.
list1.append(8)
# h. After the first element of list2, insert an element 'goodbye'.
list2.insert(1,'goodbye')
list2[3]
# i. Remove the first element from list3.
list3.pop(0)
# j. Print each of the three lists. Do the results match what you expected?
print(list1)
print(list2)
print(list3)
# l. Tell the instructor what these results mean.

'''
Execution Results
list1 == list2: True
list1 == list3: True
list2 == list3: True
list1 is list2: False
list1 is list3: False
list2 is list3: False
list1 id: 2691963635144
list2 id: 2691963635080
list3 id: 2691963635400
[2, 4.1, 'hello', 8]
[2, 'goodbye', 4.1, 'hello']
[4.1, 'hello']
'''