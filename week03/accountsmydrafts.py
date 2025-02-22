

# messing around with codes 

accountnumber= "1234567890"
'''
lastfourdigits=accountnumber[6:]
print("The account number is: " + accountnumber )


first6digits=accountnumber[0:6]

print("The account number is: " + accountnumber )
print("its 6 first digits are: " + first6digits)
print("its 4 last digits are: " + lastfourdigits)


print(accountnumber)
print(lastfourdigits)
print(first6digits)

x= first6digits
y= lastfourdigits

###

z=accountnumber.replace("123456" , "xxxxxx")
print("Account number only showing last for digits is : " + z)

enter10digitsaccountnumber = input("Enter your account number:")
print(z)

z=accountnumber.replace(accountnumber[6:0] , "xxxxxx") interesting 

accountnumber= "1234567890"

print(accountnumber[6:])
accountnumber4digits = accountnumber.replace(accountnumber[0:6] , "xxxxxx")
print(accountnumber4digits)
'''
accountnumber= "1234567890"

accountnumber= input("Enter your account number of 10 digits:")
z=accountnumber.replace(accountnumber[0:6] , "xxxxxx")
print("Your account number's last 4 digits : " + z)




randomnumber = "1236547896541236654478963225"
randomnumber= input("Enter yout account number of any length: ")
y=randomnumber.replace(randomnumber[:-4],"xxxxxx")
print("your account number's last 4 digits : " + y)