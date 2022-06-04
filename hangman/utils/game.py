"""
Module contains functions related to game logic. It implements the following:
- single player mode
- multi players mode
"""

import sys
import time
from typing import List

from utils.helper_funcs import add_linebreak, clear_console, get_pretty_leaderboard
from utils.player import Player
from utils.words import Words, get_custom_word


class Game:
    """
    Implements game logic of the "Hangman" game. It contains single player and
    multi player game modes.
    """

    def __init__(
        self,
        words: Words,
        players=List[Player],
        number_of_players: int = 1,
        winning_point: int = 3,
    ):
        self.words = words
        self.players = players
        self.number_of_players = number_of_players
        self.winning_point = winning_point
        self.curr_player_id = 1
        self._is_continuing = True

    def start(self) -> None:
        """
        Function initiates the game based on the number of players in the game.
        """
        if self.number_of_players > 1:
            self.multiplayer_mode(self.players, self.words)

        self.single_player_mode(self.players[0], self.words)

    def get_current_player(self, players: List[Player]) -> Player:
        """Function returns the current player in the game."""

        return players[self.curr_player_id - 1]

    def is_winner(self, player: Player) -> bool:
        """Function returns whether player has won the game."""

        return player.point == self.winning_point

    def move_to_next_player(self) -> int:
        if self.number_of_players == 1:
            return self.curr_player_id

        self.curr_player_id = self.curr_player_id + 1
        if self.curr_player_id > self.number_of_players:
            self.curr_player_id = self.curr_player_id % self.number_of_players

        return self.curr_player_id

    def update_continuation_state(self):
        """
        Sets the continuation state to be False, i.e. ends the game.
        """
        self._is_continuing = False
        return self._is_continuing

    @property
    def is_continuing(self):
        return self._is_continuing

    def single_player_mode(self, player: Player, words: Words) -> None:
        """
        Function handles the game for single player.

        Args:
            player_name: name of the player
        """

        while self.is_continuing:
            message = f"Let's find this word, {player.name}"
            print(message)
            add_linebreak()

            rand_word = words.get_random_word()
            status, updated_hints_count = rand_word.guess_word(player.hints_count)
            player.hints_count = updated_hints_count

            if status:
                print("\nUpdating leaderboard ...")
                player.add_point()
            else:
                print("\nGetting leaderboard ...")
            time.sleep(3)
            clear_console()

            points = Player.points()
            self.print_leaderboard(points)
            add_linebreak()

            # asking if user wants to continue
            choice = input("Do you want to continue? (Y/N): ")
            if choice.lower() == "n":
                self.update_continuation_state()

        return None

    def multiplayer_mode(self, players: List[Player], words: Words) -> None:
        """
        Function handles the game for multiple players.

        Args:
            player_names: names of the players
        """

        while True:
            curr_player = self.get_current_player(players)
            message = f"It's your turn, {curr_player}"
            print(message)
            add_linebreak()

            user_choice = input(
                "Do you wanna be challanged by your friend? [Y(y)/N(n)] "
            )
            if user_choice.lower() == "y":
                custom_word = get_custom_word()
            else:
                custom_word = None

            word = custom_word or words.get_random_word()
            print(word.details)

            is_guessed = word.guess_word()
            if is_guessed:
                curr_player.add_point()

                if self.is_winner(curr_player):
                    self.update_continuation_state()
                    break

                print("\nUpdating leaderboard ...")
            else:
                print("\nGetting leaderboard ...")

            time.sleep(3)
            clear_console()

            self.move_to_next_player()

            self.print_leaderboard(Player.points())

        print(f"Winner is {curr_player}")
        sys.exit()

    def print_leaderboard(self, points) -> None:
        """Prints the leaderboard in a preety format."""

        print("LEADERBOARD\n==============\n")
        print(get_pretty_leaderboard(points))
        print("--------------")


if __name__ == "__main__":
    print("Module contains functions for single and multiple player functionality.")
