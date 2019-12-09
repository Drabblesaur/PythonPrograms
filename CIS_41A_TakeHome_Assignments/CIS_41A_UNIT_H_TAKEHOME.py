'''
Johnny To
CIS 41A   Fall 2019
Unit H take-home assignment
'''
# SCRIPT 1
# Write an overseerSystem function that has a kwargs argument.
def overseerSystem(**kwargs):
    for operation,value in kwargs.items():
        # see if the keyword temperature exists in kwargs. If it does, and the temperature is greater than 500, print a warning with the temperature.
        if operation.upper() == 'TEMPERATURE':
            if value > 500:
                print('Warning: temperature is',value)
        # see if the keyword CO2level exists in kwargs. If it does, and the CO2level is greater than .15, print a warning with the CO2level.
        elif operation.upper() == 'CO2LEVEL':
            if float(value) > .15:
                print('Warning: CO2level is',value)
        # see if the keyword miscError exists in kwargs. If it does, print a warning with the miscError number.
        elif operation.upper() == 'MISCERROR':
            print('Misc error #',value)

# SCRIPT 2
# Create a BritCoins class with the following methods: __init__, __add__ , __sub__ , __str__. 
# There will also be a private class dictionary called __coinValues as follows (this is similar to the __metric variable in the Length example).
class BritCoins:
    __coinValues = {"pound":240, "shilling":12, "penny":1}
    # The __init__ method should have the parameters self, and **kwargs.
    def __init__(self,**kwargs):
        # Start by initializing a self.totalPennies attribute to zero
        self.totalPennies = 0
        # Then iterate through the kwargs. For each coinType in kwargs, add the value in pennies of that type and quantity of coin to a self.totalPennies
        for key,val in kwargs.items():
            if key == 'pound':
                self.totalPennies += self.__coinValues.get('pound')*(val)
            elif key == 'shilling':
                self.totalPennies += self.__coinValues.get('shilling')*(val)
            elif key == 'penny':
                self.totalPennies += val
    # should have the parameters self and other. Calculate a local total by adding self.totalPennies to other.totalPennies. Then return this value.  
    def __add__(self,other):
        totalPennies = self.totalPennies + other.totalPennies
        return BritCoins(penny=totalPennies)
    # The __sub__ method should have the parameters self and other. It is similar to the add method except that you subtract other from self instead of adding it.
    def __sub__(self,other):
        remainderPennies = self.totalPennies - other.totalPennies
        return BritCoins(penny=remainderPennies)
    # The __str__ method has the parameter self and should return a string that represents the value of the BritCoins object. 
    # The string should be formatted as shown below, showing pounds, shillings and pennies. From self.totalPennies
    def __str__(self):
        Pennies = self.totalPennies
        Pounds = int(Pennies/self.__coinValues.get('pound'))
        Pennies -= Pounds*self.__coinValues.get('pound')
        Shilling =int(Pennies/self.__coinValues.get('shilling'))
        Pennies -= Shilling*self.__coinValues.get('shilling')
        return str(Pounds)+' pound(s) '+str(Shilling)+' shilling(s) '+str(Pennies)+' pennies '


def main():
    Message1 = {'temperature':550}
    Message2 = {'temperature':475}
    Message3 = {'temperature':450, 'miscError':404}
    Message4 = {'CO2level':.18}
    Message5 = {'CO2level':.2, 'miscError':418}
    overseerSystem(**Message1)
    overseerSystem(**Message2)
    overseerSystem(**Message3)
    overseerSystem(**Message4)
    overseerSystem(**Message5)
    c1 = BritCoins(pound=4,shilling=24,penny=3)
    c2 = BritCoins(pound=3,shilling=4,penny=5)
    c3 = c1 + c2
    c4 = c1 - c2
    print(c1.__str__())
    print(c2.__str__())
    print(c3.__str__())
    print(c4.__str__())

main()
'''
Execution Results
Warning: temperature is 550
Misc error # 404
Warning: CO2level is 0.18
Warning: CO2level is 0.2
Misc error # 418
5 pound(s) 4 shilling(s) 3 pennies
3 pound(s) 4 shilling(s) 5 pennies
8 pound(s) 8 shilling(s) 8 pennies
1 pound(s) 19 shilling(s) 10 pennies
'''