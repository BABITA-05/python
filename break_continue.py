#break statement
for n in range (2, 20):
    for x in range (2, n):
        if n%x==0:
            print(f'{n} is composite ({n} = {x}*{n//x})')
            break
    else:
        print(f'{n} is prime')



#continue statement
for n in range(2, 20):
    if n%2==0:
        print(f'{n} is even number')
        continue
    else:
        print(f'{n} is odd number')



#match
status = input("Enter your code")
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "i'm a teapot"
        case _:
            return "Something's wrong with an internet"








        


