"""
Module contains functions related to game logic. It implements the following:
- single player mode
- multi players mode 
"""

from getpass import getpass
from typing import Tuple

from utils.helper_funcs import (
    add_linebreak,
    get_next_player_number,
    get_pretty_leaderboard,
)
from utils.wordlist import WORDLIST
from utils.words import get_random_word, guess_word


def start_game_sp(player_name: str) -> None:
    """
    Function handles the game for single player.

    Args:
        player_name: name of the player
    """

    points = {player_name: 0}
    to_be_continued = True

    while to_be_continued:
        message = f"Let's find this word, {player_name}"
        print(message)
        add_linebreak()

        rand_word = get_random_word(WORDLIST["easy"])
        status = guess_word(rand_word)
        if status:
            points[player_name] += 1

        print(get_pretty_leaderboard(points))

        # asking if user wants to continue
        choice = input("Do you want to continue? (Y/N): ")
        to_be_continued = True if choice.lower() == "y" else False

    return None


def start_game_mp(player_names: Tuple[str]) -> None:
    """
    Function handles the game for multiple players.

    Args:
        player_names: names of the players
    """

    points = {player: 0 for player in player_names}
    winning_point = 3
    winner_is_decided = False
    curr_player_num = 1

    while winner_is_decided == False:
        curr_player = player_names[curr_player_num - 1]
        message = f"It's your turn, {curr_player}"
        print(message)
        add_linebreak()

        user_will_add_custom_word = input(
            "Do you wanna challange you friend by yourself? [Y(y)/N(n)] "
        )
        if user_will_add_custom_word.lower() == "y":
            custom_word = getpass(
                "Enter custom word (typed letters will be not shown, but registered): "
            ).lower()
        else:
            custom_word = None

        rand_word = custom_word or get_random_word(WORDLIST["easy"])

        status = guess_word(rand_word)
        if status:
            points[curr_player] += 1
            if points[curr_player] == winning_point:
                print(f"Winner is {curr_player}")
                exit()

        curr_player_num = get_next_player_number(curr_player_num, len(player_names))
        print(get_pretty_leaderboard(points))

    return None


if __name__ == "__main__":
    print("Module contains functions for single and multiple player functionality.")
