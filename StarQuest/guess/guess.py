from random import randint
from time import sleep
from question_answer.question_answer import check_ready


def main_guess():
    print("\n==============================")
    print("     NUMBER GUESSING GAME")
    print("==============================\n")
    print("You will play 3 levels:")
    print("Level 1: Guess a number from 1 to 10")
    print("Level 2: Guess a number from 1 to 100")
    print("Level 3: Guess a number from 1 to 1000\n")

    check_ready(input("Type 'Ready' to start: ")) #If the user want to continue or leave

    stars = 0
    level = 1
    computer_guess_number = None
    random_number = None

    while level <= 3:  #Looping for the three level

        if not random_number:
            random_number = choose_number(level)

        user_input = check_input(input("Your guess: "))         #Checking if the input, like what wc excepted
        user_guess = guess_player(random_number, user_input)

        if user_guess == "correct":
            print(f"Round {level}: You win!")
            level +=1
            stars += 1                 #Update level, and clean the varibal
            random_number = None
            print_round(level)
            continue 

        sleep(1)

        while computer_guess_number == None:
            computer_guess_number = checking_computer_guess(level)  #give random number to the computer

        print(f"The computer guess: {computer_guess_number}")

        computer_guess = guess_player(random_number, int(computer_guess_number)) #check if the computer's guess is correct

        if computer_guess == "correct":
            print(f"Round {level}: Computer wins!")
            level +=1                   #Update  level, and clean the varibal                
            random_number = None
            computer_guess = None
            print_round(level)
            continue

        elif computer_guess == "low":
            computer_guess_number = randint(computer_guess_number, random_number)   # Update the computer's guess range
        elif computer_guess == "high":
            computer_guess_number = randint(random_number, computer_guess_number)

        sleep(1)

    print("stars you get:", stars) #show how meny stars he get
    return stars


def guess_player(random_number, the_guess):
    """Check and help the player"""
    if random_number == the_guess:
        return "correct"
    elif random_number > the_guess:
        print("low!")
        return "low"
    elif random_number < the_guess:
        print("high!")
        return "high"


def choose_number(n):
    """Choose a number based on the level"""
    if n == 1:
        return randint(1, 10)
    elif n == 2:
        return randint(1, 100)
    elif n == 3:
        return randint(1, 1000)
    else:
        return False


def check_input(n):
    """Check if input is a valid number"""
    while not n.isdigit():
        print("It's not a number")
        n= input("Enter a valid number: ")
    return int(n)


def checking_computer_guess(level):
    """Check computer guess"""
    computer_guess_number = choose_number(level)
    return computer_guess_number


def print_round(round_number):
    """print round information"""
    if round_number == 1:
        print("Level 1: Guess a number between 1 and 10")
    elif round_number == 2:
        print("Level 2: Guess a number between 1 and 100")
    elif round_number == 3:
        print("Level 3: Guess a number between 1 and 1000")


def check_winner(player, computer):
    """Check who wins the game"""
    if player > computer:
        return f"You win the game, by {player} to {computer}"
    else:
        return f"Computer wins the game, by {computer} to {player}"

if __name__ == "__main__":
