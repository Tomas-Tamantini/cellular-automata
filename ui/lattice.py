class Lattice:
    def __init__(
        self, xo: int, yo: int, xf: int, yf: int, cell_size_in_pixels: int = 5
    ) -> None:
        if xf <= xo or yf <= yo:
            raise ValueError("xf and yf must be greater than xo and yo")
        self.__xo = xo
        self.__yo = yo
        self.__xf = xf
        self.__yf = yf
        self.__cell_size = cell_size_in_pixels

    @property
    def width(self) -> int:
        return (self.__xf - self.__xo) * self.__cell_size

    @property
    def height(self) -> int:
        return (self.__yf - self.__yo) * self.__cell_size

    def get_cell_bounding_box(
        self, cell_x_pos: int, cell_y_pos: int
    ) -> tuple[int, int, int, int]:
        x = (cell_x_pos - self.__xo) * self.__cell_size
        y = (cell_y_pos - self.__yo) * self.__cell_size
        return (
            x,
            y,
            x + self.__cell_size,
            y + self.__cell_size,
        )
