#1) Using range with a for loop.
#Use a for loop to print the even integers in descending order from 10 to 0 inclusive.
for i in range(10,-2,-2):
    print(i)

#2) Looping through dictionary items.
#Create a dictionary named movies and populate it
movies = {
'The Wizard of Oz':1939,
'The Godfather':1972,
'Lawrence of Arabia':1962,
'Raging Bull':1980
}
#Loop through the dictionary items and print the year in which each movie was made. Output should be alpha sorted by movie title.
for a in sorted(movies):
    print(a, 'is made in:',movies.get(a))

'''
10
8
6
4
2
0
Lawrence of Arabia is made in: 1962
Raging Bull is made in: 1980
The Godfather is made in: 1972
The Wizard of Oz is made in: 1939
'''