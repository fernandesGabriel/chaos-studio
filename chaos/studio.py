import math
from random import randint
from PIL import Image, ImageDraw


class Studio(object):
    def __init__(self, canvas: Image):
        self.canvas = canvas

    def draw_move(self, technique):
        technique.draw(ImageDraw.Draw(self.canvas))

    def exhibition(self):
        self.canvas.show('Exhibition')
