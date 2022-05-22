from utils.game import start_game_mp, start_game_sp
from utils.helper_funcs import get_player_names
from utils.player import Player


def main() -> None:
    count = int(input("How many players will be in the game?: "))
    player_names = get_player_names(count)

    if count > 1:
        # create instances for each player
        for player in player_names:
            Player(player)

        start_game_mp(Player.all())

        # start_game_mp(player_names)
    else:
        player = Player(player_names[0])
        start_game_sp(player)

    return None


if __name__ == "__main__":
    main()
