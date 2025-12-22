from random import choice
from time import sleep
from question_answer.question_answer import check_ready


many_time = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

check_win_o = []
check_win_x = []


win = [
    ["1", "2", "3"], ["4", "5", "6"], ["7","8","9"], # Rows
    ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"], # Columns
    ["1", "5", "9"], ["3", "5", "7"] # Diagonals
]


def main_x_o():
    print("=====  TIC‑TAC‑TOE  =====")
    print("The computer strikes first as O.")
    print("You fight back as X.")
    print("Only one of you will claim three in a row.")
    print("Every move matters. Every choice counts.\n")
    print_bored("", "")

    check_ready(input("Type 'Ready' to start: "))

    stars = 0
    r = 0

    """Main game loop"""
    while True:
        computer_guess = choice(many_time)         #computer random choice

        check_number("o", computer_guess) 

        if check_win(check_win_o, check_win_x) == True:  #chick if comueter win
            break

        if r == 4:
            print("It's a draw")                        #draw condition
            break   
        
        player_x = input("Enter the namber you want play: ") #taking player input
        if check_number("x", player_x) == False:
            while True:
                player_x = input("player 1: enter your namber:")    #validating input
                if check_number("x", player_x) == True:
                    break

        if check_win(check_win_o, check_win_x) == True:
            stars += 1                                          #win condition       
            break
        r += 1

    print("Stars you get:", stars)                 #printing stars earned, and returning stars
    return stars


def check_win(check_o, check_x):
    """chick win condition"""
    if len(check_o) >= 3 or len(check_x) >= 3:
        for i in win:                    
            if all(elem in check_o for elem in i):
                print("O win")
                return True
            elif all(elem in check_x for elem in i):
                print("X win")                       
                return True
        return False


def check_number(player_symbol, n):
    """Check if user input is valid, and print board"""
    for i in many_time:
        if i == n:
            many_time.remove(i)
            print_bored(player_symbol, n)
            return True
    print("Invalid move, try again.")
    return False


def print_bored(player_symbol, n):
    """Print the game board"""
    if player_symbol == "o":
        board[int(n) - 1] = "o"
        check_win_o.append(n)  
    elif player_symbol == "x":
        board[int(n) - 1] = "x"
        check_win_x.append(n)
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")
    sleep(1)


if __name__ == "__main__":
