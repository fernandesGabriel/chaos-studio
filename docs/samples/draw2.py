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

coordinates = random_coordinates(
    500,
    random_int(round(canvas_width / 8), round(canvas_width / 8) * 6),
    random_int(round(canvas_height / 8), round(canvas_height / 8) * 6),
    random_int(1, 100),
    random_int(round(canvas_width / 8), round(canvas_width / 8) * 6),
    random_int(round(canvas_height / 8), round(canvas_height / 8) * 6),
    random_int(1, 50)
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
