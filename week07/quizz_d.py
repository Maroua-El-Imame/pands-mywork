# Lab Topic 07-Files

# d. Look at the modified program below, what will the contents of the file be after this program is run.
# answer:
# the contents of the file after the program is run, will be two lines, where each line shows the number of characters that we rquested to be written.
# using the append mode it makes the program run witout being overwritten

# The with statement will automatically close the file
# when it is finished with it
with open("test-d.txt", "w") as f:
 data = f.write("test d\n") # returns the number of chars written
 print (data)
with open("test-d.txt", "a") as f2: # open file again
 data = f2.write("another line\n")
 print (data)