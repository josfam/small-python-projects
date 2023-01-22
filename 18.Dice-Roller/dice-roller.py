"""Program that simulates a dice roll in the spirit of tabletop role-playing
games
"""
from textwrap import dedent
from collections import namedtuple, deque
from typing import Union
import sys
import random
import time
from rich import print as rprint
import argparse

ARROW = '\u2192'
PAUSE_DURATION = 0.05
DICE_IN_HISTORY = 10  # maximum dice to show in rolled history

COLORS = {
    'running_total': 'deep_sky_blue1',
    'final_total': 'green',
    'plus_extra': 'green3',
    'minus_extra': 'deep_pink2',
}

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--instant', help='displays the dice rolls instantly, instead of showing sucessive rolls', action='store_true'
)

args = parser.parse_args()

Dice = namedtuple('Dice', ['num_of_dice', 'sides', 'score_modifier'], defaults=[None])
pause_duration = 0 if args.instant else PAUSE_DURATION
dice_history = deque(maxlen=DICE_IN_HISTORY)


def main():
    print(show_instructions())

    while True:
        dice_history.clear()
        try:
            dice = input('Enter dice to roll (q to quit)> ')
        except KeyboardInterrupt:
            sys.exit('\nGoodbye!')
        else:
            if dice.lower() == 'q':
                sys.exit('\nGoodbye!')
            parts = extract_dice_parts(dice)
            if isinstance(parts, Dice):
                if not parts.score_modifier is None:
                    roll_dice(parts.num_of_dice, parts.sides, parts.score_modifier)
                else:
                    roll_dice(parts.num_of_dice, parts.sides)
            else:
                print(parts)  # The 'error' message
                continue


def show_instructions():
    """Returns the instructions for the game"""

    instructions = dedent(
        """
    Enter the kind and number of dice to roll, in this format:
    The number of dice, 'd', the number of sides that the dice have.

    4d7 rolls four 7-sided dice
    3d8+2 rolls three 8-sided dice, and then adds 2 to the dice total
    6d30-1 rolls six 30-sided dice, and then subtracts 1 from the dice total
    Entering 'Q' quits the program 
    """
    )
    return instructions


def extract_dice_parts(dice: str) -> Union[Dice, str]:
    """Returns: the number of dice, the sides of a single die, and the number of points
    (if available) to add or subtract (as a namedtuple, Dice) given a string representing those
    dice details.
    Returns error information, if the input is in an invalid format

    an input of '4d7' will return Dice(num_of_dice=4, sides=7, score_modifier=None)
    an input of '3d8+2' will return Dice(num_of_dice=3, sides=8, score_modifier=2)
    an input of '6d30-1' will return Dice(num_of_dice=6, sides=30, score_modifier=-1)
    """
    num_of_dice, sides, score_modifier = None, None, None

    if not 'd' in dice:
        return "You are missing a 'd'"
    d_index = dice.find('d')

    try:
        num_of_dice = int(dice[:d_index])
    except ValueError:
        return "You provided an incorrect format for the number of dice."

    # check if there is a '+' or '-'
    modifier_index = dice.find('+')
    if modifier_index == -1:
        modifier_index = dice.find('-')

    if modifier_index == -1:
        # sides are everything after the 'd'
        try:
            sides = int(dice[d_index + 1 :])
        except ValueError:
            return 'You provided an incorrect format for the number of sides.'
    else:
        # sides are between the 'd' and the '-' or '+'
        try:
            sides = int(dice[d_index + 1 : modifier_index])
        except ValueError:
            return 'You provided an incorrect format for the number of sides.'

        # get score to add or subtract
        try:
            score_modifier = int(dice[modifier_index:])
        except ValueError:
            return 'You provided an incorrect format for the number of points to add or subtract.'

    return Dice(num_of_dice, sides, score_modifier)


def roll_dice(num_dice: int, sides: int, extra_points=None):
    """Simulates a dice roll of a total of 'num_dice' dice, each with 'sides' sides, and
    'extra_points' points added or subtracted from the resulting dice total
    """
    total = 0
    total_color = COLORS['running_total']

    for die_count in range(1, num_dice + 1):
        die = random.randint(1, sides)
        total += die
        dice_history.appendleft(str(die))
        history = ", ".join(dice_history)
        history_formatted = f'[grey70]{history}[/grey70]'

        if die_count == num_dice:
            total_color = COLORS['final_total']

            if extra_points:
                total += extra_points
                total_formatted = f'[{total_color}]{str(total).rjust(5)}[/{total_color}]'
                sign = ''

                if extra_points < 0:
                    extra_color = COLORS['minus_extra']
                else:
                    extra_color = COLORS['plus_extra']
                    sign = '+'

                rprint(
                    "".join(
                        [
                            total_formatted,
                            ' ',
                            f'{ARROW} ',
                            history_formatted,
                            f' ]',
                            f' [{extra_color}]({sign}{extra_points})',
                        ]
                    ),
                    flush=True,
                )
            else:
                total_formatted = f'[{total_color}]{str(total).rjust(5)}[/{total_color}]'
                rprint("".join([total_formatted, ' ', f'{ARROW} ', history_formatted, f' ]']), flush=True)
        else:
            total_formatted = f'[{total_color}]{str(total).rjust(5)}[/{total_color}]'
            rprint("".join([total_formatted, ' ', f'{ARROW} ', history_formatted, f' ]']), flush=True)

        time.sleep(pause_duration)


if __name__ == '__main__':
    main()
