# CIS 40 Johnny To Chapter 6 EX4
#Displays medals from countries

# Create a Table (List on a List)
medalCount = [
    [0,3,0],[0,0,1],[0,0,1],[1,0,0],[3,1,1],[0,1,0],[1,0,1],
    ]
medalCountDic = {"Canada":[0,3,0],"Italy":[0,0,1],"Germany":[0,0,1],
                 "Japan":[1,0,0], "Russia":[3,1,1],"South Korea":[0,1,0],
                 "United States":[1,0,1]}
# Counts all medals
def countMedals(lst):
    medalCount = 0
    for countries in lst:
        for medal in countries:
            medalCount += medal
    return medalCount

def countMedalsSpec(lst):
    goldCount = 0
    silverCount = 0
    bronzeCount = 0
    for countries in lst:
            goldCount += countries[0]
            silverCount += countries[1]
            bronzeCount += countries[2]
    return goldCount,silverCount,bronzeCount

# Removes all Gold medal values that are 0
def removeZeros(lst):
    itemRemove = []
# NOTE: having lst.pop(lst.index(medals)) in the for loop doesn't give the required result
    for medals in lst:
        if medals[0]==0:
# SOL: Any gold val's that are 0 are stored to a list to be removed in a second step
            lst.pop(lst.index(medals))
    for item in itemRemove:
        lst.pop(lst.index(item))

# Print the table
for medal in medalCount:
    print(medal)
print("----------------------------")
#Print the total number of medals
totalMedal = countMedals(medalCount)
print('TOTAL: ',totalMedal)
print("----------------------------")
totalMedalSpec = countMedalsSpec(medalCount)
print (totalMedalSpec)
print("----------------------------")
removeZeros(medalCount)
for medal in medalCount:
    print(medal)

print("----------------------------")
for country,medal in medalCountDic.items():
    print(country,medal)

'''
OUTPUT
[0, 3, 0]
[0, 0, 1]
[0, 0, 1]
[1, 0, 0]
[3, 1, 1]
[0, 1, 0]
[1, 0, 1]
----------------------------
TOTAL:  14
----------------------------
(5, 5, 4)
----------------------------
[0, 0, 1]
[1, 0, 0]
[3, 1, 1]
[1, 0, 1]
----------------------------
Canada [0, 3, 0]
Italy [0, 0, 1]
Germany [0, 0, 1]
Japan [1, 0, 0]
Russia [3, 1, 1]
South Korea [0, 1, 0]
United States [1, 0, 1]
'''
