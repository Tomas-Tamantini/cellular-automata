from models.rules import Seeds


def test_seeds_has_only_two_states():
    assert Seeds().number_of_cell_states == 2


def test_dead_world_stays_dead():
    seeds = Seeds()
    seeds.tick()
    assert len(seeds.alive_cells) == 0
