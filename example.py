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

trace = Trace({'fill': 1, 'width': 4})

for i in range(100):
    studio.execute_technique(
        LineTechnique(
            trace,
            (get_int(0, canvas_width), get_int(0, canvas_height)),
            (get_int(0, canvas_width), get_int(0, canvas_height))
        )
    )

studio.exhibition()
