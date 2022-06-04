ALL_WORDS = {
    "easy": [
        {"word": "hmm", "hint": "indicating thinking or pondering"},
        {"word": "zen", "hint": "related to one school of Buddhism"},
        {"word": "pox", "hint": "disease"},
        {"word": "fix", "hint": "to repair"},
        {"word": "joy", "hint": "intense happiness"},
        {"word": "jazz", "hint": "music"},
        {"word": "bomb", "hint": "TNT"},
        {"word": "jump", "hint": "to spring"},
        {"word": "cozy", "hint": "comfortable"},
        {"word": "joke", "hint": "amusing stiry"},
        {"word": "jeep", "hint": "vehicle brand"},
        {"word": "exam", "hint": "test"},
        {"word": "jail", "hint": "a place of detention"},
        {"word": "join", "hint": "to connect"},
        {"word": "quit", "hint": "to exit"},
        {"word": "alone", "hint": "lonely"},
        {"word": "juicy", "hint": "full of juice"},
        {"word": "jokey", "hint": "characterized by joking or jokes"},
        {"word": "above", "hint": "at a higher level"},
        {"word": "shine", "hint": "give out a bright light"},
    ],
    "medium": [
        {"word": "python", "hint": "programming language"},
        {"word": "accept", "hint": "answer affirmatively"},
        {"word": "avenue", "hint": "a broad roadway lined with trees"},
        {"word": "attend", "hint": "to be present at"},
        {"word": "battle", "hint": "armed fighting"},
        {"word": "ancient", "hint": "very old"},
        {"word": "captain", "hint": "one who commands, leads, or guides others"},
        {"word": "average", "hint": "Usual or ordinary in kind or character"},
        {"word": "battery", "hint": " A device containing an electric energy"},
        {
            "word": "auction",
            "hint": "a publicly held sale at which goods are sold to the highest bidder",
        },
    ],
    "hard": [
        {"word": "attorney", "hint": "Saul Goodman"},
        {"word": "bathroom", "hint": "a room containing a toilet and sink"},
        {
            "word": "champion",
            "hint": "one that wins first place or first prize in a competition.",
        },
        {"word": "suspicious", "hint": "doubtful"},
        {"word": "category", "hint": "a specifically defined division in a system of classification; a class."},
    ],
}
# ALL_WORDS = {
#     "easy": [
#         "and",
#         "get",
#         "tan",
#         "arm",
#         "art",
#         "ask",
#         "act",
#         "add",
#         "tea",
#         "ago",
#         "fun",
#         "run",
#         "area",
#         "army",
#         "aunt",
#         "away",
#         "about",
#         "above",
#         "actor",
#         "after",
#         "again",
#         "agree",
#         "alone",
#         "along",
#         "angry",
#         "apple",
#         "phone",
#         "water",
#     ],
#     "medium": [
#         "python",
#         "across",
#         "active",
#         "afraid",
#         "amount",
#         "answer",
#         "always",
#         "appear",
#         "around",
#         "arrive",
#         "attack",
#         "autumn",
#         "ability",
#         "absence",
#         "academy",
#         "account",
#         "accused",
#         "achieve",
#         "acquire",
#         "address",
#         "advance",
#         "adverse",
#         "advised",
#         "adviser",
#     ],
#     "hard": ["marvellous", "extraordinary", "tremendous", "suspicious"],
# }

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
