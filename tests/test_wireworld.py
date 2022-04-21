from models import Cell
from models.rules import WireWorld


def test_dead_world_stays_dead():
    wireworld = WireWorld(initial_cells=set())
    wireworld.tick()
    assert len(wireworld.alive_cells) == 0


def test_electron_head_becomes_electron_tail():
    electron = Cell(10, 12, state=2)
    wireworld = WireWorld(initial_cells={electron})
    wireworld.tick()
    assert wireworld.alive_cells == {Cell(10, 12, state=3)}
