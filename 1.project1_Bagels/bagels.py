"""
Bagels is a guessing game in which the user guesses a 3-digit number.

The program prints:
"Pico" for each correct number in the guess that is in the wrong place,
"Fermi" for each correct number in the guess that is the right place,
"Bagels" if none of the digits is correct.
"""

import random
from textwrap import dedent

MAX_GUESSES = 10

# Accept leading zeroes as well.
computer_num = str(random.randint(0, 999)).zfill(3)

print(dedent('''
    I am thinking of a number. 
    You have 10 guesses to get it.
    '''))

for guess in range(MAX_GUESSES):
    user_num = input(f'Guess #{guess}:\n>')
