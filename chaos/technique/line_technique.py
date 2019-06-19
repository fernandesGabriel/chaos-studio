from PIL import Image as Canvas
from PIL.ImageDraw import Draw
from .technique import Technique
from trace import Trace


class LineTechnique(Technique):
    def __init__(self, trace: Trace, start: tuple, end: tuple):
        Technique.__init__(self, trace)

        self.start = start
        self.end = end

    def draw_on(self, canvas: Canvas):
        Draw(canvas).line(
            [self.start, self.end], fill=self.get_fill(), width=self.get_width()
        )

    def get_fill(self):
        return self.trace.properties['fill']

    def get_width(self):
        return self.trace.properties['width']
