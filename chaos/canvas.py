from PIL import Image


class Cavnas(object):
    def __init__(self, canvas_width: int, canvas_height: int, canvas_color: str = 'white', image_color: str = 'RGB'):

        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas_color = canvas_color
        self.image_color = image_color

        self.canvas = Image.new(
            image_color, (canvas_width, canvas_height), canvas_color
        )

    def get(self):
        return self.canvas
