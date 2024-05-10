import random
import requests
from Score import *


def get_money_interval(difficulty):
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    value = response.json()
    exchange_rate = value["rates"]["ILS"]
    money = random.randint(1, 100)
    interval = (money - (5 - difficulty), money + (5 - difficulty))
    return money, interval, exchange_rate


def get_guess_from_user():
    while True:
        try:
            guess = float(input("Enter your guess for the value in ILS: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")


def play3(difficulty):
    money, interval, exchange_rate = get_money_interval(difficulty)
    print("You have to guess the value of {} USD in ILS.".format(money))
    print("Interval for guessing: {} ILS to {} ILS".format(interval[0], interval[1]))
    guess = get_guess_from_user()
    if interval[0] <= (guess / exchange_rate) <= interval[1]:
        print("Congratulations! Your guess is correct.")
        add_score(difficulty)
        return True
    else:
        print("Sorry, your guess is incorrect. The correct value is {} ILS.".format(money / exchange_rate))
        return False




