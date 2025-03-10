# guess2.py
# this program tells the user if their guess is too high or too low, each time they guess the number. 
# HINT: put an if statement inside the while loop.


numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess <30:
        print ("Too Low")    
    else:
        print("too high")
    guess = int(input("Please guess again:"))
print("Well done! Yes the number was ", numberToGuess)


### get the program to generate a random number from 0 to 100.


import random
print(random.randrange(1,100))

