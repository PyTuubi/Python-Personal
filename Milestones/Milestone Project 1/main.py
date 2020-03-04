# Tic Tac Toe

import random
import sys

mainBoard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def display_board(board):

    print("\n" + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def clear_board():

    print(' \n' * 100)

playerOne = ''
playerTwo = ''

def player_input():

    global playerOne
    global playerTwo
    tempBool = False

    while tempBool == False:
        playerOne = str(input('\nSelect X or O for player 1: '))
        if playerOne == 'X':
            playerOne = 'X'
            playerTwo = 'O'
            tempBool = True
        elif playerOne == 'O':
            playerOne = 'O'
            playerTwo = 'X'
            tempBool = True
        else:
            print('\nPlease input a valid character.')
            continue

def place_marker(board, marker, position):
    board[position] = marker

winCheck = False

def win_check(board, mark):
    
    global winCheck
    #if full_board_check != True:
    # Horizontal
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True

    # Vertical
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True

    # Diagonal
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True

    else:
        return False
        
startingPlayer = ''
secondPlayer = ''

def choose_first():

    global secondPlayer
    global startingPlayer

    randomNum = random.randint(0, 100)

    if randomNum <= 50:
        startingPlayer = str(playerOne)
        secondPlayer = str(playerTwo)
    else:
        startingPlayer = str(playerTwo)
        secondPlayer = str(playerOne)

def space_check(board, position):
    
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    
    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return True

chosenPos = 0

def player_choice(board):
    
    global chosenPos

    acceptedInts = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    

    tempBool2 = True

    while tempBool2 == True:

        inputChosenPos = str(input('\nPosition on board: '))

        if inputChosenPos.isdigit():
            if int(inputChosenPos) in acceptedInts:
                if space_check(mainBoard, int(inputChosenPos)) == True:
                    chosenPos = int(inputChosenPos)
                    tempBool2 = False
                else:
                    print('\nThat position is not empty')

        else:
            print('\nPlease input a number from 1-9.')
            

replayCheck = False

def replay():
    
    global replayCheck

    positiveAns = ['y', 'yes', 'Y', 'Yes', 'YES']
    negativeAns = ['n', 'no', 'N', 'No', 'NO']

    checkBool1 = False

    while checkBool1 == False:
        answer = str(input('\nReplay? [Y]es or [N]o: '))
        if answer in positiveAns:
            replayCheck = True
            checkBool1 = True
        elif answer in negativeAns:
            replayCheck = False
            checkBool1 = True
        else:
            print('\nPlease answer the question')
            continue
        
print('Welcome to Tic Tac Toe!')

while True:

    # Set the game up here
    display_board(mainBoard)
    player_input()
    print(f'\nPlayer one is now: {playerOne}\nPlayer two is now: {playerTwo}\n')
    choose_first()
    print(f'{startingPlayer} will start the game\n')
    display_board(mainBoard)

    game_on = True

    while game_on:
        # Player 1 Turn        

        print(f"\n{startingPlayer}s turn")

        player_choice(mainBoard)
        
        place_marker(mainBoard, startingPlayer, chosenPos)

        clear_board()

        display_board(mainBoard)
        
        if full_board_check(mainBoard) == True:
            if win_check(mainBoard, startingPlayer) == True:
                print(f"\n{startingPlayer} won the game")
                game_on = False
                break

            elif win_check(mainBoard, startingPlayer) == False:
                print("\nIt's a draw")
                game_on = False
                break

        elif win_check(mainBoard, startingPlayer) == True:
            print(f"\n{startingPlayer} won the game")
            game_on = False
            break


        # Player2's turn.

        print(f"\n{secondPlayer}s turn")

        player_choice(mainBoard)

        place_marker(mainBoard, secondPlayer, chosenPos)

        clear_board()

        display_board(mainBoard)

        if full_board_check(mainBoard) == True:
            if win_check(mainBoard, secondPlayer) == True:
                print(f"\n{secondPlayer} won the game")
                game_on = False
                break

            elif win_check(mainBoard, secondPlayer) == False:
                print("\nIt's a draw")
                game_on = False
                break

        elif win_check(mainBoard, secondPlayer) == True:
            print(f"\n{secondPlayer} won the game")
            game_on = False
            break

    if game_on == False:
        replay()
        if replayCheck == True:
            mainBoard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            game_on = True
        else:
            sys.exit("")

