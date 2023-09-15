# number guessing game with random library
import random

secretNumber = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")
# ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print("Your guess was too low!")
    elif guess > secretNumber:
        print("Your guess was too high!")
    else:
        break #because we guessed the number
if guess == secretNumber:
    print("Nicely done! You guessed my number in " + str(guessesTaken) + " tries!")
else:
    print("Sorry. The number I was thinking of was " + str(secretNumber))