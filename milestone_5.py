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
        guess = guess.lower() #Convert the guess into lowercase
        if guess in self.word: #Check if the guess is in the word
            print("-" * 30) #Print -'s to enhance readability
            print(f"Good guess! {guess} is in the word.") #Print encouragement
            for idx, letter in enumerate(self.word): #Update the word_guessed list with the guessed letter - Enumerate means that the letters are revealed in the correct positions. Using "str.replace" sometimes breaks.
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1  #Reduce the count of remaining unique letters
        else:
            print("-" * 30) #Print -'s to enhance readability
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1  #Decrease the number of lives
            print(f"Lives: {self.num_lives}") #Print lives remaining so that the user doesn't need to keep track themselves
        print(f"Current word: {''.join(self.word_guessed)}") #Print visual

    def ask_for_input(self):
        while True:
            print("-" * 30) #Print -'s to enhance readability
            guess = input("Guess a letter: ") #Ask for a letter input
            if len(guess) == 1 and guess.isalpha(): #Check if the input is valid
                if guess in self.list_of_guesses: #Check if already guessed
                    print("-" * 30) #Print -'s to enhance readability
                    print("You already tried that letter.") #Sometimes I forget what letters I've already guessed
                else:
                    self.list_of_guesses.append(guess) #Add to list of guessed
                    self.check_guess(guess) #Call to validate the guess
                    break
            else:
                print("-" * 30) #Print -'s to enhance readability
                print("Invalid letter. Please, enter a single alphabetical character.") #For any non-letters

def play_game(word_list): #Game functions
    num_lives = 5 
    game = Hangman(word_list, num_lives) 
    print(f"Word to guess: {''.join(game.word_guessed)}") #Print visual for user to guess against
    print(f"Number of unique letters: {game.num_letters}") #Print how many letters
    print(f"Lives: {game.num_lives}") #Print for clear limit
    
    while True:
        if game.num_lives == 0: #Check number of lives
            print("-" * 30) #Print -'s to enhance readability
            print("You lost!") #Print Game Over
            break #Game Over
        elif game.num_letters > 0:
            game.ask_for_input() #Ask for input
        else:
            print("-" * 30) #Print -'s to enhance readability
            print("Congrats. You won the game!") #Print Game Won
            break #Game Over

word_list = ['kiwi', 'apple', 'pineapple', 'tomato', 'grapes'] #Tamatoes are a lot easier to cook with than these others
play_game(word_list) #Initiate Game
