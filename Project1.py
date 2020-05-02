import random


def display_board(board):
    print('\n' * 1000)
    print('\n' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1 please choose symbol "X" or "O" :').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return board[1] == board[2] == board[3] == mark or \
           board[4] == board[5] == board[6] == mark or \
           board[7] == board[8] == board[9] == mark or \
           board[1] == board[4] == board[7] == mark or \
           board[2] == board[5] == board[8] == mark or \
           board[3] == board[5] == board[9] == mark or \
           board[1] == board[5] == board[9] == mark or \
           board[3] == board[5] == board[7] == mark


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please enter position from "1" to "9" :'))

    return position


def replay():
    choice = input('Do you want play more? "Yes" or "No" :')

    return choice == 'yes' or choice == 'Yes'


while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' is first')

    play_game = input('Are you reade to start game? Yes or No: ')

    if play_game == 'Yes' or play_game == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            print(position)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 won')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Draw')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            if turn == 'Player 2':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 won')
                    game_on = False

                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Draw')
                        game_on = False
                    else:
                        turn = 'Player 1'

    if not replay():
        break
