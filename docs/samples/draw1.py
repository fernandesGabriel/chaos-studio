from pathlib import Path

from chaos.studio import Studio
from chaos.canvas import Canvas
from chaos.technique.trace import Trace
from chaos.technique.line_technique import LineTechnique
from chaos.util.random import random_coordinates, random_int

canvas_width = 1000
canvas_height = 1000

studio = Studio(
    Canvas(canvas_width, canvas_height).new(),
    'docs/samples'
)

trace = Trace({'fill': (0, 0, 0), 'width': 1})

for i in range(100):
    coordinates = random_coordinates(
        random_int(1, 50),
        random_int(1, canvas_width),
        random_int(1, canvas_height),
        random_int(1, 100),
        random_int(1, canvas_width),
        random_int(1, canvas_height),
        random_int(1, 60)
    )

    for coordinate in coordinates:
        studio.execute_technique(
            LineTechnique(
                trace,
                coordinate[0],
                coordinate[1]
            )
        )

studio.publish(Path(__file__).stem)
