# grade.py
# This program reads in a students percentage and prints out the corresponding grade
# Author : Maroua EL imame

'''
Ref : 
Under 40% => Fail
Between 40% and 49% => Pass
Between 50% and 59% => Merit 2
Between 60% and 69% => Merit 1
Over 70% => Distinction
'''

percentage = float(input("Enter the percentage: "))
#print (percentage)

# be careful with ands and ors
if percentage < 0 or percentage > 100:
                                         # Later we will show you error handling
                                            # This should really throw an error
    print ("Please enter a number between 0 and 100")
elif percentage < 40:                 # we know it is greater than 0
    print ("Fail")
elif percentage < 50:                # between 40 and 49
    print ("Pass")
elif percentage < 60:               # between 50 and 59
    print ("Merit1")
elif percentage < 70:               # between 60 and 69
    print ("Merit2")
else: # the only option left
     print ("Distinction")


# using the built in function round (), will round the student percentages so they're allocated the corresponding grades.
# The program is as below :


percentage = float(input("Enter the percentage: "))
if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif round(percentage) < 40:                
    print ("Fail")
elif round(percentage) < 50:               
    print ("Pass")
elif round(percentage) < 60:              
    print ("Merit1")
elif round(percentage) < 70:              
    print ("Merit2")
else: 
     print ("Distinction")


# I've kept both functions so the 1st one prints the incorrect grade, while the 2nd one prints the correct grade.