from PIL import Image as Canvas
from PIL.ImageDraw import Draw
from .technique import Technique
from ..util.random import *


class LineTechnique(Technique):

    def draw_on(self, canvas: Canvas):
        Draw(canvas).line(
            [(get_int(0, 1000), get_int(0, 1000)), (get_int(0, 1000), get_int(0, 1000))], fill=self.get_fill(), width=self.get_width()
        )

    def get_fill(self):
        return self.trace.properties['fill']

    def get_width(self):
        return self.trace.properties['width']
