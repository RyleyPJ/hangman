import random 

def choose_word():
    words = ["Python", "computer", "programming", "power"]
    return random.choice(words)

def hangman():
    chosen_word = choose_word().lower()
    guessed_letters = set
    
    print("Welcome to hangman, please guess a letter!")
    
    while True: 
        guess = get_letter(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in choose_word:
            print("Correct")
        else:
            print("Incorrect")
            
            if all(letter in guessed_letters for letter in chosen_word):
                print("Congratulationa, you have guessed the word!", chosen_word)
                break

def get_letter(guessed_letters):
    while True:
        letter = input("Enter a letter: ").lower()
        
        if letter.isalpha() and len(letter) == 1:
            if letter in guessed_letters:
                print("You have already guessed that, please try a different letter!")
            else:
                return letter 
            else:
                print("Invalid input. Please try a different letter!")
            

#Code to run the game

hangman()