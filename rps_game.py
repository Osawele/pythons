import random



def check_game(user_name):
    options = ["rock", "paper", "scissors"]
    computer_name = random.choice(options)
    user_name = input("Enter a choice (rock, paper, scissors):")
    
    
    print (f"You chose {user_name}, the computer chose {computer_name}")
    
    if user_name == computer_name:
        return (f"It's a tie! Try again.")
    
    elif user_name == "scissors":
        if computer_name == "paper":
            return (f"Scissors cut paper! You win!")

        else: return (f"Rock break scissors. You lose.")


    elif user_name == "paper":
        if computer_name == "rock":
            return (f"Paper covers rock! You win!")
        
        else: return (f"Scissors cuts paper. You lose.")


    elif user_name == "rock":
        if computer_name == "scissors":
            return (f"Rock breaks Scissors! You win!")
        
        else: return (f"Paper covers rock. You lose.")
        
    else:
        return (f"Something has deperately gone wrong.")

print (check_game("rock"))