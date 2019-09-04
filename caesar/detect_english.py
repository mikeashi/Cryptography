ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENGLISH_WORDS = []


def get_words():
    dictionary = open('en.txt','r')
    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)
    dictionary.close()


def count_matches(text):
    text = text.upper()
    words = text.split(' ')
    matches = 0
    for word in words:
        if word in ENGLISH_WORDS:
            matches += 1
    return matches


def is_text_english(text):
    matches = count_matches(text)
    if float(matches) / len(text.split(' ')) * 100 >= 80 :
        return True
    return False

