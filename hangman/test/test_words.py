import unittest
from io import StringIO
import sys
from typing import Dict, List

from unittest import mock
from unittest.mock import patch
from utils.words import (get_random_word, get_masked_word, get_mapped_letters,
                         update_masked_word, get_pretty_masked_word, check_provision,
                         check_input, get_pretty_used_letters, get_guessed_letter,
                         show_used_letters, get_word_details, word_is_found, guess_word)


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

    def test_check_provision(self):
        script = check_provision("a", ["a", "b"])
        self.assertTrue(script)

        script = check_provision("a", ["b", "c"])
        self.assertFalse(script)

        script = check_provision("ab", ["b", "c"])
        self.assertFalse(script)

        script = check_provision("", ["b", "c"])
        self.assertFalse(script)

        script = check_provision(None, ["b", "c"])
        self.assertFalse(script)

        script = check_provision(1, ["b", "c"])
        self.assertFalse(script)

    def test_check_input(self):
        input_is_valid, input_message = check_input("a")
        real_bool = True
        self.assertEqual(real_bool, input_is_valid)
        real_message = ""
        self.assertEqual(real_message, input_message)

        input_is_valid, input_message = check_input("ab")
        real_bool = False
        self.assertEqual(real_bool, input_is_valid)
        real_message = "You need to provide one letter. What is your guess? "
        self.assertEqual(real_message, input_message)

        input_is_valid, input_message = check_input("[1]")
        real_bool = False
        self.assertEqual(real_bool, input_is_valid)
        real_message = "You need to provide one letter. What is your guess? "
        self.assertEqual(real_message, input_message)

        input_is_valid, input_message = check_input(1)
        real_bool = False
        self.assertEqual(real_bool, input_is_valid)
        real_message = "Input is not string. Provide a string of a letter."
        self.assertEqual(real_message, input_message)

        input_is_valid, input_message = check_input(1.12)
        real_bool = False
        self.assertEqual(real_bool, input_is_valid)
        real_message = "Input is not string. Provide a string of a letter."
        self.assertEqual(real_message, input_message)

        input_is_valid, input_message = check_input([1])
        real_bool = False
        self.assertEqual(real_bool, input_is_valid)
        real_message = "Input is not string. Provide a string of a letter."
        self.assertEqual(real_message, input_message)

        input_is_valid, input_message = check_input(None)
        real_bool = False
        self.assertEqual(real_bool, input_is_valid)
        real_message = "Input is not string. Provide a string of a letter."
        self.assertEqual(real_message, input_message)

        input_is_valid, input_message = check_input("")
        real_bool = False
        self.assertEqual(real_bool, input_is_valid)
        real_message = "You need to provide one letter, it can't be empty. What is your guess? "
        self.assertEqual(real_message, input_message)

        input_is_valid, input_message = check_input("@")
        real_bool = False
        self.assertEqual(real_bool, input_is_valid)
        real_message = "You need to provide a letter, this is not supported. What is your guess? "
        self.assertEqual(real_message, input_message)

    def test_get_pretty_used_letters(self):
        script = get_pretty_used_letters(["a", "b", "c"])
        real = f"You have used these letters so far: \"a, b, c\""
        self.assertEqual(real, script)

        script = get_pretty_used_letters([])
        real = "You have not used any letters yet. What are you waiting for!?"
        self.assertEqual(real, script)

    def test_show_used_letters_with_letters(self):
        real = '\nYou have used these letters so far: "a, b, c"\n\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            show_used_letters(["a", "b", "c"])
            script = fake_out.getvalue()
            self.assertEqual(script, real)

    def test_show_used_letters_no_letter(self):
        real = '\nYou have not used any letters yet. What are you waiting for!?\n\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            show_used_letters([])
            script = fake_out.getvalue()
            self.assertEqual(script, real)

    def test_get_word_details(self):
        script = get_word_details("hey")
        real = "Word contains 3 letters. Let's find them!"
        self.assertEqual(real, script)

        script = get_word_details("activity")
        real = "Word contains 8 letters. Let's find them!"
        self.assertEqual(real, script)

        script = get_word_details("Active")
        real = "Word contains 6 letters. Let's find them!"
        self.assertEqual(real, script)

    def test_word_is_found(self):
        script = word_is_found(["_", "a", "g"])
        self.assertFalse(script)

        script = word_is_found(["b", "a", "g"])
        self.assertTrue(script)

    @mock.patch('utils.words.input', create=True)
    def test_get_guessed_letter(self, input):
        input.side_effect = ["a", "d"]
        s_l, s_p_ls = get_guessed_letter(["a", "b", "c"])
        r_l = "d"
        self.assertEqual(r_l, s_l)
        r_p_ls = ["a", "b", "c", "d"]
        self.assertEqual(r_p_ls, s_p_ls)

        input.side_effect = ["a", "1", "c", "e"]
        s_l, s_p_ls = get_guessed_letter(["a", "b", "c"])
        r_l = "e"
        self.assertEqual(r_l, s_l)
        r_p_ls = ["a", "b", "c", "e"]
        self.assertEqual(r_p_ls, s_p_ls)

        input.side_effect = ["a", "1", "@", "f"]
        s_l, s_p_ls = get_guessed_letter(["a", "b", "c"])
        r_l = "f"
        self.assertEqual(r_l, s_l)
        r_p_ls = ["a", "b", "c", "f"]
        self.assertEqual(r_p_ls, s_p_ls)

    @mock.patch('utils.words.input', create=True)
    def test_guess_word(self, input):
        input.side_effect = ["a", "d", "d", "v", "s", "q", "m", "l"]
        script: bool = guess_word(custom_word="anger")
        self.assertFalse(script)

        input.side_effect = ["e", "a", "g", "r"]
        script: bool = guess_word(custom_word="eager")
        self.assertTrue(script)

        input.side_effect = ["a"]
        script: bool = guess_word(custom_word="a")
        self.assertTrue(script)


if __name__ == "__main__":
    unittest.main()
