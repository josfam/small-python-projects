"""Program that visualizes a DNA double-helix"""

import random
import time
import sys

PAUSE_DURATION = 0.15

# template for a dna double helix
dna_skeleton = """      ~
    {}~~~~{}
  {}~~~~~~~~{}
{}~~~~~~~~~~{}
{}~~~~~~~~~~{}
{}~~~~~~~~{}
  {}~~~~{}
    ~
  {}~~~~{}
{}~~~~~~~~{}
{}~~~~~~~~~~{}
{}~~~~~~~~~~{}
  {}~~~~~~~~{}
    {}~~~~{}
"""

# legal pairings of nucleotides
NUCLEOTIDE_PAIRS = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

print('Press CTRL + C to stop the visualization\n')
time.sleep(PAUSE_DURATION * 10)

dna_sequence = dna_skeleton.splitlines()

while True:
    for row in dna_sequence:
        try:
            left_nucleotide = random.choice(list(NUCLEOTIDE_PAIRS.keys()))
            right_nucleotide = NUCLEOTIDE_PAIRS[left_nucleotide]
            time.sleep(PAUSE_DURATION)
            print(row.format(left_nucleotide, right_nucleotide))
        except KeyboardInterrupt:
            sys.exit('\nGoodbye!')
