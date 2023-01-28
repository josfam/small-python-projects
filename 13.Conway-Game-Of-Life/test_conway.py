from conway import CellGrid, ConwaysGameOfLife

ALIVE = '\u25A0'
DEAD = '-'


def test_grid_with_only_DEAD_cells_stays_DEAD_in_the_next_generation():
    cells = {
        (0, 0): DEAD,
        (1, 0): DEAD,
        (2, 0): DEAD,
        (0, 1): DEAD,
        (1, 1): DEAD,
        (2, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): DEAD,
        (2, 2): DEAD,
    }

    expected = {
        (0, 0): DEAD,
        (1, 0): DEAD,
        (2, 0): DEAD,
        (0, 1): DEAD,
        (1, 1): DEAD,
        (2, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): DEAD,
        (2, 2): DEAD,
    }

    grid = CellGrid(size=3, cell_arrangement=cells)
    game = ConwaysGameOfLife(CellGrid=grid)
    ALIVE_neighbours = game.count_living_neighbours(grid.cells)
    assert game.get_next_iteration(grid.cells, ALIVE_neighbours) == expected


def test_grid_that_does_not_evolve_stays_the_same_in_the_next_iteration():
    cells = {
        (0, 0): ALIVE,
        (1, 0): ALIVE,
        (2, 0): DEAD,
        (0, 1): ALIVE,
        (1, 1): ALIVE,
        (2, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): DEAD,
        (2, 2): DEAD,
    }

    expected = {
        (0, 0): ALIVE,
        (1, 0): ALIVE,
        (2, 0): DEAD,
        (0, 1): ALIVE,
        (1, 1): ALIVE,
        (2, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): DEAD,
        (2, 2): DEAD,
    }

    grid = CellGrid(size=3, cell_arrangement=cells)
    game = ConwaysGameOfLife(CellGrid=grid)
    ALIVE_neighbours = game.count_living_neighbours(grid.cells)
    assert game.get_next_iteration(grid.cells, ALIVE_neighbours) == expected


def test_grid_with_ALIVE_cells_on_one_digonal_has_all_DEAD_cells_in_the_third_iteration():
    cells = {
        (0, 0): ALIVE,
        (1, 0): DEAD,
        (2, 0): DEAD,
        (0, 1): DEAD,
        (1, 1): ALIVE,
        (2, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): DEAD,
        (2, 2): ALIVE,
    }

    first_iteration = {
        (0, 0): DEAD,
        (1, 0): DEAD,
        (2, 0): DEAD,
        (0, 1): DEAD,
        (1, 1): ALIVE,
        (2, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): DEAD,
        (2, 2): DEAD,
    }

    second_iteration = {
        (0, 0): DEAD,
        (1, 0): DEAD,
        (2, 0): DEAD,
        (0, 1): DEAD,
        (1, 1): DEAD,
        (2, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): DEAD,
        (2, 2): DEAD,
    }

    grid = CellGrid(size=3, cell_arrangement=cells)
    game = ConwaysGameOfLife(CellGrid=grid)
    ALIVE_neighbours = game.count_living_neighbours(grid.cells)
    assert game.get_next_iteration(grid.cells, ALIVE_neighbours) == first_iteration
    ALIVE_neighbours = game.count_living_neighbours(first_iteration)
    assert game.get_next_iteration(grid.cells, ALIVE_neighbours) == second_iteration


def test_game_of_life_returns_the_original_generation_first_then_subsequent_iterations_afterward():
    original = {
        (0, 0): ALIVE,
        (1, 0): DEAD,
        (2, 0): DEAD,
        (0, 1): DEAD,
        (1, 1): ALIVE,
        (2, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): ALIVE,
        (2, 2): ALIVE,
    }

    first_iteration = {
        (0, 0): DEAD,
        (1, 0): DEAD,
        (2, 0): DEAD,
        (0, 1): ALIVE,
        (1, 1): ALIVE,
        (2, 1): ALIVE,
        (0, 2): DEAD,
        (1, 2): ALIVE,
        (2, 2): ALIVE,
    }

    second_iteration = {
        (0, 0): DEAD,
        (1, 0): ALIVE,
        (2, 0): DEAD,
        (0, 1): ALIVE,
        (1, 1): DEAD,
        (2, 1): ALIVE,
        (0, 2): ALIVE,
        (1, 2): DEAD,
        (2, 2): ALIVE,
    }

    expected = [original, first_iteration, second_iteration]

    grid = CellGrid(size=3, cell_arrangement=original)
    game = ConwaysGameOfLife(grid)

    for expected_iteration, actual_iteration in zip(expected, game.run_game_of_life(iterations=3)):
        assert expected_iteration == actual_iteration


def test_the_last_item_in_iteration_history_is_latest_iteration():
    original = {
        (0, 0): DEAD,
        (1, 0): DEAD,
        (2, 0): DEAD,
        (3, 0): DEAD,
        (4, 0): DEAD,
        (0, 1): DEAD,
        (1, 1): DEAD,
        (2, 1): ALIVE,
        (3, 1): DEAD,
        (4, 1): DEAD,
        (0, 2): DEAD,
        (1, 2): ALIVE,
        (2, 2): ALIVE,
        (3, 2): ALIVE,
        (4, 2): DEAD,
        (0, 3): DEAD,
        (1, 3): DEAD,
        (2, 3): ALIVE,
        (3, 3): DEAD,
        (4, 3): DEAD,
        (0, 4): DEAD,
        (1, 4): DEAD,
        (2, 4): DEAD,
        (3, 4): DEAD,
        (4, 4): DEAD,
    }

    expected = {
        (0, 0): DEAD,
        (1, 0): ALIVE,
        (2, 0): ALIVE,
        (3, 0): ALIVE,
        (4, 0): DEAD,
        (0, 1): ALIVE,
        (1, 1): DEAD,
        (2, 1): DEAD,
        (3, 1): DEAD,
        (4, 1): ALIVE,
        (0, 2): ALIVE,
        (1, 2): DEAD,
        (2, 2): DEAD,
        (3, 2): DEAD,
        (4, 2): ALIVE,
        (0, 3): ALIVE,
        (1, 3): DEAD,
        (2, 3): DEAD,
        (3, 3): DEAD,
        (4, 3): ALIVE,
        (0, 4): DEAD,
        (1, 4): ALIVE,
        (2, 4): ALIVE,
        (3, 4): ALIVE,
        (4, 4): DEAD,
    }

    grid = CellGrid(size=3, cell_arrangement=original)
    game = ConwaysGameOfLife(CellGrid=grid)
    _ = list(game.run_game_of_life(iterations=4))  # exhaust the iterator
    assert game.iteration_history.pop() == expected
