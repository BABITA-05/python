is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


#to do
price = 1000000
has_goodCredit = False
if has_goodCredit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down payment: ${down_payment}")


#logical operator
#=> and
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")


#=>not
has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")



#comparison operator
temperature = 30
if temperature>30:
    print("It's a hot day")
else:
    print("It's not a hot day")
  
#Eg:
 
name = 'Babita'
if len(name) < 3:
    print("Name must be at least 3 character")
elif len(name) > 50:
    print("Name must be maximun of 50 characters")
else:
    print("name looks good")


#weight converter


what = input("What is your name?")
print("Hi!" + what)
color = input("What is your favourite color?")
print(what+ " your favourite color is "+color)
weight = input("What is your weight in pound?")
weight_kg = int(weight) * 0.45
print("You are " + str(weight_kg) + "kg sooo ali khane garr")



weight = int(input('Weight:'))
unit = input('(L)bs or (k)g:')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"YOu are {converted} pounds")









