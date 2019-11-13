#Part 2 - Different ways of working with Attributes
#Here we explore different ways to work with Python attributes. Note that, while one of the approaches we are using is set/get, this approach is generally deprecated in favor of the simpler dot notation.

#Create a StateData2 class with the following methods: __init__, setRegion, getRegion.
class StateData2:
    #The __init__ method should have the parameters self, name and should store the name as an attribute.
    def __init__(self,name):
        self.name = name
    #The setRegion should have the parameters self, region and should store the region as an attribute.
    def setRegion(self,region):
        self.region = region
    #The getRegion should have the the parameter self and should return the the value of the region data variable.
    def getRegion(self):
        return self.region

#Test the class by creating an instance of the class called s2 with the following data: "California". Then call setRegion with the argument "West". Then set the population attribute with the following line of code: s2.pop = 39250000
s2 = StateData2("California")
s2.setRegion("West")
s2.pop = 39250000
#Then print four lines: s2.name, s2.getRegion(), s2.region, s2.pop
print(s2.name)
print(s2.getRegion())
print(s2.pop)
#Again, this test code should be after your class code.

'''
Execution:
California
West
39250000
'''