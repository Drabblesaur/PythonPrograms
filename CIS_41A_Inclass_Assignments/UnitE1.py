#First Script
#1) Determining the genre of a movie.
#Create a list called scifi that contains the elements Alien, Solaris, Inception, Moon.
scifi = ['Alien','Solaris','Inception','Moon']
#Create a list called comedy that contains the elements Borat, Idiocracy, Superbad, Bridesmaids.
comedy = ['Borat', 'Idiocracy', 'Superbad', 'Bridesmaids']
#Ask the user for the name of a movie.
userin = input("Movie? :")
#Using if/elif/else, determine and print the genre of the movie.
if(userin.strip() in scifi):
    print(userin.strip(),'is Science Fiction')
elif(userin.strip() in comedy):
    print(userin.strip(),'is Comedy')
else:
    print('UNKOWN MOVIE:', userin)
#Test three times: first with Moon, then Superbad, then Dunkirk.

'''
Movie? :Moon
Moon is Science Fiction

Movie? :Superbad
Superbad is Comedy

Movie? :Dunkirk
UNKOWN MOVIE: Dunkirk
'''