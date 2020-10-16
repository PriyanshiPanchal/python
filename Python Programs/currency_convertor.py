currencies = {
"BRL":"(Brazilian Real)",
"USD":"(US Dollar)",
"IND":"(Rupees)"
}

def real_to_dollar():
    user_value = input("How many brazilian reals? ")
    ammount = float(user_value)
    conversion = ammount * 0.26
    print(str(user_value) + " brazilian reals is equal to " + str(float(conversion)) + "$")

def rupees_to_dollar():
    user_value=input("How many rupees:")
    amount=float(user_value)
    conversion=amount*0.014;
    print(str(user_value)+"ruppes is to equals to:"+str(conversion)+"$")

def dollar_to_rupees():
    user_value=input("How many dollar(USD):")
    amount=float(user_value)
    conversion=amount*71.22;
    print(str(user_value)+"dollar is to equals to:"+str(conversion)+"Rs")

def dollar_to_real():
    user_value=input("How many USD(dollar):")
    amount=float(user_value)
    conversion=amount*4.08;
    print(str(user_value)+"USD is to equals to:"+str(conversion)+"R$")

def rupees_to_real():
    user_value=input("How many Rupees:")
    amount=float(user_value)
    conversion=amount*0.057;
    print(str(user_value)+"rupees is to equals to:"+str(conversion)+"R$")

def real_to_rupees():
    user_value=input("How many Brazilian Real:")
    amount=float(user_value)
    conversion=amount*17.45;
    print(str(user_value)+"brazilian rupees is to equals to:"+str(conversion)+"Rs")

print( "Welcome to currency converter.")
print ("Supported currencies:")
for currency in currencies:
    print(currency + " " + currencies[currency])

user_choice1 = input("Convert: ")
user_choice2 = input("To: ")

if user_choice1 == "BRL" and user_choice2 == "USD":
    real_to_dollar()

elif user_choice1 == "USD" and user_choice2 == "BRL":
    dollar_to_real()

elif user_choice1 == "IND" and user_choice2 == "USD":
    rupees_to_dollar()

elif user_choice1 == "USD" and user_choice2 == "IND":
    dollar_to_rupees()

elif user_choice1 == "IND" and user_choice2 == "BRL":
    rupees_to_real()

elif user_choice1 == "BRL" and user_choice2 == "IND":
    real_to_rupees()
