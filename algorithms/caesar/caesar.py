import argparse
from langdetect import detect_langs, DetectorFactory
DetectorFactory.seed = 0

# a simple caesar cipher encrypter/decrypter and brute force attack script


def caesar_encrypt(plain_text, alphabet, key):
    cipher_text = ''
    plain_text = plain_text.upper()
    for char in plain_text:
        if char in alphabet:
            index = alphabet.find(char)
            shifted_index = (index + key) % len(alphabet)
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += char
    return cipher_text


def caesar_decrypt(cipher_text, alphabet, key):
    plain_text = ''
    cipher_text = cipher_text.upper()
    for char in cipher_text:
        if char in alphabet:
            index = alphabet.find(char)
            shifted_index = (index - key) % len(alphabet)
            plain_text += alphabet[shifted_index]
        else:
            plain_text += char
    return plain_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", help="e to encrypt , d to decrypt , b to brute force",
                        default='e', choices=['e', 'd', 'b'])
    parser.add_argument("-k", "--key", help="the key is a number 0 < k < length of the alphabet",
                        type=int, default=3)
    parser.add_argument("-a", "--alphabet", default=" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    parser.add_argument("-l", "--language", help="the language to be used for brute force",
                        default='en',
                        choices=['af', 'ar', 'bg', 'bn', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'fa',
                                 'fi', 'fr', 'gu', 'he', 'hi', 'hr', 'hu', 'id', 'it', 'ja', 'kn', 'ko', 'lt', 'lv',
                                 'mk', 'ml', 'mr', 'ne', 'nl', 'no', 'pa', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'so',
                                 'sq', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi', 'zh-cn', 'zh-tw'])
    args = parser.parse_args()

    if args.mode == 'e':
        if args.key > len(args.alphabet):
            print("[-] the key should be in range [0,{}]".format(len(args.alphabet)))
        else:
            print(caesar_encrypt(input('Enter your plain text :'), args.alphabet, args.key))
    elif args.mode == 'd':
        if args.key > len(args.alphabet):
            print("[-] the key should be in range [0,{}".format(len(args.alphabet)))
        else:
            print(caesar_decrypt(input('Enter your cipher text :'), args.alphabet, args.key))
    elif args.mode == 'b':
        c_text = input('Enter your cipher text :')
        for k in range(len(args.alphabet)):
            de_text = caesar_decrypt(c_text, args.alphabet, k)
            lang = detect_langs(de_text)[0]
            if lang.lang == args.language and lang.prob >= 0.8:
                print('using key %s' % k)
                print(de_text)
