from utils.game import Game
from utils.helper_funcs import get_difficulty_level, get_player_names
from utils.player import Player
from utils.wordlist import get_wordlist


def main() -> None:
    difficulty_level = get_difficulty_level()
    words = get_wordlist(difficulty_level)

    number_of_players = int(input("How many players will be in the game?: "))
    player_names = get_player_names(number_of_players)

    # create instances for each player
    for player in player_names:
        Player(player)

    game = Game(number_of_players=number_of_players)
    game.start(Player.all(), words)


if __name__ == "__main__":
    main()
