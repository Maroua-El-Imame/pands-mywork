# Lab Topic 07-Files

# b. Look at the program below, if the file test-b.txt does not exist, what will be outputted to the console when this program is run?
# Answer:
# if run the file will be created in this same repository, as the module used is "w": write

# c. What will the contents of the file test-b.txt be when this program is run?
# the program will be overwritten when opened in write mode, it will return the txt in f2.write ' another line'


# the with statement will automatically close the file
# when it is finished with it
with open("test-b.txt", "w") as f:
 data = f.write("test b\n") # returns the number of chars written
print (data)
with open("test-b.txt", "w") as f2: # open file again
 data = f2.write("another line\n")
 print (data)
