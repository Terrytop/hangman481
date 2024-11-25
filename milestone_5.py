import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)  #Randomly select a word from the word_list
        self.word_guessed = ['_'] * len(self.word)  #Create a list of underscores for the word
        self.num_letters = len(set(self.word))  #Count the unique letters in the word
        self.num_lives = num_lives  #Set the initial number of lives
        self.word_list = word_list  #Store the word list
        self.list_of_guesses = []  #Initialise the list of guesses as an empty list

    def check_guess(self, guess):
        #Convert the guess into lowercase
        guess = guess.lower()
        #Check if the guess is in the word
        if guess in self.word:
            print("-" * 30)
            print(f"Good guess! {guess} is in the word.")
            #Update the word_guessed list with the guessed letter
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1  #Reduce the count of remaining unique letters
        else:
            print("-" * 30)
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1  #Decrease the number of lives
            print(f"Lives: {self.num_lives}")
        print(f"Current word: {''.join(self.word_guessed)}")

    def ask_for_input(self):
        while True:
            #Ask for input
            print("-" * 30)
            guess = input("Guess a letter: ")
            #Check if the input is valid
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("-" * 30)
                    print("You already tried that letter.")
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)  #Call to validate the guess
                    break
            else:
                print("-" * 30)
                print("Invalid letter. Please, enter a single alphabetical character.")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(f"Word to guess: {''.join(game.word_guessed)}")
    print(f"Number of unique letters: {game.num_letters}")
    print(f"Lives: {game.num_lives}")
    
    while True:
        #Check number of lives
        if game.num_lives == 0:
            print("-" * 30)
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()  #Ask for input
        else:
            print("-" * 30)
            print("Congrats. You won the game!")
            break

word_list = ['Kiwi', 'Apple', 'Pineapple', 'Tomato', 'Grapes']
play_game(word_list)