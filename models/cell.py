from dataclasses import dataclass


@dataclass(frozen=True)
class Cell:
    x: int
    y: int
    state: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))
