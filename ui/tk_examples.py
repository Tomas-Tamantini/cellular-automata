from models.rules import Seeds, WireWorld

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


def run_wireworld_example():
    # Figure 8
    conductors = set()
    for i in range(10):
        conductors.add((i + 10, 10))
        conductors.add((i + 10, 20))
        conductors.add((i + 19, 10))
        conductors.add((i + 19, 20))
        conductors.add((10, 11 + i))
        conductors.add((19, 11 + i))
        conductors.add((28, 11 + i))

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
