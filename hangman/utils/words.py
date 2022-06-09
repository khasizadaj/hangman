"""
Module contains functions related to different steps of the game.
"""

import copy
from getpass import getpass
from random import randint
from typing import Dict, List, Optional, Tuple, Union

from .helper_funcs import add_linebreak, get_emotion, get_letter_message
from .wordlist import get_wordlist


class Word:
    """Class implements the methods related to word that is guessed by user."""

    actions = ["show", "hint"]

    def __init__(self, word: Dict):
        self._word_dict = word
        self._masked = self.mask_word(word["word"])
        self.mapped_letters = self.get_mapped_letters()

    @property
    def plain(self):
        """Returns the plain word."""

        return self._word_dict["word"]

    @property
    def hint(self) -> Optional[str]:
        """Returns a hint, if available."""

        return self._word_dict.get("hint", None)

    @property
    def masked(self) -> List[str]:
        """Returns masked word."""

        return self._masked

    @staticmethod
    def mask_word(plain_word: str) -> List[str]:
        """
        Function returns masked letters of word in a list format. Masking is
        replacement of letters with underscores.

        Args:
            word: provided string
        """

        return ["_" for _ in plain_word]

    def get_mapped_letters(self) -> Dict[str, List[int]]:
        """
        Functions returns dictionary of letters and corresponding indices of those
        letters.
        """

        dictionary = {}
        for index, letter in enumerate(self.plain):
            dict_mem = dictionary.get(letter, None)
            if dict_mem is not None:
                dictionary[letter].append(index)
            else:
                dictionary[letter] = [index]

        return dictionary

    @property
    def pretty_masked(self) -> str:
        """
        Function returns string version of masked word by adding a space between
        each letter.
        """

        return " ".join(self.masked)

    def guess_word(self, hints_count: int) -> bool:
        """
        Implements word guessing logic of the game.
        """

        is_first_guess = True
        all_guessed_letters = []
        chances = 6
        hint_option_prompted = False
        hint_used = False

        print(self.pretty_masked)
        add_linebreak()

        while self.is_found() is False and chances > 0:

            if is_first_guess:
                is_first_guess = False

            guessed_letter, all_guessed_letters = get_guess(
                all_guessed_letters, self, first_time=is_first_guess
            )

            if guessed_letter in self.actions:
                add_linebreak(quantity=2)
                if guessed_letter == "show":
                    print(self.get_pretty_used_letters(all_guessed_letters))
                elif guessed_letter == "hint":
                    if self.hint is None:
                        print("Sorry, word doesn't have a hint or it is custom word.")
                    elif hint_used is True:
                        print(
                            f'You have already asked for a hint. It was "{self.hint}"'
                        )
                    else:
                        if hints_count > 0:
                            hints_count -= 1
                            hint_used = True
                            print(f"\n{self.get_hint()}")
                            print(f"You have {hints_count} hints available.")
                        else:
                            print("Unfortunately, you cannot have hints anymore.")
                add_linebreak()
                continue

            is_guessed_correctly = self.get_guess_status(guessed_letter)

            if is_guessed_correctly:
                self.update_masked_word(guessed_letter)

                if self.is_found():
                    break
            else:
                chances -= 1
                print(f"\nYou missed. You have {chances} chances left.")

            if chances == 2 and hint_option_prompted is False and hint_used is False:
                hint_wanted = input(
                    "Would you like to get a hint for the word? [Y(y)/N(n)]: "
                )
                if hint_wanted == "y":
                    if self.hint is None:
                        print("Sorry, word doesn't have a hint or it is custom word.")
                    else:
                        if hints_count > 0:
                            hints_count -= 1
                            hint_option_prompted = True
                            print(f"\n{self.get_hint()}")
                            print(f"You have {hints_count} hints available.")
                        else:
                            print("Unfortunately, you cannot have hints anymore.")

            add_linebreak()
            message = get_letter_message(is_guessed_correctly, guessed_letter)
            emotion = get_emotion(is_guessed_correctly)
            print(f"{emotion} {message}")

            # two line breaks
            add_linebreak(quantity=2)

            print(self.pretty_masked)
            add_linebreak()

        if chances == 0:
            print(
                f'\nYou couldn\'t find the word succesfully. The word was "{self.plain}".\n'
            )
            return False, hints_count

        print(
            f'\nAaaand "{guessed_letter}" is last letter.'
            + f'Wow, congrats, ingenious! You found the word, it was "{self.plain}".\n'
        )
        return True, hints_count

    def get_letter_occurrences(
        self,
        guessed_letter: Optional[str] = None,
    ) -> Union[List[int], str]:
        """
        Function returns occurences (indices) of guessed_letter in the word which
        already defined in mapped_letters.

        Args:
            guessed_letter: string of letter that is guessed
        """

        if guessed_letter is None:
            return "Guessed letter is required."
        if self.mapped_letters is None:
            return "Dictionary of mapped letters is required."

        letters = [letter for letter, _ in self.mapped_letters.items()]
        if guessed_letter not in letters:
            return None

        indices = self.mapped_letters[guessed_letter]
        return indices

    @staticmethod
    def get_pretty_used_letters(used_letters: List[str]) -> str:
        """
        Function returns a string that shows the set of used letters.

        Args:
            letters: list of used letters
        """

        if len(used_letters) < 1:
            return "You have not used any letters yet. What are you waiting for!?"

        return f"You have used these letters so far: \"{', '.join(used_letters)}\""

    def get_guess_status(self, guessed_letter: str) -> bool:
        """
        Returns status of guessed letter by checking the occurrences of letter.

        Args:
            occurrences: indices of letters in a word
        """
        occurrences = self.get_letter_occurrences(guessed_letter)
        if occurrences is None:
            return False

        return True

    def update_masked_word(self, guessed_letter: str) -> List[str]:
        """
        Function replaces underscores with letter that is found in the masked list of
        letter and return updated word.

        Args:
            masked_word: list of underscores (or already guessed letters in some
                cases) that represents word user is looking for
            letter: letter (string) that is guessed correctly by user
            occurences: indice of guessed letter in the word
        """
        if guessed_letter in self._masked:
            return self._masked

        occurences = self.get_letter_occurrences(guessed_letter)
        for index in occurences:
            self._masked[index] = guessed_letter
        return self._masked

    def is_found(self) -> bool:
        """
        Function returns boolean indicating whether word is already found/guessed.

        Args:
            masked_word: list of underscores (or already guessed letters in some
                cases) that represents word user is looking for
        """

        return "_" not in self.masked

    def get_hint(self) -> Optional[str]:
        """Function returns string with hint for the word."""

        if self.hint is None:
            return None

        return f"Hint: {self.hint}"

    def details(self) -> str:
        """
        Function returns details about word.

        Args:
            word: word that is provided
        """

        return f"Word contains {len(self.plain)} letters. Let's find them!"


class Words:
    """Class implements the methods related to words."""

    def __init__(
        self, difficulty_level: str = "all", wordlist: List[Dict] = None
    ) -> None:
        if wordlist is None:
            self._wordlist: List[str] = get_wordlist(difficulty_level)
        else:
            self._wordlist = wordlist

    def get_words(self) -> List[str]:
        """Returns a list of all words."""
        return self._wordlist

    def get_random_word(self) -> Word:
        """
        Function return random word from the provided list of words.

        Args:
            words: List of words in string format
        """

        if len(self._wordlist) == 0:
            return ""

        rand_int = randint(0, len(self._wordlist) - 1)
        return Word(self._wordlist[rand_int])


def get_custom_word() -> Word:
    """
    Function gets custom word provided by the user.
    """
    custom_word_input = getpass(
        "Choose your friend and ask him/her to type custom word"
        + "(typed letters will be not shown, but registered): "
    )

    word_is_fine = False
    if custom_word_input.isalpha():
        word_is_fine = True

    while word_is_fine is False:
        custom_word_input = input(
            "\nPlease enter proper custom word. It can only contain letters."
            + "\nNote: in order to help you, I deactivated hidden typing."
            + "Now you will see what you type. Cheers!\n\nType your word here: "
        )

        if custom_word_input.isalpha():
            word_is_fine = True

    custom_word = Word({"word": custom_word_input, "hint": None})
    return custom_word


def check_input(input_str: str) -> Tuple[bool, str]:
    """
    Function check if input provided is correct. If not, returns helper text with boolean
    value to make user provide input correctly. If input is correct, returns empty string
    with boolean value.

    Args
        input_str: input that is provided by user
    """
    # if len(input_str) == 1 and input_str.isalpha():
    #     return True, ""

    if isinstance(input_str, str) is False:
        helper_text = "Input is not string. Provide a string of a letter."
        return False, helper_text

    if input_str.isnumeric():
        helper_text = "You need to provide a letter, not number. What is your guess? "
        return False, helper_text

    if len(input_str) != 1:
        helper_text = "You need to provide one letter. What is your guess? "
        if len(input_str) == 0:
            helper_text = "You need to provide one letter, it can't be empty. What is your guess? "

        return False, helper_text

    if input_str.isalpha() is False:
        helper_text = (
            "You need to provide a letter, this is not supported. What is your guess? "
        )
        return False, helper_text

    return True, ""


def is_provided(input_str: str, typed_letters: List[str]) -> bool:
    """
    Function returns boolean value indicating whether given letter is provided
    before or not.

    Args:
        input_str: last provided letter
        typed_letters: list of letters that are provided before
    """

    return input_str in typed_letters


def get_guess(typed_letters: List[str], word: Word, first_time: bool = False) -> str:
    """
    Function prompts user to guess a letter and returns provided guess. It repeatedly
    asks for new guess until input meets requirements (`check_input` function).

    Args:
        typed_letters: list of letters that are already provided by user
        first_time: boolean value indicating whether input is asked for first
            time
    """

    if first_time:
        message = "What's your first guess, clever?: "
    else:
        message = "Time for next guess. What is the letter? "

    used_letters = copy.deepcopy(typed_letters)
    used_letters.sort()

    # this counter is used to inform user if letter is provided before.
    # it only counts current inputs. it is reset after new and correct input.
    repeat_input_counter = 0

    # input_is_correct: input is letter and never used before
    input_is_correct = False
    while input_is_correct is not True:
        input_str = input(message)

        if input_str.lower() in word.actions:
            return input_str.lower(), used_letters

        # input_is_valid: if True, it means input doesn't have any errors and is
        # letter input_message: if input_is_valid is false, it contains error
        # message. Otherwise, it's empty string.
        input_is_valid, input_message = check_input(input_str)
        if input_is_valid:
            is_provided_before = is_provided(input_str, used_letters)
            if is_provided_before is False:
                used_letters.append(input_str)
                input_is_correct = True

            else:
                if repeat_input_counter >= 2:
                    add_linebreak()
                    print(word.get_pretty_used_letters(used_letters))

                repeat_input_counter += 1
                message = "You have already used this letter. What is your guess? "

        else:
            message = input_message

    return input_str, used_letters


if __name__ == "__main__":
    print("Module contains helper functions that are related to words for hangman.")
