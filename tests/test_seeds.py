from models.rules import Seeds


def test_seeds_has_only_two_states():
    assert Seeds(cells=set()).number_of_cell_states == 2


def test_world_has_initial_living_cells():
    seeds = Seeds(cells={(0, 0), (10, 20)})
    assert len(seeds.alive_cells) == 2


def test_dead_world_stays_dead():
    seeds = Seeds(cells=set())
    seeds.tick()
    assert len(seeds.alive_cells) == 0


def test_alive_cells_die():
    seeds = Seeds(cells={(0, 0), (10, 20)})
    seeds.tick()
    assert len(seeds.alive_cells) == 0
