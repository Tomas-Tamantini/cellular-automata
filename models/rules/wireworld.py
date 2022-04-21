from models.cell import Cell

from .rules_utils import neighbors


class WireWorld:
    def __init__(
        self,
        conductor_positions: set[tuple[int, int]] = None,
        electron_head_positions: set[tuple[int, int]] = None,
        electron_tail_positions: set[tuple[int, int]] = None,
    ):
        c = conductor_positions or set()
        eh = electron_head_positions or set()
        et = electron_tail_positions or set()
        if c.intersection(eh) or c.intersection(et) or eh.intersection(et):
            raise ValueError("Cells cannot overlap")
        self.__conductor_positions = c
        self.__electron_head_positions = eh
        self.__electron_tail_positions = et

    @property
    def alive_cells(self) -> set[Cell]:
        """
        States:
            0 - empty
            1 - conductor
            2 - electron head
            3 - electron tail
        """
        cells = set()
        for x, y in self.__conductor_positions:
            cells.add(Cell(x, y, state=1))
        for x, y in self.__electron_head_positions:
            cells.add(Cell(x, y, state=2))
        for x, y in self.__electron_tail_positions:
            cells.add(Cell(x, y, state=3))
        return cells

    def tick(self) -> None:
        new_tails = {c for c in self.__electron_head_positions}
        new_conductors = {c for c in self.__electron_tail_positions}
        new_heads = set()

        for c in self.__conductor_positions:
            num_neighboring_electrons = len(
                [1 for n in neighbors(*c) if n in self.__electron_head_positions]
            )
            if num_neighboring_electrons == 1 or num_neighboring_electrons == 2:
                new_heads.add(c)
            else:
                new_conductors.add(c)

        self.__electron_tail_positions = new_tails
        self.__electron_head_positions = new_heads
        self.__conductor_positions = new_conductors
