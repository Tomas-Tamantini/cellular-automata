from models.cell import Cell
from models.rules import Seeds


def test_world_has_initial_living_cells():
    seeds = Seeds(initial_cell_positions={(0, 0), (10, 20)})
    assert len(seeds.alive_cells) == 2


def test_dead_world_stays_dead():
    seeds = Seeds(initial_cell_positions=set())
    seeds.tick()
    assert len(seeds.alive_cells) == 0


def test_alive_cells_die():
    seeds = Seeds(initial_cell_positions={(0, 0), (10, 20)})
    seeds.tick()
    assert len(seeds.alive_cells) == 0


def test_dead_cell_with_two_neighbors_is_born():
    seeds = Seeds(initial_cell_positions={(10, 10), (11, 10), (10, 11)})
    seeds.tick()
    assert seeds.alive_cells == {
        Cell(9, 10),
        Cell(9, 11),
        Cell(10, 9),
        Cell(11, 9),
    }
