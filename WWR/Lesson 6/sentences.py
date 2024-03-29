import random
words = ["boy", "girl", "cat", "dog", "bird", "house"]
prepositions= ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    cap_word = word.capitalize()
    return cap_word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
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
        words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    words = random.choice(words)
    cap_word = words.capitalize()
    return cap_word

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
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif quantity > 1 and tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    words = random.choice(words)
    cap_word = words.capitalize()
    return cap_word

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
    prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    prepositions = random.choice(prepositions)
    cap_word = prepositions.capitalize()
    return cap_word

def get_prepositional_phrase(quantity):
    if quantity == 1:
        preposition = get_preposition() 
        determiner = get_determiner(1)
        noun =  get_noun(1)
    elif quantity > 1:
        preposition = get_preposition() 
        determiner = get_determiner(2)
        noun =  get_noun(2)

    phrase = (f"{preposition} {determiner} {noun}")
    return phrase
def get_adjective():
    words = ["good", "bad", "nasty", "funny", "dangerous"]
    word = random.choice(words)
    cap_word = word.capitalize()
    return cap_word
def main():
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "past"), get_prepositional_phrase(1), get_prepositional_phrase(1))
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "present"), get_prepositional_phrase(1), get_prepositional_phrase(1))
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "future"), get_prepositional_phrase(1), get_prepositional_phrase(1))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "past"), get_prepositional_phrase(2), get_prepositional_phrase(2))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "present"), get_prepositional_phrase(2), get_prepositional_phrase(2))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "future"), get_prepositional_phrase(2), get_prepositional_phrase(2))
if __name__ == ("__main__"):
    main()