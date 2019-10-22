#CIS40 Johnny To Chapter 6 Exercise 1
# Friend Finder and Friend Adder 
friends2017 = ['John','Jason','Kevin','Vinh']
friends2018 = ['Patrick','Emma']
totalFriends = friends2017 + friends2018
print(totalFriends)
# Find Friend
searchFriend = input('What is your friend\'s name? :').title()
if searchFriend in friends2017:
    print("Found " + searchFriend + " in 2017")
elif searchFriend in friends2018:
    print("Found " + searchFriend + " in 2018")
else:
    print("Friend not found with name:" + searchFriend)
# Add Friend
addFriendName = input('What is your new friend\'s name? :').strip().title()
addFriendInt = input('Did you meet you friend in 2017 or 2018? :').strip()
if addFriendInt == '2018':
    friends2018.append(addFriendName)
elif addFriendInt == '2017':
    friends2017.append(addFriendName)
else:
    print('not valid range')
totalFriends = friends2017 + friends2018
print(totalFriends)
print('2017:',friends2017)
print('2018:',friends2018)

'''
OUTPUT

['John', 'Jason', 'Kevin', 'Vinh', 'Patrick', 'Emma']
What is your friend's name? :jason
Found Jason in 2017
What is your new friend's name? :bob
Did you meet you friend in 2017 or 2018? :2017
['John', 'Jason', 'Kevin', 'Vinh', 'Bob', 'Patrick', 'Emma']
2017: ['John', 'Jason', 'Kevin', 'Vinh', 'Bob']
2018: ['Patrick', 'Emma']

['John', 'Jason', 'Kevin', 'Vinh', 'Patrick', 'Emma']
What is your friend's name? :bob
Friend not found with name:Bob
What is your new friend's name? :bob
Did you meet you friend in 2017 or 2018? :2019
not valid range
['John', 'Jason', 'Kevin', 'Vinh', 'Patrick', 'Emma']
2017: ['John', 'Jason', 'Kevin', 'Vinh']
2018: ['Patrick', 'Emma']
'''
