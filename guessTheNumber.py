# this is a guess the nmber game.
import random
secretNumber = random.randint(1, 20)
print('I am thnking of a number betweeen 1 and 20.')

# ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # This condition is the corect guess!

    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + 'guess!')
    else:
        print('Nope. The number I was thnking of was ' + str(secretNumber))