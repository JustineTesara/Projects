from random import choice

# Function to display the current board state
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to list all free (empty) fields on the board
def make_list_of_free_fields(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['O', 'X']]

# Function to check if the given sign ('O' or 'X') has won
def victory_for(board, sign):
    win_lines = (
        [board[i] for i in range(3)] +  # rows
        [[board[i][j] for i in range(3)] for j in range(3)] +  # columns
        [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]  # diagonals
    )
    # Return True if any line contains only the given sign
    return any(all(cell == sign for cell in line) for line in win_lines)

# Function for the human player to enter their move
def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        # Validate input
        if move.isdigit() and 1 <= int(move) <= 9:
            r, c = (int(move)-1)//3, (int(move)-1)%3
            # Check if the cell is free
            if board[r][c] not in ['O', 'X']:
                board[r][c] = 'O'  # Place 'O' for human
                break
            else:
                print("Cell taken!")
        else:
            print("Invalid input!")

# Function for the computer to make a move
def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        r, c = choice(free)  # Pick a random free cell
        board[r][c] = 'X'    # Place 'X' for computer

# Initialize the board with numbers 1-9
board = [[str(3*r+c+1) for c in range(3)] for r in range(3)]
board[1][1] = 'X'  # Computer starts with the center cell
human_turn = True  # Human goes first

# Main game loop
while True:
    display_board(board)  # Show the board
    if human_turn:
        enter_move(board)  # Human move
        if victory_for(board, 'O'):  # Check if human won
            print("User won!")
            break
    else:
        draw_move(board)  # Computer move
        if victory_for(board, 'X'):  # Check if computer won
            print("Computer won!")
            break
    if not make_list_of_free_fields(board):  # Check for tie
        print("Tie!")
        break
    human_turn = not human_turn  # Switch turns
