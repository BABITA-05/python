def fibo(n):
    """Print a fibonacci series less than n."""
    a,b = 0,1
    while a<n:
        print(a, end= ' ')
        a, b = b, a+b
    print()

fibo(10)

def fibo(n):
    a, b = 0, 1
    while a<n:
        print(a, end=" ")
        a, b = b, a+b
    print()
fibo(20)


#More on defining functions

#1 default argument values
def ask_ok(prompt, retries=4, reminder="Please try again later!"):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')


#default arguments are evaluated only once. When the function is defined, not when it is called. Here below, function is defined when i=5, and if i is assigned any other value like 6 below, still function f will print 5
i =5
def f(arg = i):
    print(arg)

i = 10
f()


#keyword arguments
def parrot(voltage, state='a stiff', action='vooom', type='suga'):
    print("--This parrot wouldn't", action, end=' ')
    print("--if you put", voltage, "volts through it.")
    print("--lovely plumage, the", type)
    print("--It's", state, "!")

parrot(100) #by default, python's print() ends with a newline but in above program, inside print() we have end = " ", so instead of ending with new line it ends with a space so 1 st and 2nd line are on same line in output 
parrot(voltage=10000)

def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-"*50)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
            "It's really very, Very runny, sir.", shopkeeper="Babita",
            client="Bijaya Ma'am", 
            sketch="Cheese Shop Sketch")

#special parameters
#symbols like '/' and '*' indicate the kind of parameters by how the arguments may be passed to the function:positional-only, positional-or-keyword, and keyword-only.
# in positional-or-keyword arguments, no symbols are present in the function, arguments may be passed to a function by positional.
#positional-only parameters, we use "/" and 
#keyword-only parameters, we use "*"


#function examples
def standard_arg(arg):
    print(arg)
standard_arg("babita")

def pos_only_arg(arg, /):  #Everything before / can ONLY be passed as positional arguments.
    print(arg)
pos_only_arg(2)

def kwd_only_arg(*, arg):  #everything after * can only be passed as keyword arguments.
    print(arg)
kwd_only_arg(arg=5)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
combined_example(1, 2, kwd_only=3)









