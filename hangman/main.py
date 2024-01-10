from string import printable

from utils.game import Game
from utils.helper_funcs import (
    get_difficulty_level,
    get_guidelines,
    get_player_names,
    get_winning_point,
)
from utils.player import Player
from utils.words import Words


def main() -> None:
    """Binds all game elements in one place."""

    # print guidelines
    guidelines = get_guidelines()
    print(guidelines)

    print("First, I need to know how many players will be in the game.")
    number_of_players = int(input("Type number of players here: "))
    if 3 >= number_of_players > 1:
        print("\nGreat, it's always fun to play with your friends.\n\n")
        print("Next, I need to know your names. Please, add your names.")
    if number_of_players > 3:
        print("\nGreat, it's a lot of players. Fun is awaiting for you, guys!\n\n")
        print("Next, I need to know your names. Please, add your names in turn.")

    player_names = get_player_names(number_of_players)
    if len(player_names) > 1:
        print(
            f"\nAmazing!!! It's good to see you here, {', '.join(player_names)}. Have enjoyable time!\n"
        )
        print(
            '\nOptional | Until how many points would you like to play? Default winning point will be 5 points. Press "ENTER" to have default value.'
        )
        winning_point = get_winning_point()
    else:
        print(
            f"\nAmazing!!! It's good to see you here, {player_names[0]}. Have enjoyable time!\n"
        )
        winning_point = None

    print(
        "Last but not least I need to know in which difficulty level do you want to play."
    )
    difficulty_level = get_difficulty_level()
    words = Words(difficulty_level)

    # create instances for each player
    for player in player_names:
        Player(player)

    print("\nAlrighty!!! We can start the game now. Good luck to all of you.\n\n")
    game = Game(
        number_of_players=number_of_players,
        words=words,
        players=Player.all(),
        winning_point=winning_point,
    )
    game.start()


if __name__ == "__main__":
    main()
