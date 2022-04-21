from tkinter import Canvas, Tk

from models import CellularAutomaton

from .lattice import Lattice


def run_tkinter_animation(
    cellular_automaton: CellularAutomaton,
    lattice: Lattice,
    num_frames: int = 1000,
    frames_per_second: int = 40,
):
    frame_duration_ms = 1000 // frames_per_second
    root = Tk()
    canvas = Canvas(root, width=lattice.width, height=lattice.height)
    for _ in range(num_frames):
        canvas.delete("all")
        _draw_world(canvas, lattice, cellular_automaton)
        canvas.pack()
        root.update()
        root.after(frame_duration_ms)
        cellular_automaton.tick()
    root.mainloop()


def _draw_world(
    canvas: Canvas, lattice: Lattice, cellular_automaton: CellularAutomaton
) -> None:
    for c in cellular_automaton.alive_cells:
        cb = lattice.get_cell_bounding_box(c.x, c.y)
        canvas.create_rectangle(*cb, fill="black", outline="grey")
