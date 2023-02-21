import random
import sys
import time
import argparse

WIDTH = 70
PAUSE_DURATION = 0.05

left_width = 20
middle_width = 10

parser = argparse.ArgumentParser()
parser.add_argument('-s','--symbols', type=str, nargs=1, help='Symbols that represent the left, middle, and right section\
     of the tunnel')
args = parser.parse_args()

symbols = args.symbols if args.symbols else None

if symbols:
    chars = symbols[0]
    if ',' not in chars:
        sys.exit('Error. Make sure to separate each of the three symbols with a comma')
    separated = chars.split(',')

    if len(separated) == 2:  # given two symbols, make the last symbol the same as the first
        left_char, middle_char = chars.split(',')
        right_char = left_char
    elif len(separated) > 3: # take the first three symbols if given excess
        left_char, middle_char, right_char = chars.split(',')[0:3]
    else:
        left_char, middle_char, right_char = chars.split(',')
else:
    left_char, middle_char, right_char = ('#', ' ', '#')


while True:
    right_width = WIDTH - left_width - middle_width
    print(f'{left_char * left_width}{middle_char * middle_width}{right_char * right_width}')
    
    try:
        time.sleep(PAUSE_DURATION)
    except(KeyboardInterrupt, EOFError):
        sys.exit('Goodbye!')  # end the program when CTRL-C is pressed
    
    dice_roll = random.randint(1, 6)

    if dice_roll in {1, 2} and left_width > 1:
        left_width = left_width - 1
    elif dice_roll in {5, 6} and (left_width + middle_width) < WIDTH - 1:
        left_width = left_width + 1
    else:
        pass  # don't change the left width
