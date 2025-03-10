

def collatz(number):
    if number % 2 == 0:
        numberList.append(number // 2)
        return(number // 2)
    elif number % 2 == 1:
        result = 3 * number + 1
        numberList.append(result)
        return(result)

# Program starts here.        

number = int(input('Please enter a number: '))
numberList = [number]
        
        #If number is applicable, goes through collatz function.
while number != 1:
            number = collatz(int(number))
else:
         print(numberList, end="")
        
        