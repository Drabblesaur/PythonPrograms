'''
Johnny To
CIS 41A   Fall 2019
Unit G take-home assignment
'''
#You need to find and print the state with the highest population in the Midwest region
def midwestFindr ():
    MidW={}
    with open('States.txt', 'r') as f:
        for line in f:
            (state,region,pop)= line.split(' ')
            if region == 'Midwest':
                MidW[state]= int(pop)
        f.close
    maxVal = max(MidW.values())
    for key, value in MidW.items(): 
            if value == maxVal:
                maxKey = key
    print('Highest population state in the Midwest is:',maxKey,maxVal)

def mostPres():
    sta={}
    with open('USPresidents.txt', 'r') as j:
        for line in j:
            (state,pres)= line.split('\t')
            if state in sta:
                sta.get(state).append(pres.rstrip())
            else:
                sta[state] = [pres.rstrip()]
    j.close
    maxval ={}
    for keys in sta.keys():
        maxval[keys]=len(sta.get(keys))
    maxi = max(maxval.values())
    for k,v in maxval.items():
        if v == maxi:
            maxState = k
    print('The state with the most presidents is',maxState,'with',maxi,'presidents:')
    for i in sta.get(maxState):
        print(i)
    return maxval

def popPres(ammntPres):
    popStates = set(['CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'])
    statePres = popStates.intersection(set(ammntPres.keys()))
    print(len(statePres), 'of the 10 high population states have had presidents born in them:')
    statePres = sorted(statePres)
    for i in statePres:
        print(i,':',ammntPres.get(i))


def main():
   midwestFindr()
   var1 = mostPres()
   popPres(var1)

main()
'''
Execution Results:
Highest population state in the Midwest is: IL 12802000
The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
8 of the 10 high population states have had presidents born in them:
CA : 1
GA : 1
IL : 1
NC : 2
NY : 5
OH : 7
PA : 1
TX : 2
'''
