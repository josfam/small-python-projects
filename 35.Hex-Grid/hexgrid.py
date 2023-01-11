#!/usr/bin/env python3

""""Program that shows a tessellated pattern on the terminal"""

import argparse
import sys
import time

DEFAULT_WIDTH = 10
DEFAULT_HEIGHT = None
DEFAULT_UPPER_HALF = r'/ \_'
DEFAULT_LOWER_HALF = r'\_/ '
PAUSE_DURATION = 0.3

parser = argparse.ArgumentParser()
parser.add_argument('-W', '--width', type=int, help='How wide the pattern will be')
parser.add_argument('-H', '--height', type=int, help='How tall the pattern will be')

args = parser.parse_args()

# use the specified width and height, or use the defults otherwise
width = args.width if args.width else DEFAULT_WIDTH
height = args.height if args.height else DEFAULT_HEIGHT


def main():
    # print an infinitely tall pattern if no height was given, 
    # otherwise print a pattern that is height units tall
    if height is None:
        while True:
            try:
                print(get_one_complete_row(width))
                time.sleep(PAUSE_DURATION)
            except KeyboardInterrupt:
                sys.exit('Goodbye')
    else:
        for _ in range(height):
            print(get_one_complete_row(width))
            time.sleep(PAUSE_DURATION)


def get_one_complete_row(width):
    """Returns a row of the upper and lower half of the tesselation"""
    return f'{DEFAULT_UPPER_HALF * width}\n{DEFAULT_LOWER_HALF * width}'


if __name__ == '__main__':
    main()
