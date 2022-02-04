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

trace1 = Trace({'fill': (127, 127, 127), 'width': 2})

coordinates = random_coordinates(
    500,
    canvas_width / 2,
    333,
    100,
    canvas_width / 2,
    666,
    100
)

for coordinate in coordinates:
    studio.execute_technique(
        LineTechnique(
            trace1,
            (coordinate[0][0], coordinate[0][1]),
            (coordinate[0][0], coordinate[1][1])
        )
    )

trace2 = Trace({'fill': (0, 0, 0), 'width': 1})

coordinates2 = random_coordinates(
    1000,
    333,
    round(canvas_height / 2),
    100,
    666,
    round(canvas_height / 2),
    100
)

for coordinate in coordinates2:
    studio.execute_technique(
        LineTechnique(
            trace2,
            (coordinate[0][0], coordinate[0][1]),
            (coordinate[1][0], coordinate[0][1])
        )
    )

studio.publish(Path(__file__).stem)
