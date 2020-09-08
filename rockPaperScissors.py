import random, sys

print('Rock, Paper, Scissors GAME')

wins = 0
losses = 0
ties = 0
userMove = ""

while True:  # main game loop
    print('\n%s Wins, %s Losses, %s Ties' % (wins, losses, ties))  # print overall
    while True:  # user input loop
        print('\nEnter your move [ (R/r)ock, (P/p)aper, (S/s)cissors or (Q/q)uit ]: ')
        userMove = input()  # user enters move
        # print user choice
        if userMove.lower() == 'r':
            print('ROCK versus...')
            break
        elif userMove.lower() == 'p':
            print('PAPER versus...')
            break
        elif userMove.lower() == 's':
            print('SCISSORS versus...')
            break
        elif userMove.lower() == 'q':
            sys.exit()
        else:
            print('You must choose between Rock (R/r), Paper (P/p), Scissors (S/s) or Quit Game (Q/q) \n')

    # print computer's move
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        compMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        compMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        compMove = 's'
        print('SCISSORS')
    # print result
    if userMove.lower() == compMove:
        print('It is a tie!')
        ties = ties + 1
    elif userMove.lower() == 'r' and compMove == 's':
        print('You win!')
        wins = wins + 1
    elif userMove.lower() == 'r' and compMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif userMove.lower() == 's' and compMove == 'r':
        print('You lose!')
        losses = losses + 1
    elif userMove.lower() == 's' and compMove == 'p':
        print('You win!')
        wins = wins + 1
    elif userMove.lower() == 'p' and compMove == 'r':
        print('You win!')
        wins = wins + 1
    elif userMove.lower() == 'p' and compMove == 's':
        print('You lose!')
        losses = losses + 1