import math
from .technique import Technique
from ..util import random as r


class LineTechnique(Technique):

    def draw(self, draw):
        draw.line(
            [(r.get_int(0, 1000), r.get_int(0, 1000)), (r.get_int(0, 1000), r.get_int(0, 1000))], fill=self.get_fill(), width=self.get_width()
        )

    def get_fill(self):
        return self.trace.properties['fill']

    def get_width(self):
        return self.trace.properties['width']
