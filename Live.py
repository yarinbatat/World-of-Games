def welcome(name):
    name = input("Please enter your name: ")
    print("Hello", name, "and welcome to the World of Games (WoG). "
                         "\nHere you can find many cool games to play.")


def load_game():
    game = int(input("Please choose a game to play:"
                     "\n 1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess id back."
                     "\n 2.Guess Game - guess a number and see if you chose like the computer"
                     "\n 3.Currency Roulette - try and guess the value of a random amount of USD and ILS"
                     "\n -"))
    if game == 1:
        print("You chose to play - Memory Game")
    elif game == 2:
        print("You chose to play - Guess Game")
    elif game == 3:
        print("You chose to play - Currency Roulette")
    else:
        print("You have selected a not possible option, please select again. ")

    level = int(input("Please choose game difficulty from 1 to 5: "))
    if level == 1:
        print("You have selected to play at level 1")
    elif level == 2:
        print("You have selected to play at level 2")
    elif level == 3:
        print("You have selected to play at level 3")
    elif level == 4:
        print("You have selected to play at level 4")
    elif level == 5:
        print("You have selected to play at level 5")
    else:
        print("You have selected a not possible option, please select again. ")

    return game, level

