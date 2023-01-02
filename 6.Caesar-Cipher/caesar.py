# Program that encrypts and decrypts with the caesar cipher

from string import ascii_uppercase
import sys

ALPHABET = ascii_uppercase
MIN_KEY_LEN = 0
MAX_KEY_LEN = len(ascii_uppercase)
ASCII_UPPER_A = 65


def main():
    mode = ask_encrypt_or_decrypt()
    key = ask_for_key(mode)
    message = ask_for_message(mode)
    transform(mode, key, message)


def ask_encrypt_or_decrypt():
    """Returns whether the user wants to encrypt(e) or decrypt(d)"""

    while True:
        caesar_mode = input("Press 'e' for encryption, and 'd' for decryption\n> ")
        if caesar_mode.lower().startswith('d'):
            return 'decryption'
        elif caesar_mode.lower().startswith('e'):
            return 'encryption'
        else:
            continue


def ask_for_key(mode: str) -> int:
    """Gets, and returns the key to be used for decryption or encryption"""

    # keep asking for a key until a valid key is entered
    while True:
        key = input(f'Enter the {mode} key\n> ')
        if not key.isnumeric():
            continue
        if not MIN_KEY_LEN <= int(key) <= MAX_KEY_LEN:
            continue
        else:
            return int(key)


def ask_for_message(mode):
    """Returns the message that will be encrypted or decrypted"""
    message = input(f'Enter the message to {mode}\n> ')
    return message


def transform(mode: str, key: int, message: str) -> str:
    """Returns a string that is the result of transforming (either by encryption or decryption)
    the message, based on the provided mode"""

    # stores the encoded/decoded characters
    transformed = []

    for char in message:
        # only transform letters
        if char.isalpha():
            alpha_index = ascii_uppercase.index(char.upper())

            # encrypt or decrypt based on provided mode
            if mode == 'encryption':
                cipher_index = (alpha_index + key) % len(ALPHABET)
            else:
                cipher_index = ((alpha_index - key) + len(ALPHABET)) % len(ALPHABET)

            # keep the transformed character
            transformed.append(ALPHABET[cipher_index])

        else:
            transformed.append(char)

    return ''.join(transformed)


if __name__ == '__main__':
    main()
