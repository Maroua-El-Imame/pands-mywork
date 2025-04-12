# Lab Topic 07-Files

#Write a program that counts how many times it was run.
# For this exercise will have to store data outside of memory, and that is accessible each time the program is run, (persistent data).
# We would normally use adatabase for something like this, but we can use a file.
# To make life easier let’s assume that the file already exists. So, we can just read the current count from it then overwrite it with the new count.

# answer:
# we created a file "count.txt"
# Write a function that reads in a number from a file that already exists (count.txt). test the program by calling the function and outputting the number.


FILENAME = "count.txt"
def readNumber():                  
 with open(FILENAME) as f:
    number = int(f.read())
    return number
# test it
num = readNumber()
print (num)

#nb
#!!!Remember last  week I said, in functions, only  use data that was passed in as an argument.


# explained :
# a fille in all capitals as constant, is written all caps to signal that they should not be chanegd once defined.
# the function here bellow, is using FILENAME 
# def readNumber():
 #with open(FILENAME) as f:
    #number = int(f.read())
    #return number
# this rule is applicable exceptionnaly when using a constant we dont plan to change.

# code explained :
# FILENAME = "count.txt"            variable assigned to file name
# readNumber():                     The function doesnt take parameters but uses FILENAME
# with open(FILENAME) as f:         it opens the file
# int(f.read())                     num converts the content to an intger

# !!!Here. I am breaking that rule. I am using a variable that I want to treat as a constant (FILENAME) so I am putting all in capitals. 
# I do not change this variable.

# Write a function that takes in a number and overwrites a file with that number (count.txt). 
# test it and check that the file has been changed

def writeNumber(number):
    with open(FILENAME, "wt") as f:                 # see xcl note line 38 
 # write takes a string so we need to convert
        f.write(str(number))
# test it
writeNumber(3)


# we dont change the constant later
# if we want to change it, it would be passed as an argument instead

