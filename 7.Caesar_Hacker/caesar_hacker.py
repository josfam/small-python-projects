"""Program that decrypts a message that was encrypted by the Caesar cipher.
Cracking is done by brute force, therefore it is up to the user to read the output
themselves."""

from string import ascii_uppercase

ALPHABET = ascii_uppercase
POSSIBLE_KEYS = [n for n in range(0, len(ALPHABET))]


def main():
    ciphertext = ask_for_ciphertext()

    # decrypt the message using all possible keys
    for key in POSSIBLE_KEYS:
        print(f"Key #{key}: ", end='')
        print(decrypt(ciphertext, key))


def ask_for_ciphertext():
    """Asks the user for the ciphertext."""
    ciphertext = input('Enter the encrypted Caesar cipher message to hack.\n> ')
    return ciphertext


def decrypt(ciphertext, key):
    """Decrypts the given ciphertext using the given key."""
    hacked_output = []

    for char in ciphertext:

        # only encrypt letters
        if char.isalpha():
            alpha_index = ALPHABET.index(char.upper())

            # decrypt according to the current key
            plain_index = ((alpha_index - key) + len(ALPHABET)) % len(ALPHABET)

            # keep the plaintext character
            hacked_output.append(ALPHABET[plain_index])
        else:
            hacked_output.append(char)

    return ''.join(hacked_output)


if __name__ == '__main__':
    main()
