import random 

def choose_word()
    words = ["Python", "computer", "programming", "power"]
    return words[random.randint(0, words.length - 1)]

def choose_word()
    print("Welcome to the hangman, please enjoy and choose any letters")
    def get_letter(letter):
        if letter in guessed_letters:
            print("You have already guessed that letter, please try a different letter"):
            return False
    
def chosen_word(word):
    print("Well done, you guessed the word in " + str(len(guessed_letters)) +)
    print(word)
    