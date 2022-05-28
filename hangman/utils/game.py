"""
Module contains functions related to game logic. It implements the following:
- single player mode
- multi players mode
"""

import sys
from getpass import getpass
from typing import List

from utils.helper_funcs import (
    add_linebreak,
    get_next_player_number,
    get_pretty_leaderboard,
)
from utils.player import Player
from utils.words import get_random_word, guess_word


class Game:
    def __init__(self, number_of_players: int = 1, winning_point: int = 3):
        self.number_of_players = number_of_players
        self.winning_point = winning_point
        self.curr_player_id = 1
        self._is_continuing = True

    def start(self, players: List[Player], words: List[str]) -> None:
        if self.number_of_players > 1:
            self.multiplayer_mode(players, words)

        self.single_player_mode(players, words)

    def get_current_player(self, players: List[Player]) -> Player:
        return players[self.curr_player_id - 1]

    def is_winner(self, player: Player) -> bool:
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

    def single_player_mode(self, player: Player, words: List[str]) -> None:
        """
        Function handles the game for single player.

        Args:
            player_name: name of the player
        """

        while self.is_continuing:
            message = f"Let's find this word, {player.name}"
            print(message)
            add_linebreak()

            rand_word = get_random_word(words)
            status = guess_word(rand_word)
            if status:
                player.add_point()

            points = Player.points()
            print(get_pretty_leaderboard(points))

            # asking if user wants to continue
            choice = input("Do you want to continue? (Y/N): ")
            if choice.lower() == "n":
                self.update_continuation_state()

        return None

    def multiplayer_mode(self, players: List[Player], words: List[str]) -> None:
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

            user_will_add_custom_word = input(
                "Do you wanna challange you friend by yourself? [Y(y)/N(n)] "
            )
            if user_will_add_custom_word.lower() == "y":
                custom_word = getpass(
                    "Enter custom word (typed letters will be not shown, but registered): "
                ).lower()
            else:
                custom_word = None

            rand_word = custom_word or get_random_word(words)

            status = guess_word(rand_word)
            if status:
                curr_player.add_point()
                if self.is_winner(curr_player):
                    self.update_continuation_state()
                    break

            # curr_player_num = get_next_player_number(curr_player_num, len(players))
            self.move_to_next_player()

            print(get_pretty_leaderboard(Player.points()))

        print(f"Winner is {curr_player}")
        sys.exit()


if __name__ == "__main__":
    print("Module contains functions for single and multiple player functionality.")
