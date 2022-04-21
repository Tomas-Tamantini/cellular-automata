from typing import Iterator


def neighbors(x: int, y: int) -> Iterator[tuple[int, int]]:
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            yield (i, j)
