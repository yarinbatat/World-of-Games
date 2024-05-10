import random
from time import sleep
from Score import *


def generate_sequence(difficulty):
    list = []
    for i in range(difficulty):
        number = random.randint(1, 101)
        list.append(number)
    print("remember the list", list)
    sleep(0.7)
    return list


def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
        number = int(input("Please enter a number: "))
        user_list.append(number)
    print(user_list)
    return user_list


def is_list_equal(list, user_list):
    return list == user_list


def play1(difficulty):
    list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    outcome = is_list_equal(list, user_list)
    if outcome:
        print("Congratulations, you won.")
        add_score(difficulty)
    else:
        print("Sorry, you lost.")
