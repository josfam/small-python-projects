from collections import namedtuple, deque
import argparse
import random
import time
import sys
from typing import Dict, Tuple, List
from copy import copy, deepcopy

Point = namedtuple('Point', ['x', 'y'])
Dims = namedtuple('Dims', ['rows', 'cols'])
CellStats = namedtuple('CellStats', ['location', 'status'])

ALIVE = '\u25A0'  # represents '■'
DEAD = '-'
DEFAULT_GRID_SIZE = 10
CELL_ITERATION_HISTORY_SIZE = 3  # length of 3 makes sure to catch similar patterns that are one iteration apart


class CellGrid:
    """Represents a grid of dead and ALIVE cells"""

    def __init__(self, size=None, cell_arrangement: Dict[Tuple[int, int], str] = {}) -> None:
        self._size = size or DEFAULT_GRID_SIZE
        if cell_arrangement:
            self._cells = cell_arrangement
        else:
            self._cells = self._create_cell_arrangement()

    def _create_cell_arrangement(self) -> Dict[Tuple[int, int], str]:
        """Returns a random arrangement of dead and ALIVE cells"""
        cell_arrangement = {}
        for y in range(self._size):
            for x in range(self._size):
                cell_arrangement[(x, y)] = random.choice([DEAD, ALIVE])
        return cell_arrangement

    @property
    def cells(self) -> Dict[Tuple[int, int], str]:
        """Returns the cell arrangement, that represents dead and ALIVE cells in the grid"""
        return self._cells

    @property
    def grid_size(self) -> int:
        """Returns the dimensions of the (square) cell grid"""
        return self._size

    def __str__(self) -> str:
        """Returns the string representation of a grid"""
        return str(self.cells)


class ConwaysGameOfLife:
    """Represents a game of Conway's game of life based on the following rules:
    - Living cells with 2 or 3 neighbours stay ALIVE in the next step of the simulation
    - Dead cells with exactly 3 neighbours become ALIVE in the next ste of the simulation
    - Any other cell dies or stays dead in the next step of the simulation
    """

    def __init__(self, CellGrid: CellGrid) -> None:
        self._grid = CellGrid
        self._iteration_history = deque(maxlen=CELL_ITERATION_HISTORY_SIZE)
        self._total_iterations = 0

    @property
    def first_generation(self):
        """Returns the very first generation of cells in the game"""
        return self._grid.cells

    @property
    def iteration_history(self):
        """Returns the most recent iterations"""
        return self._iteration_history

    @property
    def total_iterations(self):
        """Returns how many iterations of the original generations were made before the game stopped"""
        return self._total_iterations

    def count_living_neighbours(self, cell_grid: Dict[Tuple[int, int], str]) -> List[int]:
        """Returns a list whose elements represent the number of living cells that surround
        that location in the cell grid
        """
        grid = copy(cell_grid)
        living_neighbour_count = []

        for location, _ in cell_grid.items():
            here = Point(*location)  # the current location
            top = Point(here.x, here.y - 1)
            right = Point(here.x + 1, here.y)
            bottom = Point(here.x, here.y + 1)
            left = Point(here.x - 1, here.y)
            top_left = Point(top.x - 1, top.y)
            top_right = Point(top.x + 1, top.y)
            bottom_right = Point(bottom.x - 1, bottom.y)
            bottom_left = Point(bottom.x + 1, bottom.y)

            living_neighbours = 0

            if grid.get(top) == ALIVE:
                living_neighbours += 1
            if grid.get(right) == ALIVE:
                living_neighbours += 1
            if grid.get(bottom) == ALIVE:
                living_neighbours += 1
            if grid.get(left) == ALIVE:
                living_neighbours += 1
            if grid.get(top_left) == ALIVE:
                living_neighbours += 1
            if grid.get(top_right) == ALIVE:
                living_neighbours += 1
            if grid.get(bottom_right) == ALIVE:
                living_neighbours += 1
            if grid.get(bottom_left) == ALIVE:
                living_neighbours += 1

            living_neighbour_count.append(living_neighbours)

        return living_neighbour_count

    def get_next_iteration(
        self, current_gen: Dict[Tuple[int, int], str], alive_neighbours: List[int]
    ) -> Dict[Tuple[int, int], str]:
        """Returns the next iteration of the grid of cells, based on the rules of the game"""
        previous_gen = deepcopy(current_gen)
        next_gen: Dict[Tuple[int, int], str] = {}

        cell_info = (CellStats(location, status) for location, status in previous_gen.items())

        for cell_stats in zip(cell_info, alive_neighbours):
            location = cell_stats[0].location
            status = cell_stats[0].status
            living_neighbours = cell_stats[1]

            if status == ALIVE and living_neighbours in [2, 3]:
                next_gen[(location)] = ALIVE
            elif status == DEAD and living_neighbours == 3:
                next_gen[(location)] = ALIVE
            else:
                next_gen[(location)] = DEAD

        return next_gen

    def run_game_of_life(self, iterations: int):
        """Runs Conway's game of life `iterations` times"""
        current_gen = deepcopy(self._grid)

        # the original/first generation will not count towards the iteration count
        # but it is added to history to account for non-changing patterns
        self._iteration_history.append(current_gen.cells)

        yield current_gen.cells

        for _ in range(iterations):
            cells = current_gen.cells
            living_neighbour_count = self.count_living_neighbours(cells)
            next_iteration = self.get_next_iteration(cells, living_neighbour_count)
            current_gen = CellGrid(cell_arrangement=next_iteration)

            if next_iteration in self._iteration_history:
                print('\033c', end='')  # clear the terminal
                print('Game over due to a repeated pattern!')
                break
            else:
                yield next_iteration
                self._total_iterations += 1

            self._iteration_history.append(next_iteration)


def clear_previous_generation(size: int):
    """Clears `size` lines of the previous terminal output from the terminal"""
    sys.stdout.write(f'\033[{size}A\033[K')


def show_iteration_as_grid(generation: List[str], size: int) -> None:
    """Takes an iteration from the game of life, and shows it as an `size` by `size` grid"""
    for i in range(0, len(generation), size):
        slice = generation[i : i + size]
        print(' '.join(slice))


def main():
    DEFAULT_ITERATIONS = 50
    DEFAULT_PAUSE_TIME = 0.2

    # setup commandline args
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', type=int, help='The width and height of the square grid')
    parser.add_argument('-i', '--iters', type=int, help='The number of unique iterations that the game will perform')
    parser.add_argument(
        '-p', '--pause', type=float, help='How much time passes between iterations. 0.5 is half a second'
    )
    args = parser.parse_args()

    size = args.size
    iterations = args.iters if args.iters else DEFAULT_ITERATIONS
    pause_time = args.pause if args.pause else DEFAULT_PAUSE_TIME

    # clamp pause time to values greater than 0
    if pause_time <= 0:
        pause_time = 0.04

    cell_grid = CellGrid(size=size)
    game = ConwaysGameOfLife(cell_grid)
    first_generation = list(game.first_generation.values())

    for iteration in game.run_game_of_life(iterations=iterations):
        current_generation = list(iteration.values())
        try:
            show_iteration_as_grid(current_generation, cell_grid.grid_size)
            time.sleep(pause_time)
        except KeyboardInterrupt:
            print('\nGoodbye!')
            break
        clear_previous_generation(game._grid._size)

    print('The last generation was:\n')
    last_generation = list(game.iteration_history.pop().values())
    show_iteration_as_grid(last_generation, cell_grid.grid_size)
    print(f'\nThat was {game._total_iterations} iterations from the original below:\n')
    show_iteration_as_grid(first_generation, cell_grid._size)


if __name__ == '__main__':
    main()
