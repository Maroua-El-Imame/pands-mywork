

# messing around with codes 

accountnumber= "1234567890"
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
