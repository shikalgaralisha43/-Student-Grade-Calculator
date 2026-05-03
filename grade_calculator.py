# STUDENTS GRADE CALCULATOR 
#Students Name:
students=("alisha","aman","riya","kashish","rutuja")
#2D list:Students Marks:
marks=[[95,97,90,93],[60,54,40,45],[75,80,90,87],[66,60,70,55],
       [50,45,36,35]]
#loops[for loop]:
for i in range(len(students)):
#Average Formula:
    average=sum(marks[i]) / len(marks[i])
#Grade:
    if average>=90:
        grade="A"
    elif average>=80:
        grade="B"
    elif average>=70:
        grade="C"
    elif average>=60:
        grade="D"
    else:
        grade="F"
    print(f"name:{students[i]}")
    print(f"average:{average}")
    print(f"grade:{grade}")

