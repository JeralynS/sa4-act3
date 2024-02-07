
number = 10
print("I'm thinking of a number...")

count = 5
while True:
    guess = input("What number am I thinking of? ")

    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    if guess == 'q':
        print(f'The number was {number}')    
        break
    if guess != number:
         print(f'Incorrect guess. Try again.')






    if count == 0:
        break