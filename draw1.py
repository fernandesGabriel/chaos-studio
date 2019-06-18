import math
from random import randint
from PIL import Image, ImageDraw

# ---------------------------------------
# Functions
# ---------------------------------------
def techiniqueLine(width, height):

    return [(randint(0, width),randint(0, height)), (randint(0, width),randint(0, height))]

# ---------------------------------------
# Studio
# ---------------------------------------
canvas_width = 2000
canvas_height = 2000

image = Image.new('RGB',(canvas_width,canvas_height),'white')
draw = ImageDraw.Draw(image)

for i in range(randint(0, 100)):
    draw.line(techiniqueLine(canvas_width,canvas_height), fill=0, width=4)

image.show()