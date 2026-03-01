#it is another built in data type in pyhton that stores key:value pair
price = {'apple':300, 'banana':150}
price['pear']=200   #can be modified like we can add key value anytime
print(price)
del price['apple']
print(price)

price['mango'] = 250
print(price)
fruit = list(price)
print(fruit)
fruit = sorted(fruit)
print(fruit)

# the dict() builds dictonaries directly
fruits = dict([('apple', 300), ('banana', 150)])
print(fruits)
#can also be created as this way
fruits = dict(apple=300, banana=150, mango=200)
print(fruits)

square = {x: x**2 for x in (2,4,6)}
print(square)