import random

choices = ["rock", "paper", "scissors"]

def game():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice not in choices:
        print("Sahi se likh sirf rock,paper,scissor likh saktai ho tum")
        return
    
    comp_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")
    
    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
        (user_choice == "scissors" and comp_choice == "paper") or \
        (user_choice == "paper" and comp_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

game()
