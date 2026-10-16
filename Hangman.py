import random 

def play_hangman():
    words = ["apple", "flower", "braids", "bubble", "python"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("=" * 45)
    print("        🎮 WELCOME TO HANGMAN")
    print("=" * 45)
    print("Guess the word one letter at a time!")
    print("You have 6 incorrect guesses allowed.\n")

    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word:", display_word)
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongrats!! You have guessed the correct word")
            break

        guess = input("\nEnter the letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.\n")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅Correct Guess!\n")

        else:
            attempts -= 1
            print("❌ Wrong Guess!\n")

    else:
        print("😢 Game Over! The word was:", secret_word)

    print("=" * 40)
    print("         THANKS FOR PLAYING!")
    print("=" * 40)

if __name__ == "__main__":
    play_hangman()
    
