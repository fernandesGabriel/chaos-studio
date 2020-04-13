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
            trace,
            (coordinate[0][0], coordinate[0][1]),
            (coordinate[0][0], coordinate[1][1])
        )
    )

coordinates2 = random_coordinates(
    500,
    333,
    canvas_height / 2,
    100,
    666,
    canvas_height / 2,
    100
)

for coordinate in coordinates2:
    studio.execute_technique(
        LineTechnique(
            trace,
            (coordinate[0][0], coordinate[0][1]),
            (coordinate[1][0], coordinate[0][1])
        )
    )

studio.exhibition()
