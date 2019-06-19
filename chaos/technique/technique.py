from PIL import ImageDraw
from trace import Trace

class Technique(object):
    def __init__(self, trace: Trace):
        self.trace = trace

    def draw(self, draw: ImageDraw):
        pass
