from typing import Protocol

from .cell import Cell


class CellularAutomaton(Protocol):
    @property
    def number_of_cell_states(self) -> int:
        ...

    @property
    def alive_cells(self) -> set[Cell]:
        ...

    def tick(self) -> None:
        """
        Compute the next generation of the cellular automaton.
        """
        ...
