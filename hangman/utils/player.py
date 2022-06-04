class Player:
    """Implements player logic."""

    _all_players = []

    def __init__(self, name: str = "Player X", point: int = 0):
        self._all_players.append(self)

        self.name = name
        self.point = point

    def add_point(self):
        self.point += 1
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
