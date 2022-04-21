from models.cell import Cell


class Seeds:
    @property
    def number_of_cell_states(self) -> int:
        return 2

    @property
    def alive_cells(self) -> set[Cell]:
        return set()

    def tick(self) -> None:
        pass
