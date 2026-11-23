import random
import json

with open("questions.json", "r") as file:
    questions = json.load(file)

RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
RESET = "\x1b[0m"
BLACK = "\x1b[30m"


def show_menu():
    print(f"{YELLOW}===================================")
    print("      WELCOME TO THE QUIZ GAME!    ")
    print("===================================")
    print("Let's see how much you can get right!", RESET)
    print()


def play_quiz():
    user_score = 0
    random.shuffle(questions)  # to change the order of my question
    for question in questions:
        # to get the values under the key ["question"]
        print(BLACK + question["question"] + RESET)
        letters = "ABCD"
        number = 0
        # to change the order of my option in each question
        random.shuffle(question["options"])
        for option in question["options"]:
            print(BLUE, letters[number] + ".", option, RESET)
            number += 1
        while True:
            try:
                user = input(f"{BLUE}Choose an option: {RESET}").upper().strip()
                position = letters.index(user)
                break
            except ValueError:
                print(f"{YELLOW}/!\\ Give a valid option{RESET}")
        
        if question["options"][position] == question["answer"]:
            print(f"{GREEN}Correct!{RESET}")
            print()
            user_score += 1
        else:
            print(f"{RED}Wrong answer!{RESET}")
            print(f"{RED}The correct answer is {question['answer']}{RESET}")
            print()

    print("Quiz Finished!")
    if user_score == 0 or user_score <= 10:
        print(f"{RED}You got {user_score} questions right out of {len(questions)} questions!{RESET}")
    elif user_score <= 15:
        print(f"{YELLOW}You got {user_score} questions right out of {len(questions)} questions!{RESET}")
    
    else:
        print(f"{GREEN}You got {user_score} questions right out of {len(questions)} questions!{RESET}")


show_menu()
while True:
    play_quiz()
    play_again = True
    while True:
        restart = input("Play again? Yes or no: ").lower().strip()
        if restart == "yes":
            print("Okay!")
            break
        elif restart == "no":
            print("Have a nice day!")
            play_again = False
            break
        else:
            print("You input an invalid Option")
            continue
    if play_again == False:
        break
    
    