import random
import os  # For file operations

def load_high_score():
    """Loads the high score from a file."""
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read())
            return high_score
    except FileNotFoundError:
        return float('inf')  # No high score yet, so return infinity (anything will beat it)
    except ValueError: #if file is empty or contains non-int
        return float('inf')

def save_high_score(high_score):
    """Saves the high score to a file."""
    with open("high_score.txt", "w") as f:
        f.write(str(high_score))

def guess_game():
    # ... (rest of your guess_game function code)

    high_score = load_high_score()
    print(f"Current High Score: {high_score}") #display high score

    num_guesses = 5
    guesses_taken = 0 #keep track of how many guesses the player used.

    while num_guesses > 0:
        guesses_taken += 1 #increment guesses at the start of the loop
        # ... (your existing input and checking logic)

    if num_guesses == 0:
        print(f"You've run out of guesses! The Secrete number is {secret_number}")
    else: #player won!
        print(f"You won in {guesses_taken} guesses!")
        if guesses_taken < high_score:
            print("Congratulations! You set a new high score!")
            high_score = guesses_taken
            save_high_score(high_score)
            print(f"New High Score: {high_score}")


while True:
    guess_game()
    # ... (rest of your play again logic)