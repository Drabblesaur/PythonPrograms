#CIS40 Johnny To Chapter 6 Exercise 2
# Friend Finder and Friend Adder
friends = {'2017':['John','Jason','Kevin','Vinh'],'2018':['Patrick','Emma']}
print(friends)
# Find Friend
searchFriend = input('What is your friend\'s name? :').title()
if searchFriend in friends.get('2017'):
    print("Found " + searchFriend + " in 2017")
elif searchFriend in friends.get('2018'):
    print("Found " + searchFriend + " in 2018")
else:
    print("Friend not found with name:" + searchFriend)
# Add Friend
addFriendName = input('What is your new friend\'s name? :').strip().title()
addFriendInt = input('Did you meet you friend in 2017 or 2018? :').strip()
if addFriendInt == '2018':
    friends.get('2018').append(addFriendName)
elif addFriendInt == '2017':
    friends.get('2017').append(addFriendName)
else:
    print('not valid range')
print('2017:',friends.get('2017'))
print('2018:',friends.get('2018'))
