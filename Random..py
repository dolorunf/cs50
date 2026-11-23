from random import choice
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
while True:
    computer = choice(choices)
    user = input("Make a choice, rock, paper or scissors: ").lower()
    if user == "rock":
        print(f"Computer picked {computer}")
        if computer == "paper":
            print("You lost")
            computer_score += 1
        elif computer == "scissors":
            print("You win")
            user_score += 1
        else:
            print("It's a draw")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
    elif user == "paper":
        print(f"Computer picked {computer}")
        if computer == "rock":
            print("You win")
            user_score += 1
        elif computer == "scissors":
            print("You lost")
            computer_score += 1
        else:
            print("It's a draw")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")  
    elif user == "scissors":
        print(f"Computer picked {computer}")
        if computer == "paper":
            print("You win")
            user_score += 1
        elif computer == "rock":
            print("You lost")
            computer_score += 1
        else:
            print("It's a draw")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
    else:
        print("Input a valid choice")
        continue

    restart = input("Play again? Yes or no: ").lower()
    if restart == "yes":
        print("Okay!")
        continue
    elif restart == "no":
        print("Have a nice day!")
        break
    else:
        print("Invalid option")
        continue