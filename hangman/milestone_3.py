#Define a function called check_guess
def check_guess(guess):
    #Convert the guess into lower case
    guess = guess.lower()
    #Sample word to check against
    word = "apple"
    #Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

#Define a function called ask_for_input
def ask_for_input():
    while True:
        #Prompt the user for input
        guess = input("Guess a letter: ")
        #Check if the input is valid
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    #Call the check_guess function to check the validity of the guess
    check_guess(guess)

#Call the ask_for_input function to test the code
ask_for_input()