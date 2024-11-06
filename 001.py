import random

# Hangman stages for visual feedback
stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''
]

# Word bank for the game
word_list = ["aardvark", "baboon", "camel"]

# Choose a random word and initialize variables
chosen_word = random.choice(word_list)
display = "_" * len(chosen_word)
lives = len(stages) - 1
guessed_letters = []

print("Welcome to Hangman! Try to guess the word before you run out of lives.")
print("Here's your starting word:", ' '.join(display))

# Main game loop
while lives > 0:
    guess = input("\nGuess a letter: ").lower()

    # Check for repeated guesses
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a new letter.")
        continue
    guessed_letters.append(guess)

    # Update display and lives based on guess
    new_display = ""
    for letter in chosen_word:
        if letter == guess or letter in guessed_letters:
            new_display += letter
        else:
            new_display += "_"

    # Check if guess was incorrect
    if guess not in chosen_word:
        lives -= 1
        print(f"\nIncorrect! You have {lives} lives remaining.")

    # Print the current hangman stage and word progress
    print(stages[len(stages) - lives - 1])
    print("Word: ", ' '.join(new_display))

    # Update the display for next iteration
    display = new_display

    # Check for win condition
    if "_" not in new_display:
        print("\n🎉 Congratulations, you win! 🎉")
        break

# If the loop ends without a win, the player has lost
if "_" in display:
    print("\n😢 You ran out of lives. The word was:", chosen_word)
    print("Better luck next time!")
