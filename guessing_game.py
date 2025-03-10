# clears the screen
import os  # import module
import random  # import module


# create the play again function
def play_again():
    again = input("Would you like to play again? (y/n): ")
    if again == "y":
        game()
    else:
        print("Thank you for playing!")


# create main game function
def game():

    # create guess tracker
    number_of_guesses = 0
    correct = False  # while loops are great with booleans
    # clear screen
    os.system("clear")

    # without parameters error reads you need(a, b) inside of argument.
    number_to_guess = random.randint(1, 10)  # variable to hold the random number

    # Get user input
    print("Guess a number between 1 and 10")

    # Add while loop here because we dont want the previous question to repeat over and over
    while correct == False:

        # try/except block
        try:
            guess = int(input("Enter your Guess: "))
        except:
            print("Please try again by entering a number")
            return
        # create some logic to check the guess
        if guess < number_to_guess:
            print("Too low. Try again")
            number_of_guesses += 1
        elif guess > number_to_guess:
            print("Too high. Try again")
            number_of_guesses += 1
        elif guess == number_to_guess:
            number_to_guess += 1
            print(
                f"Correct! The number was {number_to_guess - 1}. And you guessed it in {number_of_guesses + 1} guess/es!"
            )
            # set correct to true to stop the loop
            correct = True

            play_again()


# call our game function
game()
