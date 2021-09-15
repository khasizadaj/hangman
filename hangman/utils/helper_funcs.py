from typing import List, Dict, Optional, Union


def get_guess_occurrences(guessed_letter: Optional[str] = None, mapped_letters: Optional[Dict] = None) -> Union[List[int], str]:
    """
    Function returns occurences (indices) of guessed_letter in the word which 
    already defined in mapped_letters.

    Args:
        guessed_letter: string of letter that is guessed
        mapped_letters: letter and indices of letters in a dictionary 
    """

    if guessed_letter == None:
        return "Guessed letter is required."
    if mapped_letters == None:
        return "Dictionary of mapped letters is required."
    
    if mapped_letters == {}:
        return [-1]

    if guessed_letter in mapped_letters.keys():
        indices = mapped_letters[guessed_letter]
        return indices

    return [-1]


def get_guess_status(occurrences: Optional[List[int]] = None) -> Union[bool, str]:
    """
    Returns status of guessed letter by checking the occurrences of letter.

    Args: 
        occurrences: indices of letters in a word
    """
    if occurrences is None:
        return "Occurences (positions) are required."

    if occurrences == [] or occurrences == [-1]:
        return False
    return True


def get_emotion(status: Optional[bool] = None) -> str:
    """
    Function returns an emotion based on the status of guessed letter. 

    Args:
        status: boolean value indicating correctness of guessed letter
    """
    if status is None:
        return "Status is required."

    if status:
        return "Hooray! We did it."
    return "We'll be successful next time. Cheer up!"


def get_letter_message(status: Optional[bool] = None, guessed_letter: Optional[str] = None) -> str:
    """
    Function returns a string containing message about the guessed letter based 
    on the status of guess.

    Args:
        status: boolean value indicating correctness of guessed letter
        guessed_letter: string of letter that is guessed
    """

    if status is None:
        return "Status is required."
    if guessed_letter is None:
        return "Letter is required."

    if status:
        return f'Letter "{guessed_letter}" is in the word.'
    return f'Letter "{guessed_letter}" is not in the word.'


if __name__ == "__main__":
    print("Module contains general helper functions for hangman.")
