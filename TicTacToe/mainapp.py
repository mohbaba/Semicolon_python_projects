from tictactoe import *

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? yes or no ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # player1
        if turn == 'Player1':
            display_board(board)
            position1 = player_choice(board)
            place_marker(board, player1_marker, position1)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations! Player1 wins!!!')
                game_on = False

            else:
                if fullboard_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player2'


        else:
            # player2

            display_board(board)
            position1 = player_choice(board)
            place_marker(board, player2_marker, position1)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations! Player2 wins!!!')
                game_on = False

            else:
                if fullboard_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player1'

    if not replay():
        break


