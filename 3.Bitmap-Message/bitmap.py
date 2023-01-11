"""Program that shows the provided message based on the bitmap image used"""

import argparse
import sys
from patterns import patterns

parser = argparse.ArgumentParser()
parser.add_argument('--octocat', action='store_true', help='Shows the message in the form of an octocat')
args = parser.parse_args()

# use a world map by default, if no option is chosen
image = patterns.octo_cat if args.octocat else patterns.world_map

print('Enter the message to display with the bitmap.')
message = input('> ')

if message == '':
    sys.exit('Cannot have an empty message.')

# Fetch all lines in the image
image_lines = image.splitlines()

# Iterate through each line
for line in image_lines:
    # Loop through each character in that line
    for i, char in enumerate(line):
        if char == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()
