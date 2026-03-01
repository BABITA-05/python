squares = []

for i in range(5):
    squares.append(i**2)
print(squares)

#the above code overwrites so we simply do
squares = [i**2 for i in range(9)]
print(squares)

comb = []
for a in [1,2,3]:
    for b in [3,1,4]:
        if a!=b:
            comb.append((a,b))
print(comb)
#this above code can be written in simple 2 lines, like this way
combs = [(a,b) for a in [1,2,3] for b in [3,1,4] if a!=b]
print(combs)

vec = [-2, -1, 0, 1, 2]
print(vec)
vec = [i*2 for i in vec]
print(vec)
#vec = [i for i in vec if i>=0]
#print(vec)
vec = [abs(i) for i in vec]  #it actually return the absolute value, -ve xa bhane ni sign remove gardinxa
print(vec)

#let's create a list of 2 tuples like (num, sqr)
num = []
num = [(x, x**2) for x in range(10)] #tuples are denoted by small bracket where list is denoted by big bracket ani tuples sanga work garda we must use parenthesis
print(num)


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
matrix = [[row[i] for row in matrix] for i in range(3)]
print(matrix)
#simply this can be done in another way too

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
transposed = []
for i in range(3):
    transposed.append([row[i] for row in matrix])

print(transposed)


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
matrix = list(zip(*matrix))
print(matrix)


