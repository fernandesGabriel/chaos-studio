from chaos.studio import Studio
from chaos.canvas import Canvas
from chaos.technique.trace import Trace
from chaos.technique.line_technique import LineTechnique

studio = Studio(
    Canvas(1000, 1000).create()
)

technique = LineTechnique(
    Trace({'fill': 1, 'width': 4})
)

for i in range(100):
    studio.execute_moviment(technique)

studio.exhibition()
