import argparse


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
            print('Using key %s: \n\t\t %s\n' % (k, caesar_decrypt(c_text, args.alphabet, k)))
