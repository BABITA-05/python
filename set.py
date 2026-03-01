bag = {'apple', 'banana', 'pear', 'orange', 'apple' }
print(bag) #set is unordered so junai element pani printt huna sakxa, it won't appear the way we entered element

print('orange' in bag)
print('kiwi' in bag)

a = set('applsdsds')
b = set('hdjasideas')
print(a)
print(b)
print(a-b)  #element which is present only in a not in b
print(a|b)   #element in a or b or both, it's union
print(a & b)  #element which is present in both
print(a^b)   #element in a or b but not in both

a = {x for x in 'applsdsds' if x not in 'abcde' }
print(a)
a = {x for x in 'applsdsds' if x in 'abcde' }
print(a)