import random

# my solution:
# randomNumber = random.randint(1,20)
# n = 1
# number = 0
# print('I am thinking of a number between 1 and 20.')
# print('Take a guess!')
# number = int(input())
# while number != randomNumber:
#     if number < randomNumber:
#         print('Your guess is too low.')
#         print('Take a guess.')
#         number = int(input())
#         n = n + 1
#     else:
#         print('Your guess is too high.')
#         print('Take a guess')
#         number = int(input())
#         n = n + 1
# print('Good job! You guessed my number in ' + str(n) + ' guesses!')

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  #This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))