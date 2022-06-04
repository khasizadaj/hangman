"""Module contains class&functions related to players."""


class Player:
    """Implements player logic."""

    _all_players = []
    hints_count: int = 3

    def __init__(self, name: str = "Player X", point: int = 0):
        self._all_players.append(self)

        self.name = name
        self.point = point

    def add_point(self, custom_word=True):
        if custom_word:
            added_point = 2
        else:
            added_point = 1

        self.point += added_point
        return self.point

    @classmethod
    def all(cls):
        return cls._all_players

    @classmethod
    def points(cls):
        """
        Function return leaderboard table for all players.
        It consists of name and points of all players.
        """
        # TODO Consider having different people with same name
        return {player.name: player.point for player in cls.all()}

    def __str__(self) -> str:
        return self.name.capitalize()
