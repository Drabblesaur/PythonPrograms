import csv
population={}
with open('Cities.csv', 'r') as f:
    next(f)
    for line in f:
        (name,city,pop)=line.split(',')
        population[(name,city)]=int(pop)
    f.close
for i in population:
    print(i[0],i[1],population.get(i))

cityIn = input("Please enter a city:").strip()
stateIn = input("Please enter a state:").strip()
keyVal = (cityIn,stateIn)
if keyVal in population:
    print(cityIn,stateIn,"has a population of",population.get(keyVal))
else:
    print("ERROR CANT FIND LOCATION")
'''
Execution Results:
Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064
Please enter a city:Dublin
Please enter a state:California
Dublin California has a population of 46036
'''



