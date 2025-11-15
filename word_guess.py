import random

def play_game():
    # List of words for the game
    words = ["apple", "banana", "cherry", "orange", "grapes"]

    # Choose a random word
    secret_word = random.choice(words)

    # Create blank spaces for the word
    display = ["_"] * len(secret_word)

    # Number of chances
    chances = 6

    print("\n🎉 Welcome to the Word Guessing Game!")
    print("Guess the word, one letter at a time.")
    print("Word:", " ".join(display))

    while chances > 0:
        guess = input("\nEnter a letter: ").lower()

        # If user enters more than one letter
        if len(guess) != 1:
            print("Please enter only ONE letter!")
            continue

        # Check if guess is in the word
        if guess in secret_word:
            print(" Correct!")

            # Reveal the guessed letter in the display
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess

        else:
            print(" Wrong guess!")
            chances -= 1
            print("Chances left:", chances)

        # Show progress
        print("Word:", " ".join(display))

        # If user wins
        if "_" not in display:
            print("\n Congratulations! You guessed the word:", secret_word)
            return  # End this round

    # If user loses
    print("\n Game Over! The correct word was:", secret_word)

# Main loop to play again
while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\n Thanks for playing! See you next time!")
        break

