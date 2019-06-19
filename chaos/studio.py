from PIL import Image, ImageDraw
from .technique.technique import Technique


class Studio(object):
    def __init__(self, canvas: Image):
        self.canvas = canvas

    def execute_moviment(self, technique: Technique):
        technique.draw(ImageDraw.Draw(self.canvas))

    def exhibition(self):
        self.canvas.show('Exhibition')
