'''
Johnny To
CIS 41A Fall 2019
Unit F take-home assignment
'''

#Part One – Keyword Arguments and Default Values

#Write an invoice function.

#The function will generate a simple invoice and will have two required arguments and two keyword arguments.
#The two required arguments are unitPrice and quantity.
#The first keyword argument is shipping, and it has a default value of 10.
#The second keyword argument is handling, and it has a default value of 5.
def invoice(unitPrice,quantity,shipping=10,handling=5):
    print('Cost (unitPrice x quantity) =',unitPrice*quantity)
    print('Shipping =',shipping)
    print('Handling =',handling)
    print('Total =',unitPrice*quantity+shipping+handling)

#Part Two – args (Variable-Length Arguments)
#Write a printGroupMembers function.
#The function prints a list of students who are working together on a group project, as well as the group name.
#The function has one required argument, the group name, and one variable-length argument that contains the student names.
def printGroupMembers(groupName,*studentNames):
    print('Members of',groupName)
    for i in studentNames:
        print(i)


#Part Three – Non-Rectangular (Ragged) 2D lists
#Write two functions that will build and display a Bell triangle - see: What is a Bell triangle
#A Bell triangle can be constructed as follows:

#The first row has a single element which has the value 1.
#For the second row and all subsequent rows:
#The number of elements in a row is equal to the number of elements in the previous row + 1.
#The first element in the row is equal to the last element of the previous row.
#The second through nth elements of a row are calculated by adding the value of the previous element (n-1) in the current row to the (n-1) element of the previous row.
def buildBell(row):
    finalList=[]
    for i in range(1,row+1):
        indexList=[]
        if len(finalList) == 0:
            indexList.append(i)
        elif len(indexList) == 0: 
            above_num = finalList[-1][-1]
            indexList.append(above_num)
            while len(indexList) != i:
                next_num = indexList[-1]+finalList[-1][len(indexList)-1]
                indexList.append(next_num)
        finalList.append(indexList)
    return finalList

def printBell(x):
    for i in range(0, len(x)): 
        for j in range(0, i+1): 
            print(str(x[i][j]).rjust(8,' '),end="") 
        print("\r")

def main():
    invoice(unitPrice=20,quantity=4,shipping=8)
    invoice(unitPrice=15,quantity=3,handling=15)
    printGroupMembers("Group A", "Li", "Audry", "Jia")
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
    printGroupMembers(*groupB)
    x=buildBell(8)
    printBell(x)


if __name__== "__main__":
  main()
