from PIL import Image


class Canvas(object):
    def __init__(self, canvas_width: int, canvas_height: int, canvas_color: str = 'white', image_color: str = 'RGB'):

        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas_color = canvas_color
        self.image_color = image_color

    def create(self):
        return Image.new(
            self.image_color,
            (self.canvas_width, self.canvas_height),
            self.canvas_color
        )
