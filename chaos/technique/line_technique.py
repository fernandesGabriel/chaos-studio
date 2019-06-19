from PIL import ImageDraw
from .technique import Technique
from ..util.random import *


class LineTechnique(Technique):

    def draw(self, draw: ImageDraw):
        draw.line(
            [(get_int(0, 1000), get_int(0, 1000)), (get_int(0, 1000), get_int(0, 1000))], fill=self.get_fill(), width=self.get_width()
        )

    def get_fill(self):
        return self.trace.properties['fill']

    def get_width(self):
        return self.trace.properties['width']
