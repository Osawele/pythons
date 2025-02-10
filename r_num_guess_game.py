import random

def guess_game():
    print(f"Secret Number guessing game! Designed by Isioma Osawele on 7th Feb, 2025.\nThis is a test game anyway for learning python :-)")

    #I'm defining levels to this game!
    print("\n\n\t\t\tLevels")
    print(f"[01]Easy    [02]Medium  [03]Hard    [04]Impossible")
    level = input("Please pick a level:    ")
    valid = ['01', '02', '03', '04']

    while level not in valid:
        level = input("Please pick a valid difficulty level:    ")

    if level == '01':
        secret_number_max = 5
        secret_number = random.randint(1, secret_number_max)
        print(f"\nYou picked level 'Easy', Your secret number is between 1 and {secret_number_max}")
    elif level == '02':
        secret_number_max = 20
        secret_number = random.randint(1, secret_number_max)
        print(f"\nYou picked level 'Medium', Your secret number is between 1 and {secret_number_max}")
    elif level == '03':
        secret_number_max = 50
        secret_number = random.randint(1, secret_number_max)
        print(f"\nYou picked level 'Hard', Your secret number is between 1 and {secret_number_max}")
    else:
        secret_number_max = 100
        secret_number = random.randint(1, secret_number_max)
        print(f"\nYou picked level 'Impossible', Your secret number is between 1 and {secret_number_max}")

    num_guesses = 5
    print("You've got 5 tries to guess your Secret number!")

    while num_guesses > 0:
        player_input = int(input(f'Guess the Number:    '))
        if player_input == secret_number:
            print(f"Bravo! You won the Game.")
            break
        elif player_input < secret_number:
            print("You're not quite there. Try a higher number.")
        else:
            print(f"Not there yet. Try a lower number")
        num_guesses -= 1
        print(f"You've got {num_guesses} tries left!")


    if num_guesses == 0:
        print(f"You've run out of guesses! The Secrete number is {secret_number}")


guess_game()

#this part is not yet correct
p_again = input(f"Would you like to play again? y/n:    ")
yes_or_no = ['y', 'n', 'yes', 'no']
while p_again not in yes_or_no:
    input(f"You've got to pick a valid option. Would you like to play again? y/n:   ")
    if p_again == 'y' or p_again == 'yes':
        guess_game()

