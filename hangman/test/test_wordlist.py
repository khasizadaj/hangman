import unittest

from utils import wordlist
from utils.wordlist import get_difficulty_value, get_wordlist


class TestWordList(unittest.TestCase):
    def test_get_wordlist(self):
        test = wordlist.get_wordlist(1)
        self.assertListEqual(test, wordlist.ALL_WORDS["easy"])

        test = wordlist.get_wordlist(2)
        self.assertListEqual(test, wordlist.ALL_WORDS["medium"])

        test = wordlist.get_wordlist(3)
        self.assertListEqual(test, wordlist.ALL_WORDS["hard"])

        test = wordlist.get_wordlist(0)
        real = (
            wordlist.ALL_WORDS["easy"]
            + wordlist.ALL_WORDS["medium"]
            + wordlist.ALL_WORDS["hard"]
        )
        self.assertListEqual(test, real)

    def test_get_all_words(self):
        test = wordlist.get_all_words()
        real = (
            wordlist.ALL_WORDS["easy"]
            + wordlist.ALL_WORDS["medium"]
            + wordlist.ALL_WORDS["hard"]
        )
        self.assertListEqual(test, real)


if __name__ == "__main__":
    unittest.main()
