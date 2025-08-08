from random import choice

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def make_list_of_free_fields(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['O', 'X']]

def victory_for(board, sign):
    win_lines = (
        [board[i] for i in range(3)] +  # rows
        [[board[i][j] for i in range(3)] for j in range(3)] +  # columns
        [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]  # diagonals
    )
    return any(all(cell == sign for cell in line) for line in win_lines)

def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            r, c = (int(move)-1)//3, (int(move)-1)%3
            if board[r][c] not in ['O', 'X']:
                board[r][c] = 'O'
                break
            else:
                print("Cell taken!")
        else:
            print("Invalid input!")

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        r, c = choice(free)
        board[r][c] = 'X'

board = [[str(3*r+c+1) for c in range(3)] for r in range(3)]
board[1][1] = 'X'
human_turn = True

while True:
    display_board(board)
    if human_turn:
        enter_move(board)
        if victory_for(board, 'O'):
            print("User won!")
            break
    else:
        draw_move(board)
        if victory_for(board, 'X'):
            print("Computer won!")
            break
    if not make_list_of_free_fields(board):
        print("Tie!")
        break
    human_turn = not human_turn