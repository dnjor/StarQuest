from r_p_s.r_p_s import main_r_p_s
from question_answer.question_answer import main_question_answer
from x_o.x_o import main_x_o
from guess.guess import main_guess

from random import shuffle
from time import sleep

games = [main_r_p_s, main_x_o, main_guess, main_question_answer]
shuffle(games)
def main():
    print("Welcome to the Mini-Game Collection!")
    print("There are 4 games available")
    print("And you need to close as many stars as you can get")
    print("You will play aginst the computer in each game.")

    print("Before we start, You need type your name:")
    player_name = input("Your name: ").strip()
    print(f"Hello, {player_name}.")

    stars = 0
    try:
        for game in (games):
            stars += game()
            sleep(1)
    except KeyboardInterrupt:
        pass
    

    print(f"You have collected a total of {stars} stars. Thanks for playing!")

    with open("stars.txt", "a") as file:
        file.write(f"{player_name}: {stars} stars\n")

if __name__ == "__main__":
    main()
