# this  program allows a user to create new students and to view students.  
# write a function that prints out a menu of commands we can perform, 
# ie add, view and quit. 
# The function should return what the user chose.
# Test the function. 

# definening a function called menu using print
def fromMenu():
    print("What would you like to do?")
    print("(a) Add new student")
    print("(v) View students")
    print("(q) Quit")
    choice = input("Type one letter a or v or q :  ")

    return choice
#testing the function
# make a variable out of the argument needed
choice = fromMenu()
print(choice)

     