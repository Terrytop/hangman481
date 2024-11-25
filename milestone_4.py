#Import the random module for selecting a word from the word_list
import random
#Create a class called Hangman
class Hangman:
    #Define the __init__ method
    def __init__(self, word_list, num_lives=5):
        #Initialise attributes
        self.word = random.choice(word_list)  #Randomly select a word from the word_list
        self.word_guessed = ['_'] * len(self.word)  #Create a list of underscores for the word
        self.num_letters = len(set(self.word))  #Count the unique letters in the word
        self.num_lives = num_lives  #Set the initial number of lives
        self.word_list = word_list  #Store the word list
        self.list_of_guesses = []  #Initialize the list of guesses as an empty list

word_list = ['Kiwi', 'Apple', 'Pineapple', 'Tomato', 'Grapes']
game = Hangman(word_list)
print(f"Word to guess: {''.join(game.word_guessed)}")
print(f"Number of unique letters: {game.num_letters}")
print(f"Lives: {game.num_lives}")