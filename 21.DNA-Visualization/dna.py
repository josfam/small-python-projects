"""Program that visualizes a DNA double-helix, and other variants if requested"""
import argparse
import rich
import sys
from variants import DNA, BladeRunner2049

parser = argparse.ArgumentParser()
parser.add_argument('--br2049', help='represents DNA as seen in Blade Runner 2049', action='store_true')
args = parser.parse_args()

# show the double-helix by default if no other variant is chosen
if args.br2049:
    dna = BladeRunner2049()
else:
    dna = DNA()

while True:
    try:
        rich.print(dna.get_DNA())
    except KeyboardInterrupt:
        sys.exit('\nGoodbye!')
