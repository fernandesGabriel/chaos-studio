from pathlib import Path

from chaos.studio import Studio
from chaos.canvas import Canvas
from chaos.technique.trace import Trace
from chaos.technique.line_technique import LineTechnique
from chaos.util.random import random_coordinates

canvas_width = 1000
canvas_height = 1000

studio = Studio(
    Canvas(canvas_width, canvas_height).new(),
    'docs/samples'
)

trace = Trace({'fill': (0, 0, 0), 'width': 1})

coordinates = random_coordinates(
    1000,
    round(canvas_width / 2),
    333,
    100,
    round(canvas_width / 2),
    666,
    100
)

for coordinate in coordinates:
    studio.execute_technique(
        LineTechnique(
            trace,
            (coordinate[0][0], coordinate[0][1]),
            (coordinate[0][0], coordinate[1][1])
        )
    )

studio.publish(Path(__file__).stem)
