from models.cell import Cell


class Seeds:
    def __init__(self, cells: set[tuple[int, int]]) -> None:
        self.__cells = cells

    @property
    def number_of_cell_states(self) -> int:
        return 2

    @property
    def alive_cells(self) -> set[Cell]:
        return self.__cells

    def tick(self) -> None:
        self.__cells = set()
