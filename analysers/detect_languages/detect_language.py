import os


WORDS = []


def load_words(language):
    dictionary = open(os.path.join(os.path.dirname(__file__), language+'.txt'), 'r', encoding="utf8")
    for word in dictionary.read().split('\n'):
        WORDS.append(word)
    dictionary.close()


def count_matches(text):
    text = text.lower()
    words = text.split(' ')
    matches = 0
    for word in words:
        if word in WORDS:
            matches += 1
    return matches


def is_text(language, text):
    if language in ['en', 'ar']:
        load_words(language)
        matches = count_matches(text)
        if float(matches) / len(text.split(' ')) * 100 >= 80:
            return True
        return False
