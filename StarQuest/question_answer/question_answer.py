import requests
from random import choice
from time import sleep
from sys import exit


def main_question_answer():
    print("\n" + "="*40)
    print("        QUESTIONS & ANSWERS GAME")
    print("="*40 + "\n")
    print("The game consists of 5 questions.")
    print("Easy: True or False questions.")
    print("Medium: Multiple-choice questions.")
    print("Hard: You type the answer yourself. Each correct letter you type will be revealed.")
    print()

    check_ready(input("Type 'Ready' to start: "))

    stars = 0
    animels = 0
    sport = 0
    cheinses = 3

    """questions about animels"""
    print("quesstions about animels")
    while animels != 2:
        sleep(1)
        animels_question = animels_question_api() #We get the data from the API
        user_answer = checking_answers_True_False(animels_question) #check the answer

        if user_answer == "correct":
            stars += 1
            print("That's correct!")   #if correct the player get stars if not, the comueter get it
        else:
            print("That's not correct!")

        animels += 1

    sleep(1)

    """questions about sport"""
    print("questions about sport")
    while sport != 2:

        sport_question = sport_question_api() #We get the data from the API
        correct_answer, options = checking_answers_multiple_choice(sport_question) #check the correct answer, and options

        for i in sorted(options):  # Print the options
            print("-" + i)

        user_answer = check_input(input("Your answer: ").lower().strip())

        if user_answer == correct_answer:
            stars += 1
            print("That's correct!")
        else:                                      #if the answer is not correct, The computer choice from options
            print("That's not correct!")           #until one of them choose the correct answer
            while True:
                sleep(1)
                computer_answer = choice(options)
                print("computer answer:", computer_answer)
                if computer_answer == correct_answer:
                    print("computer choose, is correct")
                    break
                print("computer choose, is incorrect")

                user_answer = check_input(input("Your answer: ").lower().strip())
                sleep(1)
                if user_answer == correct_answer:
                    stars += 1
                    print("That's correct!")
                    break
                print("That's not correct!")

        sport += 1

    sleep(1)

    """questions about history"""
    print("questions about history")

    history_question = history_question_api() #We get the data from the API
    correct_answer, options = checking_answers_multiple_choice(history_question) #check the correct answer, and options

    while cheinses != 0:
        result = ""
        user_answer = check_input(input("Your answer: ").lower().strip())

        for litter in correct_answer:
            if litter in user_answer:      #looping for the player input and print the letters
                print(litter, end="")      
                result += litter
            else:
                print("_", end="")
        print()
        if result != correct_answer:
            cheinses -= 1
            print(f"That's not correct!. You have {cheinses} chances left.")   #The player he have a few cheinses
        else:
            print("That's correct!")
            stars += 1
            break
        
        computer_answer = choice(options)
        print("computer answer:", computer_answer)     #computer he will choise from options
        if computer_answer == correct_answer:
            print("computer choose, is correct")  
            break                
        print("computer choose, is incorrect")

        if cheinses == 0:
            print("The correct answer is:", correct_answer)  #print if the user not finde the correct answer 


    print("stars you get:", stars) #show how meny stars he get
    return stars


def animels_question_api():
    """Fetch an animal question from the API."""
    url = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=boolean"
    respone = requests.get(url)
    if respone.status_code != 200:
        print("Error fetching data")
        return
    data = respone.json()

    return choice(data["results"])


def checking_answers_True_False(data_question):
    """Check the True or False answers."""
    question = data_question["question"]
    answer = data_question["correct_answer"]

    print(question)
    while True:
        user_answer = input("Enter your answer (True/False): ").lower().strip()
        if user_answer == "true":
            break
        elif user_answer == "false":
            break
    
    if answer.lower() == user_answer:
        return "correct"
    return "incorrect"


def sport_question_api():
    """Fetch a sport question from the API."""
    url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=multiple"
    respone = requests.get(url)
    if respone.status_code != 200:
        print("Error fetching data")
        return
    data = respone.json()
    
    return choice(data["results"])


def checking_answers_multiple_choice(data_question):
    """Check the multiple choice answers."""
    question = data_question["question"]
    correct_answer = data_question["correct_answer"].lower()
    options = data_question["incorrect_answers"]
    options.append(correct_answer)

    print(question)
    
    return correct_answer, options


def history_question_api():
    """Fetch a history question from the API."""
    url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=hard"  
    respone = requests.get(url)
    if respone.status_code != 200:
        print("Error fetching data")
        return
    data = respone.json()

    return choice(data["results"])


def check_input(n):
    """Check if the input contains only letters, spaces, and digits."""
    while True:
        for word in n:
            if word.isalpha() or word == " " or word.isdigit():
                return n
        n = input("You only can type litter and speace, your answer: ")


def check_ready(n):
    """Check if the user is ready to start the game."""
    n = n.lower().strip()
    while n != "ready":
        print("Please enter 'ready' or 'exit'")
        if (n := input().lower().strip()) == "exit":
            exit(1)
    return n

if __name__ == "__main__":
