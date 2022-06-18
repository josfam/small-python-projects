"""Program that shows the provided message based on the bitmap image used"""

import sys
from bitmap_patterns import patterns

image = patterns.WORLD_MAP

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
