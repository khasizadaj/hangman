from typing import List, Dict

from utils.words import (WORDLIST, get_guess, check_input, get_masked_word, get_random_word,
                         update_masked_word, get_pretty_masked_word, get_mapped_letters)
from utils.helper_funcs import (get_guess_occurrences, get_guess_status,
                                get_emotion, get_letter_message)

RAND_WORD = get_random_word(WORDLIST["easy"])
CHANCES = 6
HIDDEN_WORD = get_masked_word(RAND_WORD)
LETTERS = get_mapped_letters(RAND_WORD)


length = len(RAND_WORD)
print(f"Word contains {length} letters. Let's find them!")
print(get_pretty_masked_word(HIDDEN_WORD))
print("")

guessed_letter = get_guess(first_time=True)

occurrences = get_guess_occurrences(guessed_letter, LETTERS)
status = get_guess_status(occurrences)

if status:
    HIDDEN_WORD = update_masked_word(HIDDEN_WORD, guessed_letter, occurrences)
else:
    CHANCES -= 1
    print(f"\nYou missed. You have {CHANCES} chances left.\n")


print("")
emotion = get_emotion(status)
message = get_letter_message(status, guessed_letter)
print(f"{emotion} {message}")
print("\n")  # two line breaks
print(get_pretty_masked_word(HIDDEN_WORD))
print("")

while "_" in HIDDEN_WORD:
    guessed_letter = get_guess()
    occurrences = get_guess_occurrences(guessed_letter, LETTERS)
    status = get_guess_status(occurrences)

    if status:
        HIDDEN_WORD = update_masked_word(
            HIDDEN_WORD, guessed_letter, occurrences)

        if "_" not in HIDDEN_WORD:
            print(
                f'\nAaaand "{guessed_letter}" is last letter. Wow, congrats, ingenious! You found the word.\n')
            exit()
        message = get_letter_message(status, guessed_letter)

    else:
        CHANCES -= 1
        message = get_letter_message(status, guessed_letter)

        if CHANCES <= 0:
            print(
                f'\nYou couldn\'t find the word succesfully. The word was "{RAND_WORD}".\n')
            exit()
        print(f"\nYou missed. You have {CHANCES} chances left.")

    print("")
    emotion = get_emotion(status)
    print(f"{emotion} {message}")
    print("\n")  # two line breaks
    print(get_pretty_masked_word(HIDDEN_WORD))
    print("")
