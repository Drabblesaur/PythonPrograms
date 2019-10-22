'''
Johnny To
CIS 41A Fall 2019
In-Class Assignment 4
'''
# Create a dictionary of fruit and desserts made from the fruit. The fruit should be the key and the dessert should be the value. Use these key value pairs:
dessert= {
'apple':'sauce',
'peach':'cobbler',
'carrot':'cake',
'strawberry':'sorbet',
'banana':'cream pie'
}
#Add the mango fruit to the dictionary. Its dessert is sticky rice.
dessert['mango'] = 'sticky rice'
#Change the strawberry dessert to shortcake.
dessert['strawberry'] = 'shortcake'
#Carrot is not a fruit, so remove carrot from the dictionary.
dessert.pop('carrot')
#Print the apple dessert.
print(dessert['apple'])
#See if a banana dessert exists.
print('banana' in dessert )
#See if a pear dessert exists.
print('pear' in dessert )
#Print the keys in the dessert dictionary.
print(dessert.keys())
#Print the values in the dessert dictionary.
print(dessert.values())
#Print the key-value pairs in the dessert dictionary.
print(dessert.items())

#Script 2
# Create a dictionary named capitols1 and populate it 
capitols1 = {
    'Alabama':'Montgomery',
    'Alaska':'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California':'Sacramento'
}
# Create a dictionary named capitols2 and populate it
capitols2 = {
    'California' :'Sac.',
    'Colorado':'Denver',
    'Connecticut':'Hartford'
}
# Using the dictionary update() method, update capitols1 with capitols2.
capitols1.update(capitols2)
# Print the sorted capitols (values). Note the updated value of California's capitol.
print(sorted(capitols1.values()))

#Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.
class1 = {'Li', 'Audry', 'Jia', 'Migel', 'Tanya'}
#Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.
class2 = {'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'}
#Add John to class1.
class1.add('John')
#Print a sorted list of students who are in both classes.
print(sorted(class1 & class2))
#Print a sorted list of all students.
print(sorted(class1|class2))
#Test to see if Sasha is in class1.
print('Sasha'in class1)
'''
Execution Results:

sauce
True
False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
['Audry', 'Migel', 'Tanya']
['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
False
'''