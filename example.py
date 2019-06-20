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

for i in range(100):

    coordinates = random_coordinates(
        random_int(1, 1),
        random_int(1, 1000),
        random_int(1, 1000),
        random_int(1, 60),
        random_int(1, 1000),
        random_int(1, 1000),
        random_int(1, 60)
    )

    studio.execute_technique(
        LineTechnique(
            trace,
            coordinates[0],
            coordinates[1]
        )
    )

studio.exhibition()
