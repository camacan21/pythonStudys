import random
import os

# Funções
def display_board(board):
    print(f"                         {board[0]} | {board[1]} | {board[2]} ")
    print("                        ---+---+---")
    print(f"                         {board[3]} | {board[4]} | {board[5]} ")
    print("                        ---+---+---")
    print(f"                         {board[6]} | {board[7]} | {board[8]} ")


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('\nPlayer 1: Você quer ser X ou O? ').upper()

    if marker == 'X':
        return 'X','O'
    else:
        return 'O','X'


def place_marker(board, marker, move):
    board[int(move)] = marker

def win_check(board, marker):

    # Horizontal
    if board[0] == board[1] == board[2] == marker:
        return True
    elif board[3] == board[4] == board[5] == marker:
        return True
    elif board[6] == board[7] == board[8] == marker:
        return True

    # Vertical
    elif board[0] == board[3] == board[6] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True

    # Diagonal
    elif board[0] == board[4] == board[8] == marker:
        return True
    elif board[2] == board[4] == board[6] == marker:
        return True


def space_check(board, move):
    for index in board:
        if board[int(move)] == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            return True


def full_board_check(board):
    for index in board:
        if space_check(board, move):
            return False
    return True


def player_choice(board):
    move = input('\nQual será sua jogada? (0-8) ')
    check = space_check(board, move)
    if check == True:
        return move
    else:
        print('Essa posição está ocupada! Tente novamente!')
        player_choice(board)

def clear():
    os.system('cls')

# Variáveis
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
count = 0
game_on = True

# Início do jogo
print('         ********** Bem vindo ao jogo da velha **********\n')


while game_on:
    display_board(board)
    player = choose_first()
    player1_marker, player2_marker = player_input()
    print(player + ' começa')
    move = player_choice(board)
    if player == 'Player 1':
        place_marker(board, player1_marker, move)
        player = 'Player 2'
    else:
        place_marker(board, player2_marker, move)
        player = 'Player 1'

    clear()

    while game_on:
        if player == 'Player 1':
            print('Sua vez, ' + player)
            display_board(board)
            move = player_choice(board)
            place_marker(board, player1_marker, move),

            clear()

            if win_check(board,player1_marker):
                display_board(board)
                print('Você venceu, ' + player + '!!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Empate!')
                    break
                else:
                    player = 'Player 2'

        else:
            print('Sua vez, ' + player)
            display_board(board)
            move = player_choice(board)
            place_marker(board, player2_marker, move)

            clear()

            if win_check(board, player2_marker):
                display_board(board)
                print('Você venceu, ' + player + '!!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Empate!')
                    break
                else:
                    player = 'Player 1'
    game_on = False