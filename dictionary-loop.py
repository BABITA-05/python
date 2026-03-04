#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
fruits = {'apple':400, 'banana':150}
for k, v in fruits.items():
    print(k, v)


#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favourite color']
answers = ['Babita', 'the holy grail', 'black']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

whatIWant = ['the most', 'to be', 'to do']
answer = ['love', 'kind and loved', 'whatever i like']
for w, a in zip(whatIWant, answer):
    print('What do you want {0}? {1}.' .format(w,a))


#to loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for b in reversed(range(1, 10, 2)):  #from 1 to 9 with difference 2
    print (b)

#similarly, for sorting things we can use sorted()
bag=['apple', 'orange', 'banana', 'kiwi', 'orange']
for b in sorted(bag):
    print (b)

#similarly, for eliminating duplicate elements we use set() with sorted()
bag=['apple', 'orange', 'banana', 'kiwi', 'orange']
for b in sorted(set(bag)):
    print (b)

#for filtering data
import math
raw_data = [34.2, float('NaN'), 56.1, 45, 56.1, float('NaN'), 47.3]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
