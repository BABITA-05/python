for item in 'Python':
    print(item)

for item in ['babita', 'bijaya', 'asmita']:
    print(item)

#for creating range of numbers
for item in range(10):
 print(item)  #print from 0 to 9

for item in range(1, 10):
   print(item)   #print from 1 to 9 as it has starting value 1

for item in range(1, 10, 2):
   print(item)  #print from 1 to 9 but with difference of 2

prices = [10, 20, 30]
total = 0
for price in prices:
   total = total + price
print(f'total:{total}')


#count the number of letters of each words
word = {"Babita", "Bijaya", "Asmitaa Bhandari"}
for w in word:
   print(w,":", len(w))