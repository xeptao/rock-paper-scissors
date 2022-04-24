import random


def pick_for_computer():
    choices = ["r", "p", "s"]
    comp_choice = random.choice(choices)

    return comp_choice


def check_winner(user_choice, comp_choice):
    game_rules = {
        "r": {
            "beats": "s",
            "loses_to": "p"
        },
        "p": {
            "beats": "r",
            "loses_to": "s"
        },
        "s": {
            "beats": "p",
            "loses_to": "r"
        }
    }

    user_data = game_rules[user_choice]

    if user_data["beats"] == comp_choice:
        print(
            f"\033[1m\nyou won!\nyou picked: {user_choice},\nthe computer picked: {comp_choice}\n\033[0m")
    elif user_data["loses_to"] == comp_choice:
        print(
            f"\033[1m\nyou lost!\nyou picked: {user_choice},\nthe computer picked: {comp_choice}\n\033[0m")
    else:
        print("\033[1m\nits a draw!\n\033[0m")


def handle_game():
    while True:
        user_choice = input("\nr for rock, p for paper, s for scissors: \n")
        comp_choice = pick_for_computer()

        check_winner(user_choice, comp_choice)

        option_quit_or_play = input(
            "wanna play again? anything for yes, n for no \n")

        if option_quit_or_play == "n":
            exit()
