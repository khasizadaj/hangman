from utils.game import Game
from utils.helper_funcs import get_difficulty_level, get_guidelines, get_player_names
from utils.player import Player
from utils.wordlist import get_wordlist


def main() -> None:
    # print guidelines
    guidelines = get_guidelines()
    print(guidelines)

    print("First, I need to know how many players will be in the game.")
    number_of_players = int(input("Type number of players here: "))
    if 3 >= number_of_players > 1:
        print("\nGreat, it's always fun to play with your friends.\n\n")
    if number_of_players > 3:
        print("\nGreat, it's a lot of players. Fun is awaiting for you, guys!\n\n")

    print("Next, I need to know your names. Please, add your names in turn.")
    player_names = get_player_names(number_of_players)
    print(
        f"\nAmazing!!! It's good to see you here, {', '.join(player_names)}. Have enjoyable time!\n"
    )

    print(
        "Last but not least I need to know in which difficulty level do you want to play."
    )
    difficulty_level = get_difficulty_level()
    words = get_wordlist(difficulty_level)

    # create instances for each player
    for player in player_names:
        Player(player)

    print("\nAlrighty!!! We can start the game now. Good luck to all of you.\n\n")
    game = Game(number_of_players=number_of_players)
    game.start(Player.all(), words)


if __name__ == "__main__":
    main()
