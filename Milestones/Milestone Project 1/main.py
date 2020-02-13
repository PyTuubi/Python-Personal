# Tic Tac Toe

import random

mainBoard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def display_board(board):
    '''
    Print board
    '''

    print("\n" + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)


def clear_board():
    '''
    Clear board
    '''

    print(' \n' * 100)


playerOne = ''
playerTwo = ''

def player_input():
    '''
    Assign markers to players
    '''

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

#player_input()
#print(f'Player one is now: {playerOne}\nPlayer two is now: {playerTwo}')


def place_marker(board, marker, position):
    board[position] = marker

#place_marker(mainBoard,'$',int(input('Position on board: ')))
#display_board(mainBoard)


def win_check(board, mark):
    '''
    Check if someone won
    '''

    if full_board_check != True:
    # Horizontal
        if board[1] == mark and board[2] == mark and board[3] == mark:
            print(f'{mark} wins!')
        elif board[4] == mark and board[5] == mark and board[6] == mark:
            print(f'{mark} wins!')
        elif board[7] == mark and board[8] == mark and board[9] == mark:
            print(f'{mark} wins!')

    # Vertical
        elif board[1] == mark and board[4] == mark and board[7] == mark:
            print(f'{mark} wins!')
        elif board[2] == mark and board[5] == mark and board[8] == mark:
            print(f'{mark} wins!')
        elif board[3] == mark and board[6] == mark and board[9] == mark:
            print(f'{mark} wins!')

    # Diagonal
        elif board[1] == mark and board[5] == mark and board[9] == mark:
            print(f'{mark} wins!')
        elif board[3] == mark and board[5] == mark and board[7] == mark:
            print(f'{mark} wins!')

        else:
            print("\nIt's a draw")
        
    
#win_check(test_board,'O')

startingPlayer = ''
secondPlayer = ''

def choose_first():
    '''
    Assing the starting player
    '''

    global secondPlayer
    global startingPlayer

    randomNum = random.randint(0, 100)

    if randomNum <= 50:
        startingPlayer = str(playerOne)
        secondPlayer = str(playerTwo)
    else:
        startingPlayer = str(playerTwo)
        secondPlayer = str(playerOne)

#player_input()
#choose_first()
#print(f'{startingPlayer} will start the game')


def space_check(board, position):
    
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    
    if board[1] != '' and board[2] != '' and board[3] != '' and board[4] != '' and board[5] != '' and board[6] != '' and board[7] != '' and board[8] != '' and board[9] != '':
        return True

    # Run win check now for the last time

chosenPos = 0

def player_choice(board):
    
    global chosenPos

    acceptedInts = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    chosenPos = int(input('\nPosition on board: '))

    while True:
        if chosenPos in acceptedInts:
            if space_check(board, chosenPos) == True:
                return True
            else:
                print('\nThat position is not empty')
                break
        else:
            print('\nPlease input a number from 1-9.')
            break

replayCheck = False

def replay():
    
    global replayCheck

    positiveAns = ['y', 'yes']
    negativeAns = ['n', 'no']

    #answer = str(input('Replay? [Y]es or [N]o: '))
    checkBool1 = False

    while checkBool1 == False:
        answer = str(input('\nReplay? [Y]es or [N]o: '))
        if answer.lower in positiveAns:
            replayCheck = True
            checkBool1 = True
        elif answer.lower in negativeAns:
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
    print(f'{startingPlayer} will start the game')

    game_on = True

    while game_on:
        # Player 1 Turn
        player_choice(mainBoard)
        
        place_marker(mainBoard, startingPlayer, chosenPos)

        display_board(mainBoard)
        
        win_check(mainBoard, startingPlayer)

        # Player2's turn.
        player_choice(mainBoard)

        place_marker(mainBoard, secondPlayer, chosenPos)

        display_board(mainBoard)

        if win_check == 
        

    #if not replay():
        #break
