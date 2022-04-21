from models.rules import Seeds
from ui import Lattice, run_tkinter_animation

world = Seeds(
    {(50, 50), (50, 51), (50, 52), (60, 60), (60, 61), (31, 60), (31, 59), (30, 60), (10, 10), (11, 10)}
)
lattice = Lattice(0, 0, 100, 100, cell_size_in_pixels=5)

run_tkinter_animation(world, lattice, frames_per_second=8, num_frames=80)
