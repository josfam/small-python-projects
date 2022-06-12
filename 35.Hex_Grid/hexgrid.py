#!/usr/bin/env python3

""""
Program that prints a tessellated tile pattern to a text file for later
viewing.
"""

import sys

DEFAULT_WIDTH, DEFAULT_HEIGHT = 10, 10
MIN_DIMENSIONS = 5
X_REPEAT, Y_REPEAT = None, None

# use defaults if no dimensions are given
if len(sys.argv) == 1:
    X_REPEAT, Y_REPEAT = DEFAULT_WIDTH, DEFAULT_HEIGHT

elif not len(sys.argv) == 3:
    sys.exit("usage: python3 hexgrid.py [<width> <height>]")
else:
    X_REPEAT, Y_REPEAT = sys.argv[1], sys.argv[2]

    # accept only numbers
    if not (X_REPEAT.isnumeric() and Y_REPEAT.isnumeric()):
        sys.exit("width and height must be numbers")

    # limit the length and width
    elif not (int(X_REPEAT) >= MIN_DIMENSIONS and int(Y_REPEAT) >= MIN_DIMENSIONS):
        sys.exit(f'Width and height must each be greater than {MIN_DIMENSIONS}')

upper_half = r'/ \_'
lower_half = r'\_/ '

X_REPEAT, Y_REPEAT = int(X_REPEAT), int(Y_REPEAT)

for y in range(Y_REPEAT):
    # print the upper half of pattern
    for x in range(X_REPEAT):
        print(upper_half, end='')
    print()

    # print the lower half of pattern
    for x in range(X_REPEAT):
        print(lower_half, end='')
    print()
