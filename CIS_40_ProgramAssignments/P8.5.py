# P8.5 Johnny To
# Grade Logger
gradeList = {}
def addStudent():
    nameStu = input("Enter name:")
    grade = input("Enter grade:")
    gradeList[nameStu] = grade
    return "added"
def removeStudent():
    exitTrigger = True
    while exitTrigger:
        nameStu = input("Enter name:")
        if nameStu in gradeList:
            del gradeList[nameStu]
            exitTrigger = False
        else:
            print("Student not Found")
        return "REMOVED"
def modifyGrade():
    exitTrigger = True
    while exitTrigger:
        nameStu = input("Enter name:")
        if nameStu in gradeList:
            grade = input("New Grade: ")
            gradeList[nameStu] = grade
            exitTrigger = False
        else:
            print("Student not Found")
def printGrades():
    for names, grades in gradeList.items():
        print(names, grades)
def switch(argument):
    switcher = {
        1: addStudent,
        2: removeStudent,
        3: modifyGrade,
        4: printGrades,
    }
    func = switcher.get(argument)
    return func()


trigger = False
while trigger == False:
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Modify Student Grade")
    print("4. Print All Grades")
    print("0 --- END")
    argu = int(input("Enter an Option:"))
    if argu == 0:
        trigger = True
    elif argu > 4 or argu < 0:
        print("INVALID RESPONSE")
    else:
        switch(argu)

'''
OUTPUT
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:1
Enter name:Annie
Enter grade:AQ
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:2
Enter name:Annie
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:4
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:1
Enter name:JOhnny
Enter grade:A
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:1
Enter name:Annie
Enter grade:C
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:4
JOhnny A
Annie C
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:3
Enter name:Johnny
Student not Found
Enter name:Annie
New Grade: B
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:4
JOhnny A
Annie B
1. Add Student
2. Remove Student
3. Modify Student Grade
4. Print All Grades
0 --- END
Enter an Option:
'''