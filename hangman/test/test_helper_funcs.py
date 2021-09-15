import unittest
from typing import List

from utils.helper_funcs import (
    get_guess_occurrences, get_guess_status, get_emotion, get_letter_message)
from utils.words import get_mapped_letters


class HelperFunctionsTest(unittest.TestCase):

    def setUp(self):
        self.letters_1 = get_mapped_letters("hangman")
        self.letters_2 = get_mapped_letters("sense")

    def test_get_guess_occurrences(self):
        script = get_guess_occurrences("a", self.letters_1)
        self.assertIsInstance(script, List)

        script = get_guess_occurrences(mapped_letters=self.letters_2)
        real = "Guessed letter is required."
        self.assertEqual(script, real)

        script = get_guess_occurrences(guessed_letter="h")
        real = "Dictionary of mapped letters is required."
        self.assertEqual(script, real)

        script = get_guess_occurrences("s", self.letters_2)
        real = [0, 3]
        self.assertEqual(script, real)

        script = get_guess_occurrences("h", self.letters_1)
        real = [0]
        self.assertEqual(script, real)

        script = get_guess_occurrences("h", self.letters_2)
        real = [-1]
        self.assertEqual(script, real)

    def test_get_guess_status(self):
        occurrences_1 = [-1]
        script = get_guess_status(occurrences_1)
        self.assertFalse(script)

        occurrences_2 = []
        script = get_guess_status(occurrences_2)
        self.assertFalse(script)

        script = get_guess_status()
        real = "Occurences (positions) are required."
        self.assertEqual(script, real)

        occurrences_3 = [0, 5]
        script = get_guess_status(occurrences_3)
        self.assertTrue(script)

    def test_get_emotion(self):
        script = get_emotion(status=False)
        real = "We'll be successful next time. Cheer up!"
        self.assertEqual(script, real)

        script = get_emotion(status=True)
        real = "Hooray! We did it."
        self.assertEqual(script, real)

    def test_get_letter_message(self):
        script = get_letter_message(status=True, guessed_letter='a')
        real = 'Letter "a" is in the word.'
        self.assertEqual(script, real)

        script = get_letter_message(status=False, guessed_letter='a')
        real = 'Letter "a" is not in the word.'
        self.assertEqual(script, real)

        script = get_letter_message(guessed_letter='a')
        real = "Status is required."
        self.assertEqual(script, real)

        script = get_letter_message(status=True)
        real = "Letter is required."
        self.assertEqual(script, real)


if __name__ == "__main__":
    unittest.main()
