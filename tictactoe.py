# import sys
#
#  ---- WITHOUT FUNCTION ----
#
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#
#
# def clearBoard(board):
#     board = dict.fromkeys(board, ' ')
#     return board
#
#
# def printBoard(board):
#     print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
#     print('- + - + -')
#     print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
#     print('- + - + -')
#     print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])
#
#
# playAgain = True
#
# # print(theBoard)
# # theBoard['top-L'] = 'X'
# # print(theBoard)
# # theBoard = clearBoard(theBoard)
# # print(theBoard)
# # print(dict.fromkeys(theBoard))
#
#
# while playAgain:
#     moveList = []
#     count_X = count_O = 0
#     turn = 'X'
#     for i in range(9):
#         printBoard(theBoard)
#         print('Turn for ' + turn + '. Move on which space?')
#         if turn == 'X':
#             count_X += 1
#         else:
#             count_O += 1
#         move = input()
#
#         while move not in theBoard.keys() or move in moveList:
#             if move.lower() == 'exit':
#                 sys.exit()
#             if move in moveList:
#                 print('This coordinate is not empty. Pick another!')
#                 move = input()
#             else:
#                 print('You must enter a valid coordinate!')
#                 move = input()
#
#         moveList.append(move)
#
#         theBoard[move] = turn
#         # kodel neveikia su turn?
#         # if (theBoard['top-L'] and theBoard['top-M'] and theBoard['top-R']) == turn: # neveikia
#         # if all(theBoard['top-L'] and theBoard['top-M'] and theBoard['top-R']) == turn: # veikia
#         # if ((theBoard['top-L'] and theBoard['top-M'] and theBoard['top-R']) or
#         #     (theBoard['mid-L'] and theBoard['mid-M'] and theBoard['mid-R']) or
#         #     (theBoard['low-L'] and theBoard['low-M'] and theBoard['low-R'])) == 'X':
#         if (theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == turn) or \
#                 (theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] == turn) or \
#                 (theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == turn) or \
#                 (theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] == turn) or \
#                 (theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == turn) or \
#                 (theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] == turn) or \
#                 (theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == turn) or \
#                 (theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == turn):
#             printBoard(theBoard)
#             if turn == 'X':
#                 count = count_X
#             else:
#                 count = count_O
#             print(turn + ' has won the match in ' + str(count) + ' counts!')
#             print('Do you want to play again?')
#             play = input()
#             if play.lower() == 'yes':
#                 theBoard = clearBoard(theBoard)
#                 moveList.clear()
#                 break
#             elif play.lower() == 'no':
#                 playAgain = False
#                 break
#
#         if turn == 'X':
#             turn = 'O'
#         else:
#             turn = 'X'
#     else:
#         print('It is a tie!')
#         break




#  ---- WITH FUNCTION ----

import sys

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

helper = {'7': '7', '8': '8', '9': '9',
          '4': '4', '5': '5', '6': '6',
          '1': '1', '2': '2', '3': '3'}

# clears the board and returns new dict to theBoard in game()
def clearBoard(board):
    board = dict.fromkeys(board, ' ')
    return board


# prints the board
def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])


# calls clearBoard() with existing theBoard and returns cleared result to theBoard, which then passes to game()
def playAgain(theBoard):
    print('Do you want to play again?')
    play = input()
    if play.lower() == 'yes':
        theBoard = clearBoard(theBoard)
        moveList.clear()
        playGame(theBoard)
    elif play.lower() == 'no':
        sys.exit()


moveList = []


# start game with initial board fir the first time
# start game with cleared board from playAgain function other times
def playGame(theBoard):
    count_X = count_O = 0
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for: ' + turn + '. Choose a coordinate (press "h" for help)\n')
        if turn == 'X':
            count_X += 1
        else:
            count_O += 1
        move = input()

        while move not in theBoard.keys() or move in moveList:
            if move.lower() == 'exit':
                sys.exit()
            if move.lower() == 'help' or move.lower() == 'h':
                if theBoard.values():
                    for key, value in theBoard.items():
                        if value == 'X':
                            helper[key] = value
                        elif value == 'O':
                            helper[key] = value
                    printBoard(helper)
                else:
                    printBoard(helper)
            if move in moveList:
                print('This coordinate is already filled. Pick another!\n')
                move = input()
            else:
                print('You must enter a valid coordinate.\n')
                move = input()

        moveList.append(move)

        theBoard[move] = turn
        if (theBoard['7'] == theBoard['8'] == theBoard['9'] == turn) or \
                (theBoard['4'] == theBoard['5'] == theBoard['6'] == turn) or \
                (theBoard['1'] == theBoard['2'] == theBoard['3'] == turn) or \
                (theBoard['7'] == theBoard['4'] == theBoard['1'] == turn) or \
                (theBoard['8'] == theBoard['5'] == theBoard['2'] == turn) or \
                (theBoard['9'] == theBoard['6'] == theBoard['3'] == turn) or \
                (theBoard['7'] == theBoard['5'] == theBoard['3'] == turn) or \
                (theBoard['9'] == theBoard['5'] == theBoard['1'] == turn):
            printBoard(theBoard)
            if turn == 'X':
                count = count_X
            else:
                count = count_O
            print(turn + ' has won the match in ' + str(count) + ' tries!')
            playAgain(theBoard)

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        print('It is a tie!')
        printBoard(theBoard)
        playAgain(theBoard)


# start game with initial board
playGame(theBoard)