import random

def guess_game():
    print("\n\nSecret Number guessing game! Designed by Isioma Osawele on 7th Feb, 2025.\nThis is a test game anyway for learning python :-)")

    print("\n\n\t\t\tLevels")
    print("[01]Easy    [02]Medium  [03]Hard    [04]Impossible")

    while True:  # Loop until a valid level is chosen
        level = input("Please pick a level: ")
        if level in ['01', '02', '03', '04']:
            break  # Exit loop if level is valid
        print("Please pick a valid difficulty level.")

    if level == '01':
        secret_number_max = 5
    elif level == '02':
        secret_number_max = 20
    elif level == '03':
        secret_number_max = 50
    else:
        secret_number_max = 100

    secret_number = random.randint(1, secret_number_max)
    print(f"You picked level {level}, Your secret number is between 1 and {secret_number_max}")

    num_guesses = 5
    print("You've got 5 tries to guess your Secret number!")

    while num_guesses > 0:
        try:  # Handle potential ValueError if user enters non-integer input
            player_input = int(input("Guess the Number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Go back to the beginning of the loop

        if player_input == secret_number:
            print("Bravo! You won the Game")
            break
        elif player_input < secret_number:
            print("You're not quite there. Try a higher number.")
        else:
            print("Not there yet. Try a lower number")
        num_guesses -= 1
        print(f"You've got {num_guesses} tries left!")

    if num_guesses == 0:
        print(f"You've run out of guesses! The Secrete number is {secret_number}")

while True:  # Outer loop for playing multiple games
    guess_game()
    while True:  # Inner loop for getting valid play-again input
        p_again = input("Would you like to play again? y/n: ")
        if p_again in ['y', 'yes', 'n', 'no']:
            break  # Exit inner loop if input is valid
        print("You've got to pick a valid option. Would you like to play again? y/n: ")

    if p_again in ['n', 'no']:
        break  # Exit outer loop if user doesn't want to play again

print(f"Your Score: {5 - num_guesses}")