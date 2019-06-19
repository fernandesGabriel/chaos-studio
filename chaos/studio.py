from PIL import Image as Canvas
from .technique.technique import Technique


class Studio(object):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas

    def execute_technique(self, technique: Technique):
        technique.draw_on(self.canvas)

    def exhibition(self):
        self.canvas.show('Exhibition')
