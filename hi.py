n = int(input("Enter the value"))
if n%2!=0:
    print("Weird")
elif n%2==0:
    if n>=2 & n<=5:
        print("Not weird")
    elif n>=6 & n<=20:
        print("Weird")
    else:
        print("Not Weird")