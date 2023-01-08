import random
import time

PAUSE_DURATION = 0.1

# legal pairings of nucleotides
NUCLEOTIDE_PAIRS = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


class DNA:
    """DNA is represented as the standard double-helix"""

    def __init__(self):
        self.skeleton = """      ~
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

    def get_sequence(self) -> list:
        """Returns the DNA skeleton as a list"""
        return self.skeleton.splitlines()

    def get_nucleotide_pairs(self):
        l_nucleotide = random.choice(list(NUCLEOTIDE_PAIRS.keys()))
        r_nucleotide = NUCLEOTIDE_PAIRS[l_nucleotide]
        return (l_nucleotide, r_nucleotide)

    def get_DNA(self):
        """Prints the DNA representation, as a standard double-helix"""
        while True:
            for row in self.get_sequence():
                l_nucleotide, r_nucleotide = self.get_nucleotide_pairs()
                time.sleep(PAUSE_DURATION)
                print(row.format(l_nucleotide, r_nucleotide))


class BladeRunner2049(DNA):
    """DNA is represented as text on scrolling tapes to mimic the DNA viewing device--displaying the 'satcrystal backup'
    in RAW format--as seen in the 2017 film, Blade Runner 2049. 'Satcrystal backup' is jargon from the film."""

    def __init__(self) -> None:
        # each {}{}{}{} represents a segment
        self.skeleton = '{}{}{}{}-{}{}{}{}-{}{}{}{}'
        # bias the randomness to favor ███, then █ █, then █
        self.edges_and_weights = {'███ ': 10, '█ █ ': 0.2, '█   ': 0.02}
        self.tape_edges = list(self.edges_and_weights.keys())
        self.tape_weights = list(self.edges_and_weights.values())
        self.SEGMENT_COUNT = len(self.skeleton.split('-'))
        self.NUCLEOTIDES_PER_SEGMENT = 4
        self.TAPES_COUNT = 3

    def get_tape_edge(self) -> str:
        """Returns a random edge, from a collection of edges. Edges are merely decorative
        and are numerically weighted, such that the they are not chosen purely at random"""
        return random.choices(self.tape_edges, weights=self.tape_weights)[0]

    def get_row_of_one_tape(self) -> str:
        """Returns one row of one tape. A row of tape consists of an edge, the dna, then another edge, for example:
        ███ GCTA-ATAT-GCCG █ █"""
        nucleotides = []
        nucleotide_num = 0

        while nucleotide_num < (self.SEGMENT_COUNT * self.NUCLEOTIDES_PER_SEGMENT):
            l_nucleotide, r_nucleotide = self.get_nucleotide_pairs()
            nucleotides.extend((l_nucleotide, r_nucleotide))
            nucleotide_num += 1

        one_tape = self.get_tape_edge() + self.skeleton.format(*nucleotides) + ' ' + self.get_tape_edge() + ' '
        return one_tape

    def get_row_of_all_tapes(self) -> str:
        """Returns a row of all tapes"""
        all_tapes = ''
        tape_num = 0
        while tape_num < self.TAPES_COUNT:
            all_tapes += self.get_row_of_one_tape()
            tape_num += 1
        return all_tapes

    def get_DNA(self):
        """Returns the DNA representation, borrowing from the 2017 film, Blade Runner 2049."""
        time.sleep(self.get_scroll_jitter_time())
        return self.get_row_of_all_tapes()

    def get_scroll_jitter_time(self):
        """Returns how much waiting will occur between vertical scrolls of the tapes.'"""
        # bias the randomness to favor shorter wait time
        wait_times_and_weights = {0.08: 10, 0.4: 0.8}
        wait_times = list(wait_times_and_weights.keys())
        wait_weights = list(wait_times_and_weights.values())
        wait_time = random.choices(wait_times, weights=wait_weights)[0]
        return wait_time
