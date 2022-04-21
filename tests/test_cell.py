from models.cell import Cell


def test_cells_are_hashable_by_position():
    cell_a = Cell(x=0, y=0, state=14)
    cell_b = Cell(x=0, y=0, state=915)
    cell_c = Cell(x=0, y=1, state=14)
    assert hash(cell_a) == hash(cell_b)
    assert hash(cell_a) != hash(cell_c)
