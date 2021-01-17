import random
#easy is 10 attempt
#hard = 5 attempts

def guess_number(tries,number):
    if tries == 0:
        print("No more tries left, gamne over!")
        play_again()
        return

    print(f"You have {tries} left.")

    guess = int(input("Guess a number"))
    if guess == number:
        print(f"The number {guess} is correct.\n")
        play_again()
    elif guess > number:
        print(f"The number {guess} is too high, try again")
        tries -= 1
        guess_number(tries,number)
    elif guess < number:
        print(f"The number {guess} is too low, try again")
        tries -= 1
        guess_number(tries,number)

def thank_you():
    print("Thank you for playing!")


def play_again():
    play_again_input = input("Do you want to play again? (Yes or No)\n")
    play_again_input = play_again_input.lower() 
    if play_again_input == "yes":
        guess_game()
    elif play_again_input != "yes" and play_again_input != "no":
        print("I didn't understand that, let's try again")
        play_again()
    else:
        thank_you()

def guess_game():
    NUMBER = random.randrange(1,100)
    level = input("do you want to play easy or hard?\n")
    level = level.lower()
    print (f"you are playing on level {level}")
    if level == "easy":
        tries = 10
    elif level == "hard":
        tries = 5
    guess_number(tries,NUMBER)

guess_game()
