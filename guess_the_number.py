# Firstly, import random to use random modules
import random



# Next we want the user to choose the highest possible number the computer can choose from
top_of_range = int(input("Choose the highest possible number the computer can choose from?: "))

# We want the computer to pick a number randomly from the user's top of range
computer_choice = random.randint(0, top_of_range)

guess_count = 0

# We want the user to have a limited number of guesses
while guess_count < 5:
    guess_count += 1
    # We also want the user to guess the number the computer has chosen
    user_guess = int(input("Guess the number the computer picked: "))
    
    # The user should know whether he was right (in how many guesses) or wrong and how many guesses he has left
    # If he was wrong, he should know whether his guess was higher or lower than the number the computer picked
    if user_guess > computer_choice:
        print("Wrong! Your guess is higher than the number.You have", 5 - guess_count, "guesses left.")
    elif user_guess < computer_choice:
        print("Wrong! Your guess is lower than the number. You have", 5 - guess_count, "guesses left")
    else:
        print("You guessed right! You got it in", guess_count, "guesses.")
        break

    # We also want to tell the user "Game Over" if he ran out of guesses
    if guess_count == 5:
        print("Out of Guesses. Game Over! The number is " + str(computer_choice) + ".")
print("Thank you for playing. Bye!")
