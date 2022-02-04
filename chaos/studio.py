from os import path, mkdir
from PIL import Image as Canvas

from .technique.technique import Technique


class Studio(object):
    def __init__(self, canvas: Canvas, location: str = './'):
        self.canvas = canvas
        self.location = location

    def execute_technique(self, technique: Technique):
        technique.draw_on(self.canvas)

    def exhibition(self, name: str = ''):
        self.canvas.show(name)

    def publish(self, name: str, ext: str = 'jpg'):
        if not path.exists(self.location):
            mkdir(self.location)

        self.canvas.save(fp=f'{self.location}/{name}.{ext}')
