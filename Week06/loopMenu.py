# this program keeps displaying the menu util the user picks q.
# if the user chooses a then call a function called doAdd() 
# if the user chooses v then call a function called doView().

# definening a function called menu using print
def fromMenu():
    print("What would you like to do?")
    print("(a) Add new student")
    print("(v) View students")
    print("(q) Quit")
    choice = input("Type one letter a or v or q :  ")
    return choice
def doAdd():
    print(" add a student")
    return choice
def doView():
    print("view a student")
    return choice


#testing the function
# make a variable out of the argument needed
choice = fromMenu()
if choice == "a":
    doAdd()
    choice = input("Type one letter a or v or q :  ")
elif choice == "v":
    doView()
elif choice == "q":
    print("quit")