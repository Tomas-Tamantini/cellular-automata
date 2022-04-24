from models.cell import Cell
from models.rules import GameOfLife


def test_world_has_initial_living_cells():
    gof = GameOfLife(initial_cell_positions={(0, 0), (10, 20)})
    assert len(gof.alive_cells) == 2


def test_dead_world_stays_dead():
    gof = GameOfLife(initial_cell_positions=set())
    gof.tick()
    assert len(gof.alive_cells) == 0


def test_lonely_cells_die():
    gof = GameOfLife(initial_cell_positions={(0, 0), (10, 20)})
    gof.tick()
    assert len(gof.alive_cells) == 0

# TODO: Add more tests for each rule