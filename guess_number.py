
number = 10
print("I'm thinking of a number...")

count = 5
while True:
    guess = input("What number am I thinking of? ")

    if guess == 'q':
        print(f'The number was {number}')    
        break
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    if guess != number:
        if int(guess) > number:
            print('Too high! Try again. ')
        if int(guess) < number:
            print('Too low! Try again ')
        count -= 1
        print(f'You have {count} guesses left.')
        if count == 0:
            print('You ran out of guesses')
            break








    if count == 0:
        break