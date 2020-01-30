import difflib

from difflib import get_close_matches


def closeMatches(patterns, word):
    print(get_close_matches(word, patterns))


# Driver program
if __name__ == "__main__":
    word = 'ΝΕΟΛΑΙΑ'
    patterns = ['ΔΟΥΛΕΙΑ', 'ηταν', 'αδιανόητα', 'ΔΟΥΛΕΥΟΥΜΕ']
    closeMatches(patterns, word)
