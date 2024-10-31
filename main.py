import random

# TODO: Generate a random number between 1 and 10 using randint
# Call it random_num
random_num = random.randint(1,10)

while True:
    # TODO: Ask the user for a number using the int and the inputs functions.
    # store it in a variable called guess.
    guess =  int(input("What's your guess?"))
    if guess > random_num:
        print("Too high, try again.")

    elif guess < random_num:
        print("Too low, try again.")

    else:
        print("Congratulations, you've guessed the number.")
        break