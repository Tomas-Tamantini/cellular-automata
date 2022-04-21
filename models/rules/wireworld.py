from models.cell import Cell

from .rules_utils import neighbors


class WireWorld:
    """
    States:
        0 - empty
        1 - conductor
        2 - electron head
        3 - electron tail
    """

    def __init__(self, initial_cells: set[Cell]) -> None:
        self.__electron_heads = {cell for cell in initial_cells if cell.state == 2}
        self.__electron_tails = {cell for cell in initial_cells if cell.state == 3}

    @property
    def alive_cells(self) -> set[Cell]:
        return set.union(self.__electron_heads, self.__electron_tails)

    def tick(self) -> None:
        new_tails = {Cell(c.x, c.y, state=3) for c in self.__electron_heads}
        self.__electron_tails = new_tails

        new_heads = set()
        self.__electron_heads = new_heads
