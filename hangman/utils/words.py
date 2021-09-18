from typing import List, Dict, Union
from random import randint
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


def get_guess(first_time: bool = False) -> str:
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

    input_is_correct = False
    while input_is_correct != True:
        letter = input(message)

        check = check_input(letter)
        if check == True:
            input_is_correct = True
        else:
            message = check

    return letter


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


if __name__ == "__main__":
    print("Module contains helper functions that are related to words for hangman.")
