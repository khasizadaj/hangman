import unittest
from typing import Dict

from utils.player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.test_1 = Player(name="Crazy 8")
        self.test_2 = Player(name="Crazy 9")

    def test_player_details(self):
        self.assertIsInstance(self.test_1, Player)
        self.assertEqual(self.test_1.name, "Crazy 8")
        self.assertEqual(self.test_1.point, 0)

    def test_get_all_players(self):
        all_players = Player.all()
        self.assertIsInstance(all_players, list)
        self.assertEqual(len(all_players), 2)

    def test_points_initial_state(self):
        test_points = Player.points()
        self.assertIsInstance(test_points, Dict)

        real_points = {self.test_1.name: 0, self.test_2.name: 0}
        self.assertDictEqual(test_points, real_points)

    def test_points_during_game(self):
        self.test_1.add_point()
        self.test_1.add_point()
        self.test_2.add_point()
        self.test_2.add_point()
        self.test_2.add_point()
        self.test_2.add_point()

        test_points = Player.points()
        real_points = {self.test_1.name: 2, self.test_2.name: 4}
        self.assertDictEqual(test_points, real_points)

    def test_point_incrementating(self):
        self.assertEqual(self.test_1.point, 0)

        self.test_1.add_point()
        self.assertEqual(self.test_1.point, 1)

        self.test_1.add_point()
        self.assertEqual(self.test_1.point, 2)

        self.test_2.add_point()
        self.assertEqual(self.test_2.point, 1)


if __name__ == "__main__":
    unittest.main()
