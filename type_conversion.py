birth_year = input('Birth year:')
print(type(birth_year))
age = 2026 - int(birth_year)
print(type(age))
print(age)

#ask a user their weight(in pounds), convert it to kg and print on the terminal
weight_pound = input('what is your weight, in pounds?')
weight_kg = int(weight_pound) * 0.4535
print('you are ' + str(weight_kg) + ' kg')