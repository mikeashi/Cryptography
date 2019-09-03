import matplotlib.pylab as plt

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def frequency_analysis(text):
    text = text.upper()

    letter_frequency = {}

    for letter in ALPHABET:
        letter_frequency[letter] = 0

    for letter in text:
        if letter in ALPHABET:
            letter_frequency[letter] += 1

    return letter_frequency


def plot_distribution(letter_frequency):
    centers = range(len(ALPHABET))
    plt.bar(centers, letter_frequency.values(), align='center')
    plt.xticks(centers, letter_frequency.keys())
    plt.show()

