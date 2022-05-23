ALL_WORDS = {
    "easy": [
        "and",
        "get",
        "tan",
        "arm",
        "art",
        "ask",
        "act",
        "add",
        "tea",
        "ago",
        "fun",
        "run",
        "area",
        "army",
        "aunt",
        "away",
        "about",
        "above",
        "actor",
        "after",
        "again",
        "agree",
        "alone",
        "along",
        "angry",
        "apple",
        "phone",
        "water",
    ],
    "medium": [
        "python",
        "across",
        "active",
        "afraid",
        "amount",
        "answer",
        "always",
        "appear",
        "around",
        "arrive",
        "attack",
        "autumn",
        "ability",
        "absence",
        "academy",
        "account",
        "accused",
        "achieve",
        "acquire",
        "address",
        "advance",
        "adverse",
        "advised",
        "adviser",
    ],
    "hard": ["marvellous", "extraordinary", "tremendous", "suspicious"],
}

DIFFICULTIES = {
    0: "all",
    1: "easy",
    2: "medium",
    3: "hard",
}


def get_wordlist(difficulty_level: str = "all"):
    if difficulty_level == "all":
        return get_all_words()

    return ALL_WORDS[difficulty_level]


def get_all_words():
    all_words = []
    for words in ALL_WORDS.values():
        all_words.extend(words)

    return all_words
