import pytest
from ui import Lattice


@pytest.mark.parametrize(
    "bad_coords", [(10, 10, 15, 5), (10, 10, 5, 15), (10, 20, 10, 21), (10, 20, 11, 20)]
)
def test_xo_and_yo_must_be_smaller_than_xf_yf(bad_coords):
    with pytest.raises(ValueError):
        _ = Lattice(*bad_coords)


def test_width_and_height_are_proportional_to_cell_size():
    grid = Lattice(0, 0, 10, 15, 5)
    assert grid.width == 50
    assert grid.height == 75


def test_cell_bounding_box_has_width_and_height_equal_to_cell_size():
    grid = Lattice(0, 0, 10, 15, 5)
    assert grid.get_cell_bounding_box(0, 0) == (0, 0, 5, 5)
    assert grid.get_cell_bounding_box(9, 14) == (45, 70, 50, 75)


def test_cell_bounding_box_is_offset_by_xo_yo():
    grid = Lattice(5, 5, 10, 15, 5)
    assert grid.get_cell_bounding_box(5, 5) == (0, 0, 5, 5)
    assert grid.get_cell_bounding_box(9, 14) == (20, 45, 25, 50)
