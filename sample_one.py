import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        return (f"The Computer chose {computer_choice}, you chose {player_choice} \n It was a tie!")
    else:
        return (f"The Computer chose {computer_choice}, you chose {player_choice} \n Something!")

print(get_choices())