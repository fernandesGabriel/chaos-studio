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
    canvas_width/2,
    canvas_height/2,
    1,
    random_int(canvas_width/8, canvas_width),
    random_int(canvas_height/8, canvas_height),
    100
)

for coordinate in coordinates:
    studio.execute_technique(
        LineTechnique(
            trace,
            coordinate[0],
            coordinate[1]
        )
    )

studio.exhibition()
