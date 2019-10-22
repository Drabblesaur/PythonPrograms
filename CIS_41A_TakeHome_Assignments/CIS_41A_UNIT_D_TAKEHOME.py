'''
Johnny To
CIS 41A   Fall 2019
Unit D take-home assignment
'''
# Part One - Sets
# a) Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.
class1 = set(['Li','Audry','Jia','Migel','Tanya'])
# b)Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.
class2 = set(['Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'])
# c) Create a set named class3 and populate it with the students Migel, Zhang, Hiroto, Anita, Jia.
class3 = set(['Migel', 'Zhang', 'Hiroto', 'Anita', 'Jia'])
# d) Print a sorted list of students who are in all three classes.
class12 = class1.intersection(class2)
class123 = sorted(class12.intersection(class3))
print('Students in all three classes: ',class123)
# e) Print a sorted list of all students.
classAll = class1.union(class2).union(class3)
print('All students:',classAll)
# f) Print a sorted list of all students in class1 but not class2 or class3.
onlyClass1 = class1.difference(class2)
onlyClass1 = onlyClass1.difference(class3)
print('Students in class1 but not class2 or class3:',onlyClass1)

# Part Two - Swap
# a) Create a list containing elements 1, 2, 3
list1 = [1,2,3]
# b) Swap the second and third elements of the list. Do this with one line of code.
list1[1], list1[2] = list1[2], list1[1]
# c) Print the list.
print('List after swap:',list1)

# Part Three – Tuple Basics
# For Parts Three, Four and Five, you will be working with data about the movie Casablanca.

# a) Create a tuple that contains the elements Casablanca, 1942, romantic drama.
tupleMovie = ('Casablanca', 1942, 'romantic drama')
# b) Unpack the tuple into variables title, year, genre.
title = tupleMovie[0]
year = tupleMovie[1]
genre = tupleMovie[2]
# c) Print the title.
print('My favorite movie is:',title)

#Part Four – Named Tuple
from collections import namedtuple

# a) Define a named tuple called Movie that contains the fields title, year, genre.
Movie = namedtuple('Movie','title year genre')
# b) Create a Movie tuple that contains the elements Casablanca, 1942, romantic drama.
movTuple = Movie(title='Casablanca', year= 1942, genre = 'romantic drama' )
# c) Print the title.
print('My favorite movie is:',movTuple.title)

# Part Five – Named Tuple Containing a List

# a) Define a named tuple called Moviestars that contains the fields title, year, genre, stars.
Moviestars = namedtuple('Moviestars','title year genre stars')
# b) Create a Moviestars tuple called favoritemovie that contains the elements Casablanca, 1942, romantic drama, and a list containing elements Humphrey Bogart, Ingrid Bergman.
favoritemovie = Moviestars(title = 'Casablanca',year = 1942, genre = 'romantic drama', stars = ['Humphrey Bogart', 'Ingrid Bergman'])
# c) Append Claude Rains to the stars list. Hint: Use the syntax favoritemovie.stars.append
favoritemovie.stars.append('Claude Rains')
# d) Print star Ingrid Bergman.
print('My favorite star is:',favoritemovie.stars[1])
# e) Print favoritemovie.
print(favoritemovie)
# Note that, even though a tuple is immutable, we are able to change a list that is contained by a tuple.

'''
Execution Results

Students in all three classes:  ['Migel']
All students: {'Audry', 'Jia', 'Hiroto', 'Anita', 'Zhang', 'Tanya', 'Migel', 'Li', 'Sasha'}
Students in class1 but not class2 or class3: {'Li'}
List after swap: [1, 3, 2]
My favorite movie is: Casablanca
My favorite movie is: Casablanca
My favorite star is: Ingrid Bergman
Moviestars(title='Casablanca', year=1942, genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])
'''