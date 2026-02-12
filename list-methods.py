numbers = [5,2,7,9,4]
numbers.remove(5)
print(numbers)

numbers = [5,2,7,9,4]
numbers.clear()
print(numbers)

numbers = [5,2,7,9,4]
numbers.pop()  #removes last number of list
print(numbers)

numbers = [5,2,7,9,4]
print(numbers.index(4))  #gives the index of the number

numbers = [5,2,7,9,4]
print(50 in numbers)

numbers = [5,2,7,9,4]
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [5,2,7,9,4]
number2=numbers.copy()
numbers.append(6)
print(number2)


numbers = [1,2,1,3,4,2,45,3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
