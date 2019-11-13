#Part 1 - A Basic Class - State Data
#Create a StateData class with the following methods: __init__, __str__, displayState.
#Note: __ is two underline characters.
class StateData:
    #The __init__ method should have the parameters self, name, abbreviation, region, and population and should store the name, abbreviation, region, and population as attributes.
    def __init__(self,name,abbreviation,region,population):
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self.population = population
    #The __str__ method has the parameter self and should return the state's name.
    def __str__(self):
        return self.name

    #The displayState method has the parameter self and should print formatted state data as shown below.
    def displayState(self):
        print(self.name,'(',self.abbreviation,') is in the',self.region,'region and has population of',self.population)

#Test the class by creating an instance of the class (instantiating) called s1 with the following data: "California", "CA", "West", 39250000. Print your state object (this will call the __str__ method). Then call displayState. This test code should be after your class code - don't worry about calling from main.
s = StateData("California", "CA", "West", 39250000)
print(s)
s.displayState()

'''
Execution:
California
California ( CA ) is in the West region and has population of 39250000
'''