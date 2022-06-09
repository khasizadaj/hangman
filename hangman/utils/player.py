"""Module contains class&functions related to players."""

from string import digits


class Player:
    """Implements player logic."""

    _all_players = []
    hints_count: int = 3

    def __init__(self, name: str = "Player X", point: int = 0):
        names = [player.name for player in self._all_players if player.name == name]

        if len(names) != 0:
            self.name = f"{name} {digits[len(names)]}"
        else:
            self.name = name
        self.point = point
        self._all_players.append(self)

    def add_point(self, custom_word=False):
        """Adds point(s) for the plaayer that guesses the word correctly."""

        if custom_word:
            added_point = 2
        else:
            added_point = 1

        self.point += added_point
        return self.point

    @classmethod
    def all(cls):
        """Return list of all players."""

        return cls._all_players

    @classmethod
    def points(cls):
        """
        Function return leaderboard table for all players.
        It consists of name and points of all players.
        """

        return {player.name: player.point for player in cls.all()}

    def __str__(self) -> str:
        return self.name.capitalize()


if __name__ == "__main__":
    print("Module contains functions related to player for hangman.")
