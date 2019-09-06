import argparse
from algorithms.caesar.caesar import caesar_encrypt, caesar_decrypt


def vigenere_encrypt(plain_text, alphabet, key):
    cipher_text = ''
    plain_text = plain_text.upper()
    key = key.upper()
    key_index = 0
    for char in plain_text:
        cipher_text += caesar_encrypt(char, alphabet, alphabet.find(key[key_index]))
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return cipher_text


def vigenere_decrypt(cipher_text, alphabet, key):
    plain_text = ''
    cipher_text = cipher_text.upper()
    key = key.upper()
    key_index = 0

    for char in cipher_text:
        plain_text += caesar_decrypt(char, alphabet, alphabet.find(key[key_index]))
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return plain_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", help="e to encrypt , d to decrypt",
                        default='e', choices=['e', 'd'])
    parser.add_argument("-k", "--key", help="the key is a sequence of letters", default='key')
    parser.add_argument("-a", "--alphabet", default=" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    args = parser.parse_args()
    if args.mode == 'e':
        print(vigenere_encrypt(input('Enter your plain text :'), args.alphabet, args.key))
    elif args.mode == 'd':
        print(vigenere_decrypt(input('Enter your cipher text :'), args.alphabet, args.key))
