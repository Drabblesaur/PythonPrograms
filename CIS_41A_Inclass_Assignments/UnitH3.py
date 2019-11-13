#Part 3 - Data Hiding
#Data hiding within Python is achieved with the use of special naming conventions: beginning an attribute name with either a single underscore (protected) or a double underscore (private).

#Create a StateData2 class with the following method: __init__.
class StateData2:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
#The __init__ method should have the parameter self.
#  It should store the value "Public" in an attribute called public,
#  the value " Protected" in an attribute called _protected (use a single underscore),
#  and the value " Private" in an attribute called __private (use a double underscore).__private
test = StateData2()
print(test.public)
print(test._protected)
try:
    print(test.__private)
except AttributeError:
    print('Error')



'''
Public
Protected
Traceback (most recent call last):
  File "/home/suzhiheng/Desktop/Py_Pgrms/CIS_41A_Inclass_Assignments/UnitH3.py", line 17, in <module>
    print(test.__private)
AttributeError: 'StateData2' object has no attribute '__private'
'''

#print(test._StateData2__private)