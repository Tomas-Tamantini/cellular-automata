from models.cell import Cell

from .rules_utils import neighbors


class Seeds:
    def __init__(self, initial_cell_positions: set[tuple[int, int]]) -> None:
        self.__cells_pos = initial_cell_positions

    @property
    def alive_cells(self) -> set[Cell]:
        return {Cell(*p) for p in self.__cells_pos}

    def tick(self) -> None:
        num_neighbors = dict()
        for cell_pos in self.__cells_pos:
            for neighbor in neighbors(*cell_pos):
                if neighbor in self.__cells_pos:
                    continue
                num_neighbors[neighbor] = num_neighbors.get(neighbor, 0) + 1
        self.__cells_pos = {p for (p, n) in num_neighbors.items() if n == 2}
