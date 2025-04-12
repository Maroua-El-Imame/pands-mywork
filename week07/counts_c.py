# Lab Topic 07-Files

# Write a program that, uses these two functions, to count how many times the program has been run. 
#Test it, check to see that the number goes up each time.

# correction


FILENAME = "count.txt"                          
def readNumber():                                    # reads the number from the file
    with open(FILENAME) as f:
        number = int(f.read())
    return number                                    # return the actual number

def writeNumber(number):                             # the function opens file in write mode 
    with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
        f.write(str(number))                        # write the number as a string to this file

# main
num = readNumber()
num += 1
print(f"we have run this program {num} times")      # the program return the num+1 that wiill written again in the same file count.txt
writeNumber(num)