from models.rules import Seeds, WireWorld, GameOfLife

from .lattice import Lattice
from .tk_animation import run_tkinter_animation


def run_seeds_example():
    seeds_world = Seeds(
        {
            (50, 50),
            (50, 51),
            (50, 52),
            (60, 60),
            (60, 61),
            (31, 60),
            (31, 59),
            (30, 60),
            (10, 10),
            (11, 10),
        }
    )
    seeds_lattice = Lattice(0, 0, 100, 100, cell_size_in_pixels=5)

    run_tkinter_animation(
        seeds_world, seeds_lattice, frames_per_second=8, num_frames=80
    )


def run_game_of_life_example():
    cells_left = {(0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (3, 0), (3, 2)}
    cells_right = {(7 - x, y) for (x, y) in cells_left}
    bullet_left = {(-79, 80), (-78, 79), (-77, 79), (-77, 80), (-77, 81)}
    bullet_right = {(-x, y) for (x, y) in bullet_left}
    gof_world = GameOfLife(
        set.union(cells_left, cells_right, bullet_left, bullet_right)
    )
    gof_lattice = Lattice(-50, -50, 50, 50, cell_size_in_pixels=5)

    run_tkinter_animation(gof_world, gof_lattice, frames_per_second=15, num_frames=1000)


def run_wireworld_example():
    # Figure 8
    conductors = set()
    conductors.update({(i, j) for i in range(10, 29) for j in (10, 20)})
    conductors.update({(i, j) for i in (10, 19, 28) for j in range(11, 21)})

    # Diodes
    conductors.update({(9, 15), (9, 14), (11, 15), (11, 14)})
    conductors.remove((10, 15))

    conductors.update({(27, 15), (27, 14), (29, 15), (29, 14)})
    conductors.remove((28, 14))

    conductors.update({(25, 19), (25, 21), (26, 19), (26, 21)})
    conductors.remove((25, 20))

    # Current
    electrons = {(19, 15), (15, 10), (15, 20)}
    electron_tails = {(19, 16), (16, 10), (14, 20)}
    conductors = conductors - electrons - electron_tails

    wireworld = WireWorld(
        conductor_positions=conductors,
        electron_head_positions=electrons,
        electron_tail_positions=electron_tails,
    )
    wireworld_lattice = Lattice(0, 0, 40, 40, cell_size_in_pixels=10)

    run_tkinter_animation(wireworld, wireworld_lattice, frames_per_second=8)
