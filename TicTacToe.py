import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN = 5
WHO_GOES_FIRST = ""

def prompt(message):
    print(f"==> {message}")

def display_board(board):
    os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

# def join_or(sequence, delimiter=', ', word='or'):
#     match len(sequence):
#         case 0:
#             return ''
#         case 1:
#             return str(sequence[0])
#         case 2:
#             return f"{sequence[0]} {word} {sequence[1]}"

#     leading_items = delimiter.join(str(item) for item in sequence[0:-1])
#     return f'{leading_items}{delimiter}{word} {sequence[-1]}'

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def add_number(input_lst, punctu=',', conjun='or '):
    if len(input_lst) == 0:
        return []
    if len(input_lst) == 1:
        return "".join(input_lst)
    if len(input_lst) == 2:
        return f"{input_lst[0]} {conjun}{input_lst[1]}"
    else:
        a = [str(num) + punctu if num in input_lst[0:-1] else conjun + str(num) for num in input_lst]
        punctu = ','
        conjun = 'or '
        return " ".join(a)

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({add_number(valid_choices)}):")
        
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0



def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER 
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def someone_won(board):
    return bool(detect_winner(board))

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    defend_lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    

    for section in defend_lines:
        sq1, sq2, sq3 = section
        if (board[sq3] == COMPUTER_MARKER and board[sq2] == COMPUTER_MARKER and board[sq1] == INITIAL_MARKER):
            board[sq1] = COMPUTER_MARKER
            return
        if (board[sq3] == COMPUTER_MARKER and board[sq2] == COMPUTER_MARKER and board[sq1] == INITIAL_MARKER):
            board[sq1] = COMPUTER_MARKER
            return
        if (board[sq1] == HUMAN_MARKER and board[sq2] == HUMAN_MARKER and board[sq3] == INITIAL_MARKER):
            board[sq3] = COMPUTER_MARKER
            return
        if (board[sq3] == HUMAN_MARKER and board[sq2] == HUMAN_MARKER and board[sq1] == INITIAL_MARKER):
            board[sq1] = COMPUTER_MARKER
            return
        
    if board[5] == INITIAL_MARKER:
        board[5] = COMPUTER_MARKER
        return
        
        
    board[random.choice(empty_squares(board))] = COMPUTER_MARKER 
    # else:
    #     square = random.choice(empty_squares(board))
    #     board[square] = COMPUTER_MARKER
    #     return

def choose_square(square, g_player):
    if g_player == "Computer":
        computer_chooses_square(square)
    else:
        player_chooses_square(square)
    pass

def alternate_player(g_player):
    if g_player == "Computer":
        g_player = "Player"
        return g_player
    else:
        g_player = "Computer"
        return g_player
            

def play_tic_tac_toe():
    computer_win_counter = 0
    player_win_counter = 0

    
    while True:
        player_choice = int(input("Enter 1 to go first or 2 to go second: "))
        if player_choice not in [1, 2]:
            print("Invalid Choice")
        if player_choice == 2:
            current_player = "Computer"
            board = initialize_board()

            while True:
                display_board(board)
    
                choose_square(board, current_player)
                current_player = alternate_player(current_player)
                if someone_won(board) or board_full(board):
                    break
                

                # computer_chooses_square(board)
                # if someone_won(board) or board_full(board):
                #     break
                
                # player_chooses_square(board)
          

                # if someone_won(board) or board_full(board):
                #     break
            
                

            if someone_won(board):
                if detect_winner(board) == "Computer":
                    computer_win_counter += 1
                else:
                    player_win_counter += 1
                prompt(f"{detect_winner(board)} won game!")
            else:
                prompt("It's a tie!")
        
            if computer_win_counter == 5 or player_win_counter == 5:
                prompt(f"{detect_winner(board)} won match!")
                computer_win_counter = 0
                player_win_counter = 0

                

                prompt("Play again? (y or n)")
                answer = input()
                
                
                while answer not in ['y', 'Y', 'n', 'N']:
                    answer = input("Invalid input please input y or n")
                        
                if answer in ['n', 'N']:
                    break


                prompt('Thanks for playing Tic Tac Toe!')

        if player_choice == 1:
            current_player = "Player"
            board = initialize_board()

            while True:
                display_board(board)
                choose_square(board, current_player)
                current_player = alternate_player(current_player)


                if someone_won(board) or board_full(board):
                    break
            
                

            if someone_won(board):
                if detect_winner(board) == "Computer":
                        computer_win_counter += 1
                else:
                    player_win_counter += 1
                prompt(f"{detect_winner(board)} won game!")
            else:
                prompt("It's a tie!")
        
            if computer_win_counter == 5 or player_win_counter == 5:
                prompt(f"{detect_winner(board)} won match!")
                computer_win_counter = 0
                player_win_counter = 0

                prompt("Play again? (y or n)")
                answer = input()
               
                while answer not in ['y', 'Y', 'n', 'N']:
                    answer = input("Invalid input please input y or n")
                        
                    
                if answer in ['n', 'N']:
                    break

                prompt('Thanks for playing Tic Tac Toe!')

# Call the main game function
play_tic_tac_toe()