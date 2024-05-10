
def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5

    try:
        with open("scores.txt", "r") as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0

    new_score = current_score + POINTS_OF_WINNING
    with open("scores.txt", "w") as file:
        file.write(str(new_score))

add_score(4)


