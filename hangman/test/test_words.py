import unittest
from typing import Dict, List

from utils.words import (get_random_word, get_masked_word, get_mapped_letters,
                         update_masked_word, get_pretty_masked_word, WORDLIST)


class WordFunctionsTest(unittest.TestCase):

    def setUp(self):
        self.words = ["and", "hangman", "crazy"]
        self.test_word_1 = "and"
        self.test_word_2 = "hangman"
        self.test_word_3 = "crazy"

        self.test_masked_word_1 = ["_", "_", "_"]
        self.test_masked_word_2 = ["_", "_", "_", "_", "_", "_", "_"]
        self.test_masked_word_3 = ["_", "_", "_", "_", "_"]

        self.test_partially_masked_word_1 = ["_", "n", "_"]
        self.test_partially_masked_word_2 = ["_", "a", "_", "_", "_", "a", "_"]
        self.test_partially_masked_word_3 = ["_", "_", "a", "_", "_"]

    def test_get_random_word(self):
        script = get_random_word(self.words)
        self.assertIsInstance(script, str)

        script = get_random_word([])
        real = ""
        self.assertEqual(script, real)

    def test_get_mapped_letters(self):
        script = get_mapped_letters(self.test_word_1)
        self.assertIsInstance(script, Dict)

        script = get_mapped_letters(self.test_word_1)
        real = {"a": [0], "n": [1], "d": [2]}
        self.assertEqual(script, real)

        script = get_mapped_letters(self.test_word_2)
        real = {"h": [0], "a": [1, 5], "n": [2, 6], "g": [3], "m": [4]}
        self.assertEqual(script, real)

    def test_get_masked_word(self):
        script = get_masked_word("test")
        real = ["_", "_", "_", "_"]
        self.assertEqual(real, script)

        script = get_masked_word("test")
        real = ["t", "_", "_", "_"]
        self.assertNotEqual(real, script)

        script = len(get_masked_word("hangman"))
        real = len("hangman")
        self.assertEqual(real, script)

        script = len(get_masked_word("hangman"))
        real = len("hangmana")
        self.assertNotEqual(real, script)

    def test_update_masked_word(self):
        script = update_masked_word(self.test_masked_word_1, "a", [0])
        self.assertIsInstance(script, List)

        script = update_masked_word(self.test_masked_word_1, "a", [0])
        real = ["a", "_", "_"]
        self.assertEqual(real, script)

        script = update_masked_word(self.test_masked_word_3, "a", [])
        real = self.test_masked_word_3
        self.assertIs(real, script)

        script = update_masked_word(self.test_masked_word_2, "", [1])
        real = self.test_masked_word_2
        self.assertIs(real, script)

        script = update_masked_word(["_", "_"], "a", [])
        real = ["_", "_"]
        self.assertIsNot(real, script)

        script = update_masked_word(self.test_masked_word_2, "a", [1, 5])
        real = self.test_partially_masked_word_2
        self.assertEqual(real, script)

    def test_get_pretty_masked_word(self):
        script = get_pretty_masked_word(self.test_masked_word_1)
        real = "_ _ _"
        self.assertEqual(real, script)

        script = get_pretty_masked_word(self.test_partially_masked_word_1)
        real = "_ n _"
        self.assertEqual(real, script)


if __name__ == "__main__":
    unittest.main()
