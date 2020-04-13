from chaos.studio import Studio
from chaos.canvas import Canvas
from chaos.technique.trace import Trace
from chaos.technique.line_technique import LineTechnique
from chaos.util.random import *

canvas_width = 1000
canvas_height = 1000

studio = Studio(
    Canvas(canvas_width, canvas_height).new()
)

trace = Trace({'fill': 1, 'width': 1})

coordinates = random_coordinates(
    1000,
    random_int(1, canvas_width),
    1000,
    1000,
    random_int(1, canvas_width),
    1000,
    1000
)

for coordinate in coordinates:
    studio.execute_technique(
        LineTechnique(
            trace,
            (coordinate[0][0], round(canvas_height / 4)),
            (coordinate[0][1], round(canvas_height / 4) * 3)
        )
    )

studio.exhibition()
