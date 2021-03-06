"""
Module contains functions required for game but not the main part of the game.
"""


from os import name, system
from typing import Dict, List, Optional, Tuple

from utils.wordlist import DIFFICULTIES


def clear_console() -> None:
    """Function clears console and works for all main operating systems."""

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux
    else:
        _ = system("clear")


def get_emotion(status: Optional[bool] = None) -> str:
    """
    Function returns an emotion based on the status of guessed letter.

    Args:
        status: boolean value indicating correctness of guessed letter
    """

    if status is None:
        return "Status is required."

    if status:
        return "Hooray! We did it."
    return "We'll be successful next time. Cheer up!"


def get_letter_message(
    status: Optional[bool] = None, guessed_letter: Optional[str] = None
) -> str:
    """
    Function returns a string containing message about the guessed letter based
    on the status of guess.

    Args:
        status: boolean value indicating correctness of guessed letter
        guessed_letter: string of letter that is guessed
    """

    if status is None:
        return "Status is required."
    if guessed_letter is None:
        return "Letter is required."

    if status:
        return f'Letter "{guessed_letter}" is in the word.'
    return f'Letter "{guessed_letter}" is not in the word.'


def add_linebreak(quantity: int = 1) -> None:
    """
    Function adds line break(s).

    Args:
        quantity: quantity of line breaks required
    """

    if quantity == 1:
        print("")
        return None

    for _ in range(quantity):
        print("")

    return None


def get_pretty_leaderboard(points: Dict[str, int]) -> str:
    """
    Function return prettified string of leaderboard.

    Args:
        points: dictionary of player names and points
    """

    pretty_leaderboard = ""

    for player, point in points.items():
        plural_suffix = "s" if point > 1 else ""
        pretty_leaderboard += f"{player}: {point} point{plural_suffix}\n"

    return pretty_leaderboard


def get_player_names(count: int) -> Tuple[str]:
    """
    Function ask for names of the players and returns a tuple of player names.
    Amount of players is determined by provided `count` number.

    Args
        count: quantity of players that are in the game
    """

    players = []

    for p_num in range(1, count + 1):
        player = input(f"What's your name, player {p_num}?: ")
        players.append(player)

    return tuple(players)


def get_difficulty_level() -> str:
    """
    Function propmpts user for difficulty id/number for words and returns
    difficulty level that corresponds to it.
    """

    print(
        "\n"
        + "0. All"
        + "\n1. Easy (3-5 letter words)"
        + "\n2. Medium (6-7 letter words)"
        + "\n3. Hard (8 and more letter words)\n"
    )
    difficulty_id = int(input("Write your choice with number (e.g. 1): "))
    difficulty_level = get_difficulty_value(difficulty_id)
    if difficulty_level is None:
        return "all"

    return difficulty_level


def get_difficulty_value(difficulty_id: int):
    """
    Returns string value that corresponds to `difficulty_id` that is provided
    by player.
    """

    return DIFFICULTIES.get(difficulty_id, None)


def get_winning_point() -> int:
    """Return value that is provided by the user for winning point."""

    message = "\n Type winning point here: "
    while True:
        winning_point = input(message)
        if winning_point.isnumeric():
            winning_point = int(winning_point)
            break

        if winning_point == "":
            winning_point = None
            break

        message = "\n Please, provide a number:"

    return winning_point


def get_guidelines(version: str = "short"):
    """Returns short or long guidelines for the game."""

    if version not in ["short", "long"]:
        return ""

    path_to = f".\\guidelines\\{version}.txt"
    # TODO add encoding for the file opening
    with open(path_to) as guide:
        return guide.read()


if __name__ == "__main__":
    print("Module contains general helper functions for hangman.")
