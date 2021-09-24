from typing import List, Dict, Union
from random import randint

from .helper_funcs import (get_guess_occurrences, get_guess_status,
                           get_emotion, get_letter_message, add_linebreak)

WORDLIST = {"easy": ["a", "about", "above", "across", "act", "actor", "active", "activity",
                     "add", "afraid", "after", "again", "age", "ago", "agree", "air", "all",
                     "alone", "along", "already", "always", "am", "amount", "an", "and", "angry",
                     "another", "answer", "any", "anyone", "anything", "anytime", "appear",
                     "apple", "are", "area", "arm", "army", "around", "arrive", "art", "as",
                     "ask", "at", "attack", "aunt", "autumn", "away"]}


def get_random_word(words: List[str]) -> str:
    """
    Function return random word from the provided list of words.

    Args:
        words: List of words in string format
    """

    if len(words) == 0:
        return ""

    rand_int = randint(0, len(words) - 1)
    return words[rand_int]


def get_guessed_letter(provided_letters: List[str], first_time: bool = False) -> str:
    """
    Function prompts user for guess and returns provided guess. It repeatedly 
    asks for new guess until input meets requirements (`check_input` function).

    Args:
        first_time: boolean value indicating whether input is asked for first 
            time 
    """

    if first_time:
        message = "What's your first guess, clever?: "
    else:
        message = "Time for next guess. What is the letter? "

    repeat_input_counter = 0
    input_is_correct = False
    while input_is_correct != True:
        input_str = input(message)

        used_letters = [*provided_letters]
        if input_str == "show":
            add_linebreak()
            print(show_used_letters(used_letters))

        check = check_input(input_str)
        if check == True:
            is_provided_before = check_provision(input_str, used_letters)
            if is_provided_before == False:
                used_letters.append(input_str)
                input_is_correct = True
            else:
                if repeat_input_counter >= 2:
                    used_letters.sort()
                    add_linebreak()
                    print(show_used_letters(used_letters))

                repeat_input_counter += 1
                message = "You have already used this letter. What is your guess? "

        else:
            message = check

    return input_str, used_letters


def show_used_letters(letters: List[str]) -> None:
    return f"You have used these letters so far: \"{', '.join(letters)}\""


def check_input(input_str: str) -> Union[bool, str]:
    """
    Function check if input provided is correct. If not, returns helper text to 
    make user provide input correctly.

    Args
        input_str: input that is provided by user
    """

    if len(input_str) == 1 and input_str.isalpha():
        return True
    elif len(input_str) != 1:
        if input_str == "":
            return "You need to provide one letter, it can't be empty. What is your guess? "
        return "You need to provide one letter. What is your guess? "
    elif input_str.isalpha() == False:
        return "You need to provide a letter, not number. What is your guess? "


def check_provision(input_str: str, provided_letters: List[str]) -> bool:
    return input_str in provided_letters


def get_mapped_letters(word: str) -> Dict[str, List[int]]:
    """
    Functions returns dictionary of letters and corresponding indices of those 
    letters.

    Args:
        word: provided string
    """

    dictionary = {}
    for index, letter in enumerate(word):
        dict_mem = dictionary.get(letter, None)
        if dict_mem is not None:
            dictionary[letter].append(index)
        else:
            dictionary[letter] = [index]

    return dictionary


def get_masked_word(word: str) -> List[str]:
    """
    Function returns masked letters of word in a list format. Masking is 
    replacement of letters with underscores.

    Args: 
        word: provided string
    """

    return ["_" for _ in word]


def update_masked_word(masked_word: List[int],
                       letter: str, occurences: List[int]) -> List[str]:
    """
    Function replaces underscores with letter that is found in the masked list of 
    letter and return updated word.

    Args:
        masked_word: list of underscores (or already guessed letters in some 
            cases) that represents word user is looking for
        letter: letter (string) that is guessed correctly by user
        occurences: indice of guessed letter in the word
    """

    if len(occurences) == 0 or letter == "":
        return masked_word

    word = [*masked_word]
    for index in occurences:
        word[index] = letter
    return word


def get_pretty_masked_word(masked_word: List[str]) -> str:
    """
    Function returns string version of masked word by adding a space between 
    each letter.

    Args:
        masked_word: list of letters (or already guessed letters in some 
            cases) that represent word user is looking for
    """

    return " ".join(masked_word)


def guess_word() -> None:
    rand_word = get_random_word(WORDLIST["easy"])
    chances = 6
    hidden_word = get_masked_word(rand_word)
    mapped_letters = get_mapped_letters(rand_word)
    provided_letters = []

    length = len(rand_word)
    print(f"Word contains {length} letters. Let's find them!")
    print(get_pretty_masked_word(hidden_word))
    add_linebreak()

    guessed_letter, provided_letters = get_guessed_letter(
        provided_letters, first_time=True)

    occurrences = get_guess_occurrences(guessed_letter, mapped_letters)
    status = get_guess_status(occurrences)

    if status:
        hidden_word = update_masked_word(
            hidden_word, guessed_letter, occurrences)
    else:
        chances -= 1
        print(f"\nYou missed. You have {chances} chances left.\n")

    print("")
    emotion = get_emotion(status)
    message = get_letter_message(status, guessed_letter)
    print(f"{emotion} {message}")

    # two line breaks
    add_linebreak(quantity=2)

    print(get_pretty_masked_word(hidden_word))
    add_linebreak()

    while "_" in hidden_word:
        guessed_letter, provided_letters = get_guessed_letter(provided_letters)
        occurrences = get_guess_occurrences(guessed_letter, mapped_letters)
        status = get_guess_status(occurrences)

        if status:
            hidden_word = update_masked_word(
                hidden_word, guessed_letter, occurrences)

            if "_" not in hidden_word:
                print(
                    f'\nAaaand "{guessed_letter}" is last letter. Wow, congrats, ingenious! You found the word.\n')
                exit()
            message = get_letter_message(status, guessed_letter)

        else:
            chances -= 1
            message = get_letter_message(status, guessed_letter)

            if chances <= 0:
                print(
                    f'\nYou couldn\'t find the word succesfully. The word was "{rand_word}".\n')
                exit()
            print(f"\nYou missed. You have {chances} chances left.")

        print("")
        emotion = get_emotion(status)
        print(f"{emotion} {message}")

        # two line breaks
        add_linebreak(quantity=2)

        print(get_pretty_masked_word(hidden_word))
        add_linebreak()

    return None


if __name__ == "__main__":
    print("Module contains helper functions that are related to words for hangman.")
