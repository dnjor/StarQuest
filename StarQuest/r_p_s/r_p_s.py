from random import choice
import time
from question_answer.question_answer import check_ready

"""The ruls"""
choese = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}


def main_r_p_s():
    print("\n==============================")
    print("     ROCK PAPER SCISSORS")
    print("==============================\n")
    print("Three choices. Infinite mind games.")
    print("Will you outsmart the computer or fall to its strategy?")          #display game intro
    print("Rock crushes Scissors, Scissors slices Paper, Paper traps Rock.")
    print("Choose your move… and let fate decide the winner!")

    check_ready(input("Type 'Ready' to start: "))

    stars = 0
    round = 1

    """Main game loop"""        
    while round <= 5:

        print(f"Round 5/{round}")
        for i in choese.keys():
            time.sleep(1)               #dramatic countdown
            print("-", i)
        time.sleep(1)
        print("Shoote!")

        player1 = check_input(input("Choose rock, paper, or scissors: ").title().strip()) #taking player input
        computer_choice = choice(list(choese.keys())) #computer random choice
        print(f"Computer chose: {computer_choice}")
        if player1 == computer_choice:                      #draw condition
            print("It's a draw!")
        elif choese[player1] == computer_choice:            #lose condition
            print("You lose!")
        else:
            print("You win!")
            stars += 1                                      #win condition   
        round += 1
    
    print("stars you get:", stars)                  #printing stars earned, and returning stars
    return stars
    

def check_input(user_choice):
    """Check if user input is valid"""
    while not user_choice.isalpha():
        print("It's not a string")
        user_choice = input("Choose rock, paper, or scissors: ").title().strip()
    if user_choice not in choese:
        print("Invalid input. Please choose rock, paper, or scissors.")
        return check_input(input("Choose rock, paper, or scissors: ").title().strip())
    return user_choice
    

if __name__ == "__main__":
