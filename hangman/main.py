from typing import List, Dict

from utils.multiplayer import (get_player_names, start_game_mp,  start_game_sp)
from utils.words import guess_word

def main() -> None:
    count = int(input("How many players will be in the game?: "))
    players = get_player_names(count)

    if count > 1:
        start_game_mp(players)
    else:
        player = players[0]
        start_game_sp(player)

    return None

if __name__ == "__main__":
    main()