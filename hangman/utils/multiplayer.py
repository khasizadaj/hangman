from typing import Tuple, Dict

from utils.words import (guess_word, get_random_word, WORDLIST)
from utils.helper_funcs import (add_linebreak, get_pretty_leaderboard)


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

        user_will_add_custom_word = input("Do you wanna challange you friend by yourself? [Y(y)/N(n)] ")
        if user_will_add_custom_word.lower() == "y":
            custom_word = input("Enter custom word: ").lower()
        else:
            custom_word = None

        rand_word = custom_word or get_random_word(WORDLIST["easy"])

        status = guess_word(rand_word)
        if status:
            points[curr_player] += 1
            if points[curr_player] == winning_point:
                print(f"Winner is {curr_player}")
                exit()

        curr_player_num = get_next_player_number(
            curr_player_num, len(player_names))
        print(get_pretty_leaderboard(points))

    return None


def get_player_names(count: int) -> Tuple[str]:
    """
    Function ask for names of the players and returns a tuple of player names. 
    Amount of players is determined by provided `count` number.

    Args
        count: quantity of players that are in the game
    """

    players = []

    for p_num in range(1, count+1):
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


if __name__ == "__main__":
    print("Module contains functions for single and multiple player functionality.")
