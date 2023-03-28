import re

from .constants import SENTENCE_PATTERN, NON_DECLARATIVE_PATTERN, WORD_PATTERN, NUMBER_PATTERN, \
    ONE_WORD_ABBREVIATIONS, TWO_WORDS_ABBREVIATIONS, THREE_WORDS_ABBREVIATIONS


def count_sentences(text: str):
    new_text = re.sub(SENTENCE_PATTERN, r"||", text)
    amount = len(new_text.split("||"))

    for abbreviation in ONE_WORD_ABBREVIATIONS:
        amount -= text.lower().count(abbreviation)

    for abbreviation in TWO_WORDS_ABBREVIATIONS:
        amount -= text.lower().count(abbreviation) * 2

    for abbreviation in THREE_WORDS_ABBREVIATIONS:
        amount -= text.lower().count(abbreviation) * 3

    return amount if amount >= 0 else 0


def count_non_declarative(text: str):
    text = text + "\0"
    return len(re.findall(NON_DECLARATIVE_PATTERN, text))


def calc_average_sentence_length(text: str):
    words = [word for word in re.findall(WORD_PATTERN, text) if word not in re.findall(NUMBER_PATTERN, text)]
    words_len = sum(len(word) for word in words)
    return words_len / count_sentences(text) if count_sentences(text) != 0 else 0


def calc_average_word_length(text: str):
    words = re.findall(WORD_PATTERN, text)
    words_len_in_characters = sum(len(word) for word in words)
    return words_len_in_characters / len(words) if len(words) != 0 else 0


def calculate_top_k_repeated_n_grams(text: str, k: int = 10, n: int = 4):
    words = re.findall(WORD_PATTERN, text)
    ngrams = [text[i:i + n] for i in range(len(text) - n + 1)]
    dictionary = {}

    for ngram in ngrams:
        if ngram not in dictionary:
            dictionary[ngram] = 1
        else:
            dictionary[ngram] += 1

    if len(dictionary) <= k:
        return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0:k]
