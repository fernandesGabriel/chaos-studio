from chaos import studio, canvas
from chaos.technique import technique, line_technique, trace

canvas = canvas.Cavnas(1000, 1000).get()
studio = studio.Studio(canvas)

trace = trace.Trace({'fill': 1, 'width': 4})
technique = line_technique.LineTechnique(trace)

for i in range(100):
    studio.draw_move(technique)

studio.exhibition()
