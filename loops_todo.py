"""
#for loops
for i in range(1, 5):
    print(i)

# while loops
i=1
while(i<=5):
    print(i)
    i=i+1

#break & continue
for i in range(1, 5):
    if i == 3:
        break #1 2 matra print hunxa
    print(i)

for i in range(2, 9):
    if i == 6:
        continue #skips 6

    print(i) 


#qn1
for i in range(1, 21):
    print(i)

#Qn2
for i in range(1, 51):
    while i%2==0 :
     print(i)
     i = i+1

#qn3
number = int(input("Enter a number:"))
for i in range(1, 11):
   print(number, "x", i, "=", number*i)
  


num = int(input("Enter a number you want multiplication table of:"))
for i in range(1, 11):
   print(num, "x", i, "=", num*i)   

#qn4
for i in range(1, 11):
   if i == 5:
      continue
   print(i)

#qn5
for i in range(1, 100):
   if i%7==0:
      break
   print(i)
#OR
i = 1
while True:
   if i%7 == 0:
      break
   print(i)
   i = i +1

   """
#total
total = 0
for i in range(1, 11):
    total = total+i
    print(total)












  
    
