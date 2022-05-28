"""
Module contains functions required for game but not the main part of the game.
"""

import os
from typing import Dict, List, Optional, Tuple, Union

from utils.wordlist import DIFFICULTIES


def get_guess_occurrences(
    guessed_letter: Optional[str] = None, mapped_letters: Optional[Dict] = None
) -> Union[List[int], str]:
    """
    Function returns occurences (indices) of guessed_letter in the word which
    already defined in mapped_letters.

    Args:
        guessed_letter: string of letter that is guessed
        mapped_letters: letter and indices of letters in a dictionary
    """

    if guessed_letter == None:
        return "Guessed letter is required."
    if mapped_letters == None:
        return "Dictionary of mapped letters is required."

    if mapped_letters == {}:
        return [-1]

    if guessed_letter in mapped_letters.keys():
        indices = mapped_letters[guessed_letter]
        return indices

    return [-1]


def get_guess_status(occurrences: Optional[List[int]] = None) -> Union[bool, str]:
    """
    Returns status of guessed letter by checking the occurrences of letter.

    Args:
        occurrences: indices of letters in a word
    """
    if occurrences is None:
        return "Occurences (positions) are required."

    if occurrences == [] or occurrences == [-1]:
        return False
    return True


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


def get_next_player_number(curr_player_num: int, count_of_players: int) -> int:
    """
    Function returns number of player who is gonna play next.

    Args:
        curr_player_num: number of current player
        count_of_players: quantity of players that are in the game
    """

    next_player_num = curr_player_num + 1
    if count_of_players < next_player_num:
        next_player_num = 1

    return next_player_num


def get_difficulty_level() -> str:
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
    return DIFFICULTIES.get(difficulty_id, None)


def get_guidelines(version: str = "short"):
    if version not in ["short", "long"]:
        return ""

    path_to = f".\\guidelines\\{version}.txt"
    with open(path_to) as guide:
        return guide.read()


if __name__ == "__main__":
    print("Module contains general helper functions for hangman.")
