#!/usr/bin/env python3

""""
Program that prints a tessellated tile pattern to a text file for later
viewing.
"""

import sys

DEFAULT_WIDTH, DEFAULT_HEIGHT = 10, 10
MIN_DIMENSIONS = 5
UPPER_HALF = r'/ \_'
LOWER_HALF = r'\_/ '


def main():
    width, height = get_pattern_dimensions(sys.argv)
    print(make_pattern(width, height))


def get_pattern_dimensions(cmd_args):
    """Returns the dimensions of the pattern, based on the state of the
    commandline arguments"""

    # use defaults if no dimensions are given
    if len(cmd_args) == 1:
        return DEFAULT_WIDTH, DEFAULT_HEIGHT

    elif not len(cmd_args) == 3:
        sys.exit("usage: python3 hexgrid.py [<width> <height>]")
    else:
        x_repeat, y_repeat = cmd_args[1], cmd_args[2]

        # accept only numbers
        if not (x_repeat.isnumeric() and y_repeat.isnumeric()):
            sys.exit("width and height must be numbers")

        # limit the length and width
        elif not (int(x_repeat) >= MIN_DIMENSIONS and int(y_repeat) >= MIN_DIMENSIONS):
            sys.exit(f'width and height must each be greater than {MIN_DIMENSIONS}')

        return x_repeat, y_repeat


def make_pattern(x_repeat, y_repeat):
    """Makes the pattern given its length and width"""
    pattern = []

    for y in range(int(y_repeat)):
        # print the upper half of pattern
        for x in range(int(x_repeat)):
            pattern.append(UPPER_HALF)
        pattern.append('\n')

        # print the lower half of pattern
        for x in range(int(x_repeat)):
            pattern.append(LOWER_HALF)
        pattern.append('\n')

    return ''.join(pattern)


if __name__ == '__main__':
    main()
