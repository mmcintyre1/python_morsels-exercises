from collections import defaultdict, Counter
import re
from string import punctuation
from typing import Dict


def count_words_1(words: str) -> Dict[str, int]:
    """
    First solution, just splitting the string and
    iterating to count
    :param words:
    :return:
    """
    counts = {}
    for word in words.split(" "):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def count_words_2(words: str) -> Dict[str, int]:
    """
    Second solution, takes case into account.
    :param words:
    :return:
    """
    counts = {}
    for word in words.split(" "):
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def count_words_3(words: str) -> Dict[str, int]:
    """
    Third solution, with a default dict to simplify things.
    :param words:
    :return:
    """
    counts = defaultdict(int)
    for word in words:
        counts[word.lower()] += 1
    return counts


def count_words_4(words: str) -> Dict[str, int]:
    """
    Fourth solution, ignoring punctuation.
    :param words:
    :return:
    """
    counts = defaultdict(int)
    # replaces every non-word or digit character with an empty string.
    for word in re.sub(r'[^\w\d\s]\s+', '', words).split(" "):
        counts[word.lower()] += 1
    return counts


def count_words_5(words: str) -> Dict[str, int]:
    """Return the number of times each word occurs in the string."""
    return Counter(re.findall(r"\b[\w'-]+\b", words.lower()))


def count_words(words: str) -> Dict[str, int]:
    """
    Final solution, with Counter
    :param words:
    :return:
    """
    return Counter([word.lower().strip(punctuation + "¿") for word in re.split(r"\s+", words)])


if __name__ == '__main__':
    print(count_words("¿Te  gusta Python?"))
