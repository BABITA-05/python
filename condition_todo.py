 #qn1
age = int(input("What is your age?"))
if age >= 0 and age<= 12:
    print("You are a kid")
elif age>= 13 and age<=19:
    print("You are a teenager")
else:
    print("You are an adult")

#qn2
num = int(input("Enter a number to be checked:"))
if num%3 == 0 and num%5 == 0:
    print("Number is divisible by 3 and 5")
elif num%3 == 0:
    print("Number is only divisible by 3")
elif num%5==0:
    print("Number is only divisible by 5")
else:
    print("Number is not divisible by 3 and 5")

#qn3
marks = int(input("Enter your marks:"))
if marks>100 or marks<0:
    print("Invalid marks has been entered")
elif marks>=90 and marks<=100:
    print("You secured grade 'A'")
elif marks>=80 and marks<=89:
    print("You secured grade 'B'")
elif marks>=70 and marks<=79:
    print("You secured grade 'C'")
elif marks>=60 and marks<=69:
    print("You secured grade 'D'")
else:
    print("You secured below 60")


