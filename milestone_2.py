import random
word_list = ['Kiwi', 'Apple', 'Pineapple', 'Tomato', 'Grapes']
print(word_list)
word = random.choice(word_list)
print(word)
#Guessing
guess = input("Please enter a single letter: ")
print(f"You entered: {guess}")
#Create an if statement to validate the input
if len(guess) == 1 and guess.isalpha():
    # Print "Good guess!" if the input is valid
    print("Good guess!")
else:
    #Print an error message if the input is invalid
    print("Oops! That is not a valid input.")
