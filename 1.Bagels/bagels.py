"""
Bagels is a guessing game in which the user guesses a 3-digit number.

The program prints:
"Pico" for each correct number in the guess that is in the wrong place,
"Fermi" for each correct number in the guess that is the right place,
"Bagels" if none of the digits is correct.
"""

import random
import sys
from textwrap import dedent

MAX_GUESSES = 10


def main():
    """Runs Bagels game"""

    print(show_instructions())
    computer_num = generate_computer_num()
    print(f'Computer_num: {computer_num}')
    guesses_used = 0

    while True:
        if guesses_used == MAX_GUESSES:
            print(dedent(f'''
                         Sorry. You ran out of tries.
                         The number was {computer_num}'''))
            if start_new_game():
                main()
            else:
                sys.exit('Thanks for playing!')

        user_guess = input(f'Guess #{guesses_used + 1}:\n>')

        if user_guess == computer_num:
            print('You got it!')
            if start_new_game():
                main()
            else:
                sys.exit('Thanks for playing!')

        guesses_used += 1

        print(show_hints(computer_num, user_guess))


def show_instructions():
    """Prints game instructions when the game begins"""

    game_instructions = '''
        I am thinking of a 3-digit number. 
        Guess what it is.
        
        You have 10 guesses to get it right.

        Some rules:

        When I say:     It means that:
        Pico            A digit in your guess is correct, 
                        but in the wrong position

        Fermi           A digit in your guess is correct,
                        and also in the correct location

        Bagels          All digits in your guess are incorrect
        '''
    return dedent(game_instructions)


def generate_computer_num():
    """
    Generates and returns a 3-digit number
    (with leading zeroes if necessary)
    """
    # Generate zeroes as well.
    return str(random.randint(0, 999)).zfill(3)


def show_hints(computer_num, user_guess):
    """
    Returns hints including "Fermi", "Pico", and "Bagels",
    as highlighted by the game instructions
    """
    # store 'Pico', 'Fermi', and 'Bagels' hints
    hints = []

    # compare digits in user guess, to the computer number
    for i, user_num in enumerate(user_guess):
        if user_num == computer_num[i]:
            hints.append('Fermi')
        else:
            if user_num in computer_num:
                hints.append('Pico')

    if len(hints) > 0:
        return ' '.join(hints)

    return 'Bagels'


def start_new_game():
    """
    Prompts the user to play another game.
    """
    play_again = input('Do you want to play again? (yes or no)\n>')

    if play_again.lower() in ('yes', 'y'):
        return True

    return False


if __name__ == '__main__':
    main()
