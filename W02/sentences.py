# Import Random Library
import random


def main():
    quantity = 1
    tense = "past"
    print(make_sentence(quantity, tense))

    quantity = 1
    tense = "present"
    print(make_sentence(quantity, tense))

    quantity = 1
    tense = "future"
    print(make_sentence(quantity, tense))

    quantity = 2
    tense = "past"
    print(make_sentence(quantity, tense))

    quantity = 2
    tense = "present"
    print(make_sentence(quantity, tense))

    quantity = 2
    tense = "future"
    print(make_sentence(quantity, tense))


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = [
            "bird",
            "boy",
            "car",
            "cat",
            "child",
            "dog",
            "girl",
            "man",
            "rabbit",
            "woman",
        ]
    else:
        words = [
            "birds",
            "boys",
            "cars",
            "cats",
            "children",
            "dogs",
            "girls",
            "men",
            "rabbits",
            "women",
        ]
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense.lower() == "past":
        words = [
            "drank",
            "ate",
            "grew",
            "laughed",
            "thought",
            "ran",
            "slept",
            "talked",
            "walked",
            "wrote",
        ]
    elif tense.lower() == "present":
        if quantity == 1:
            words = [
                "drinks",
                "eats",
                "grows",
                "laughs",
                "thinks",
                "runs",
                "sleeps",
                "talks",
                "walks",
                "writes",
            ]
        else:
            words = [
                "drink",
                "eat",
                "grow",
                "laugh",
                "think",
                "run",
                "sleep",
                "talk",
                "walk",
                "write",
            ]
    elif tense.lower() == "future":
        words = [
            "will drink",
            "will eat",
            "will grow",
            "will laugh",
            "will think",
            "will run",
            "will sleep",
            "will talk",
            "will walk",
            "will write",
        ]
    word = random.choice(words)
    return word


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    words = [
        "about",
        "above",
        "across",
        "after",
        "along",
        "around",
        "at",
        "before",
        "behind",
        "below",
        "beyond",
        "by",
        "despite",
        "except",
        "for",
        "from",
        "in",
        "into",
        "near",
        "of",
        "off",
        "on",
        "onto",
        "out",
        "over",
        "past",
        "to",
        "under",
        "with",
        "without",
    ]
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    # Exceeding the Requirements adding adjective to function
    adjective = get_adjective()

    prepositional_phrase = f"{preposition} {determiner} {adjective} {noun}"
    return prepositional_phrase


# Exceeding the Requirements Section for get adjective
def get_adjective():
    words = [
        "happy",
        "sad",
        "big",
        "small",
        "fast",
        "slow",
        "bright",
        "dark",
        "strong",
        "weak",
        "soft",
        "hard",
        "cold",
        "hot",
        "loud",
        "quiet",
        "easy",
        "difficult",
        "beautiful",
        "ugly",
        "friendly",
        "mean",
        "clean",
        "dirty",
        "short",
        "tall",
        "heavy",
        "light",
        "young",
        "old",
    ]
    word = random.choice(words)
    return word


def get_adverb():
    words = [
        "quickly",
        "slowly",
        "happily",
        "sadly",
        "loudly",
        "quietly",
        "easily",
        "hardly",
        "gently",
        "roughly",
        "carefully",
        "recklessly",
        "softly",
        "firmly",
        "angrily",
        "calmly",
        "brightly",
        "darkly",
        "politely",
        "rudely",
        "cheerfully",
        "gracefully",
        "heavily",
        "lightly",
        "honestly",
        "dishonestly",
        "kindly",
        "boldly",
        "rarely",
        "often",
    ]
    word = random.choice(words)
    return word


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    # Exceeding the Requirements addition
    other_prepositional_phrase = get_prepositional_phrase(quantity)
    adverb = get_adverb()
    sentence = f"{determiner.capitalize()} {noun} {other_prepositional_phrase} {adverb} {verb} {prepositional_phrase}."
    return sentence

if __name__ == '__main__':
    main()
