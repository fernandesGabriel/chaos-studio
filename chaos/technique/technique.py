from PIL import Image as Canvas
from trace import Trace


class Technique(object):
    def __init__(self, trace: Trace):
        self.trace = trace

    def draw_on(self, canvas: Canvas):
        pass
