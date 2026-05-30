import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from triangle import Triangle
from rectangle import Rectangle
from trapeze import Trapeze
from parallelogram import Parallelogram
from circle import Circle
from ball import Ball
from triangular_pyramid import TriangularPyramid
from quadrangular_pyramid import QuadrangularPyramid
from rectangular_parallelepiped import RectangularParallelepiped
from cone import Cone
from triangular_prism import TriangularPrism

FIGURES = {
    "Triangle": Triangle,
    "Rectangle": Rectangle,
    "Trapeze": Trapeze,
    "Parallelogram": Parallelogram,
    "Circle": Circle,
    "Ball": Ball,
    "TriangularPyramid": TriangularPyramid,
    "QuadrangularPyramid": QuadrangularPyramid,
    "RectangularParallelepiped": RectangularParallelepiped,
    "Cone": Cone,
    "TriangularPrism": TriangularPrism,
}

def create_figure(line):
    parts = line.split()
    if not parts or parts[0] not in FIGURES:
        return None
    params = [float(x) for x in parts[1:]]
    return FIGURES[parts[0]](*params)

def process_file(filepath):
    figures = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                fig = create_figure(line)
                if fig:
                    figures.append((line, fig))
    if not figures:
        return None, 0
    return max(figures, key=lambda x: x[1].volume())

INPUT_FILES = [
     "input01.txt",
    "input02.txt",
   "input03.txt"]

output_path = os.path.join(os.path.dirname(__file__), "output.txt")

with open(output_path, 'w', encoding='utf-8') as out:
    for path in INPUT_FILES:
        name = os.path.basename(path)
        line_str, fig = process_file(path)
        vol = fig.volume() if fig else 0
        result = f"File: {name}\nFigure: {line_str}\nVolume: {vol:.4f}\n\n"
        out.write(result)
        print(result, end='')
