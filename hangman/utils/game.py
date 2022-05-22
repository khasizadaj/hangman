"""
Module contains functions related to game logic. It implements the following:
- single player mode
- multi players mode 
"""

from getpass import getpass
from typing import List

from utils.helper_funcs import (add_linebreak, get_next_player_number,
                                get_pretty_leaderboard)
from utils.player import Player
from utils.wordlist import WORDLIST
from utils.words import get_random_word, guess_word


def start_game_sp(player: Player) -> None:
    """
    Function handles the game for single player.

    Args:
        player_name: name of the player
    """

    to_be_continued = True

    while to_be_continued:
        message = f"Let's find this word, {player.name}"
        print(message)
        add_linebreak()

        rand_word = get_random_word(WORDLIST["easy"])
        status = guess_word(rand_word)
        if status:
            player.add_point()

        points = Player.points()
        print(get_pretty_leaderboard(points))

        # asking if user wants to continue
        choice = input("Do you want to continue? (Y/N): ")

        to_be_continued = False
        if choice.lower() == "y":
            to_be_continued = True

    return None


def start_game_mp(players: List[Player]) -> None:
    """
    Function handles the game for multiple players.

    Args:
        player_names: names of the players
    """

    winning_point = 3
    curr_player_num = 1

    while True:
        curr_player = players[curr_player_num - 1]
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
            curr_player.add_point()
            if curr_player.point == winning_point:
                print(f"Winner is {curr_player}")
                exit()

        curr_player_num = get_next_player_number(curr_player_num, len(players))

        print(get_pretty_leaderboard(Player.points()))


if __name__ == "__main__":
    print("Module contains functions for single and multiple player functionality.")
