# guess,py
# this program prompts the user to guess a number, the program kepps prompting the user to guess the number until the user gets the right on
# Author: Maroua EL imame



number = input("Please guess the number: ")
while number != "30":
    print ("Wrong")
    number = input("Please guess again: ")
print("Well done! Yes the number was " + number)


# needs more focus 
numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
print ("Well done! Yes the number was ", numberToGuess)
