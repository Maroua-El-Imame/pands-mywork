'''
 Write a program that will read in the data for the data structure above, ie
reads in a student’s name, then keeps reading in their modules and grades
(until the user enters a blank module name),
You can break this up into two parts:
a. Just read in the module names until the user enters blank,
b. Then read in the grade as well
This program can just read in one student (and their module details).
6. If you want to go a step further, read in multiple students (until the
student_name is blank.
Next week we will be looking at functions and we will implement something
like this.
'''

students = {
"name":"Mary",
"modules": [
    {
        "courseName":"Programming",
        "grade": 45
    },
    {
        "courseName":"History",
        "grade":99
    }
]}

students["name"] = input("enter your name : ")
while students["name"] != "Mary":
    print("not found")
    students["name"] = input("Please, enter a valid name : ")
if students["name"] == "Mary":
    for module in students["modules"]:
        students["modules"] = input("enter a module name: ")
        #while  students["modules"] == " ":
            #print("empty module name is unauthorized ")
        if module["courseName"] == "Programming":
            print(module["courseName"],"'s module grade is : ", module["grade"])
            students["name"] = input("enter an other module name : ")
        elif module["courseName"] == "History":
            print(f"{module["courseName"]},'s module grade is : ", {module["grade"]})
            students["name"] = input("enter an other module name : ")
    