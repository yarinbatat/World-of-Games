import random
from Score import *


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user():
    while True:
        try:
            guess = int(input("Please make a guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")


def compare_results(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user()

    if guess == secret_number:
        return True
    else:
        return False


def play2(difficulty):
    outcome = compare_results(difficulty)
    if outcome:
        print("Congratulations, you won.")
        add_score(difficulty)
    else:
        print("Sorry, you lost.")
