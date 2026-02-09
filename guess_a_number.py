secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit : 
    guess = int(input('Guess any number:'))
    guess_count = guess_count + 1
    if guess == secret_number:
        print("You guess right!")
        break
else:
    print("Sorry, you failed!")



