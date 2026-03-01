#similar to list but immutable(can't be changed or modified)
numbers = (1,2,3)
print(numbers[0])

"""numbers= (1,2,3,4,5)
numbers[0] = 10
print(numbers)     #error"""

t = 1234, 4567, 'hey!'
print(t[0])
print(t)
#tuples can be nested:
u = t, (1,2,3,4,5)
print(u)
#but we can't change the value so they are called immutable
#also they can contain mutable objects:
v = ([1,2,3], [4,5,6])
print(v)

empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)
