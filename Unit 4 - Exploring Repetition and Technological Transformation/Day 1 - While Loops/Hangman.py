import random


def choose_word():
    words = [
        "sussy baka", "skibidi toilet", "fortnite", "only in ohio", "w rizz", "ice spice", "max prestige",
        "bussin", "level 10 gyatt", "kai cenat", "L", "rizzing", "griddy", "grimace shake", "ohio",
        "sigma", "chad", "looks maxing at 3 a.m.", "don’t sigma chat at 3 a.m.", "without w rizz",
        "not clickbait real challenge for 24 hours with skibidi toilet",
        "Elmo and bussin gyats everywhere and joe bartolozzi rizzing my mom", "ishowmeat", "ishowspeed", "pull up to the function"
    ]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
 
def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
 
    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))
 
    while attempts > 0:
        guess = input("Guess a letter: ").lower()
 
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
 
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
 
        guessed_letters.append(guess)
 
        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
 
        display = display_word(word_to_guess, guessed_letters)
        print(display)
 
        if "_" not in display:
            print("Congratulations! You guessed the word.")
            break
 
    if "_" in display:
        print(f"Sorry, you ran out of attempts. The word was '{word_to_guess}'.")
 
if __name__ == "__main__":
    hangman()