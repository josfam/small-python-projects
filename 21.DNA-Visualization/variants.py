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
        self.colour = {'block': f'[grey30]', 'dna': f'[cadet_blue]', 'split_block_fill': f'[cyan1]'}

        # assign different blocks their colours
        block_colour, split_color = self.colour['block'], self.colour['split_block_fill']
        split_fill = f'{split_color}█{split_color}'
        single_block = f'{block_colour}█   {block_colour}'
        triple_block = f'{block_colour}███ {block_colour}'
        split_block = f'{block_colour}█{block_colour}{split_fill}{block_colour}█ {block_colour}'

        # each {}{}{}{} represents a segment
        self.skeleton = '{}{}{}{}-{}{}{}{}-{}{}{}{}'
        # bias the randomness
        self.edges_and_weights = {single_block: 0.02, triple_block: 10, split_block: 0.3}
        self.tape_edges = tuple(self.edges_and_weights.keys())
        self.tape_weights = tuple(self.edges_and_weights.values())
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

        # colour the dna characters
        dna_letters = self.skeleton.format(*nucleotides)
        coloured_dna = f'{self.colour["dna"]}{dna_letters}{self.colour["dna"]}'
        one_tape = f'{self.get_tape_edge()}{coloured_dna} {self.get_tape_edge()} '
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
        wait_times = tuple(wait_times_and_weights.keys())
        wait_weights = tuple(wait_times_and_weights.values())
        wait_time = random.choices(wait_times, weights=wait_weights)[0]
        return wait_time
