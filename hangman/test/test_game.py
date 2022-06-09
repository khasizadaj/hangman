# class Game:
#     def is_current_player(self, players: List[Player]) -> Player:
#         return players[self.curr_player_id - 1]

#     def is_winner(self, player: Player) -> bool:
#         return player.point == self.winning_point

import unittest

from utils.game import Game
from utils.player import Player


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game_1 = Game(winning_point=2)
        self.game_2 = Game(number_of_players=2, winning_point=3)

        self.player_1 = Player(name="Crazy 7")
        self.player_1.add_point()
        self.player_1.add_point()
        self.player_2 = Player(name="Crazy 8")
        self.player_2.add_point()

    def test_game_details_initial(self):
        self.assertEqual(self.game_1.winning_point, 2)
        self.assertEqual(self.game_2.winning_point, 3)

        self.assertEqual(self.game_1.number_of_players, 1)
        self.assertEqual(self.game_2.number_of_players, 2)

        self.assertEqual(self.game_1.curr_player_id, 1)

        self.assertTrue(self.game_1.is_continuing)
        self.assertTrue(self.game_2.is_continuing)

    def test_game_details_order_of_players(self):
        # Changing current player id
        #   Turn 0: 1st
        #   Turn 1: 1st
        #   Turn 2: 1st
        self.assertEqual(self.game_1.curr_player_id, 1)
        curr_player_id = self.game_1.move_to_next_player()
        self.assertEqual(curr_player_id, 1)
        curr_player_id = self.game_1.move_to_next_player()
        self.assertEqual(curr_player_id, 1)

        # Changing current player id
        #   Turn 0: 1st
        #   Turn 1: 2st
        #   Turn 2: 1st
        self.assertEqual(self.game_2.curr_player_id, 1)
        curr_player_id = self.game_2.move_to_next_player()
        self.assertEqual(curr_player_id, 2)
        curr_player_id = self.game_2.move_to_next_player()
        self.assertEqual(curr_player_id, 1)

    def test_game_details_continuation(self):
        # initial state
        self.assertTrue(self.game_1.is_continuing)

        # game finished
        self.game_1.update_continuation_state()
        self.assertFalse(self.game_1.is_continuing)

    def test_is_current_player(self):
        players = [self.player_1, self.player_2]
        curr_player = self.game_2.get_current_player(players)
        self.assertEqual(curr_player, self.player_1)

        self.game_2.move_to_next_player()
        curr_player = self.game_2.get_current_player(players)
        self.assertNotEqual(curr_player, self.player_1)
        self.assertEqual(curr_player, self.player_2)

    def test_is_winner(self):
        self.assertTrue(self.game_1.is_winner(self.player_1))
        self.assertFalse(self.game_1.is_winner(self.player_2))


if __name__ == "__main__":
    unittest.main()
