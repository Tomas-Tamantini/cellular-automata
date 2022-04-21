import pytest
from models import Cell
from models.rules import WireWorld


def test_there_can_be_no_cell_overlap():
    with pytest.raises(ValueError):
        _ = WireWorld(
            conductor_positions={(7, 9)},
            electron_head_positions={(7, 8), (7, 9), (7, 10)},
        )


def test_dead_world_stays_dead():
    wireworld = WireWorld()
    wireworld.tick()
    assert len(wireworld.alive_cells) == 0


def test_electron_head_becomes_electron_tail():
    wireworld = WireWorld(electron_head_positions={(10, 12)})
    wireworld.tick()
    assert wireworld.alive_cells == {Cell(10, 12, state=3)}


def test_electron_tail_becomes_conductor():
    wireworld = WireWorld(electron_tail_positions={(7, 9)})
    wireworld.tick()
    assert wireworld.alive_cells == {Cell(7, 9, state=1)}


def test_conductor_with_no_neighboring_electrons_stays_conductor():
    wireworld = WireWorld(conductor_positions={(7, 9)})
    wireworld.tick()
    assert wireworld.alive_cells == {Cell(7, 9, state=1)}


def test_conductor_with_more_than_two_neighboring_electrons_stays_conductor():
    electrons = {(7, 8), (7, 10), (8, 9)}
    wireworld = WireWorld(
        conductor_positions={(7, 9)}, electron_head_positions=electrons
    )
    wireworld.tick()
    assert wireworld.alive_cells == {
        Cell(7, 9, state=1),
        Cell(7, 8, state=3),
        Cell(7, 10, state=3),
        Cell(8, 9, state=3),
    }


def test_conductor_with_one_neighboring_electron_becomes_electron():
    electrons = {(7, 8)}
    wireworld = WireWorld(
        conductor_positions={(7, 9)}, electron_head_positions=electrons
    )
    wireworld.tick()
    assert wireworld.alive_cells == {Cell(7, 9, state=2), Cell(7, 8, state=3)}


def test_conductor_with_two_neighboring_electrons_becomes_electron():
    electrons = {(7, 8), (7, 10)}
    wireworld = WireWorld(
        conductor_positions={(7, 9)}, electron_head_positions=electrons
    )
    wireworld.tick()
    assert wireworld.alive_cells == {
        Cell(7, 9, state=2),
        Cell(7, 8, state=3),
        Cell(7, 10, state=3),
    }
