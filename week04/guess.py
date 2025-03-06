


number = input("Please guess the number: ")
while number != "30":
    print ("Wrong")
    number = input("Please guess again: ")
print("Well done! Yes the number was" + number)


# needs more focus 
numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
print ("Well done! Yes the number was ", numberToGuess)
