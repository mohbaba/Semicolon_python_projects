from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player1 do you want to be  'X' or 'O'? ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def choose_first():
    if random.randint(0, 1) == 0:
        return ('Player1')
    else:
        return ('Player2')


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark))


def place_marker(board, marker, position):
    board[position] = marker


def space_check(board, position):
    return board[position] == ' '


def fullboard_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def replay():
    choice = input("Play again?").lower().startswith('y')


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or space_check(board, position):
        position = int(input('Please choose position(1-9)'))

    return position


