from handlers.game import handle_game
from handlers.exit import handle_exit
from handlers.wrong_input import handle_wrong_input


def rock_paper_scissors():
    start = input("y to start, n to exit. \n")

    if start == "y":
        handle_game()
    elif start == "n":
        handle_exit()
    else:
        handle_wrong_input()


if __name__ == "__main__":
    rock_paper_scissors()
