import math
from random import randint
from PIL import Image, ImageDraw

# ---------------------------------------
# Functions
# ---------------------------------------
def techiniqueCurve(width, height, precision=1):

    # check for a valid curve
    precision = precision if precision > 1 else 1

    curve_start = (100,10) 
    curve_end = (200,10)

    curve = [curve_start] 
    for i in range(precision):        
        x = 50
        y = 50

        # make sure x and y still on the frame
        x = x if x > 0 else 0
        y = y if y > 0 else 0
        
        curve.append((x, y))

    curve.append(curve_end)

    print(repr(curve))
    
    return curve

def techiniqueLine(width, height):

    return [(randint(0, width),randint(0, height)), (randint(0, width),randint(0, height))]


def randomDistribution(start, end, focus=0, probability=1):

    # randomize without weighted distribution
    if focus == 0:
        return randint(start, end)

    # check valid distribution
    focus = focus if focus > 0 else 0
    focus = focus if focus < 1 else 1
    end = end if end >= start else start

    epcenter = round((end - start) * focus)
    magnitude = round((end - start) * probability)

    multiplier_start = round(magnitude / (epcenter - start)) 
    multiplier_end = round(magnitude / (end - epcenter))

    possiblities = []

    # add choices before epcenter
    for i in range(start, epcenter):
        for n in range(multiplier_start):
            possiblities.append(i)

    # add epcenter choices
    for n in range(magnitude):
            possiblities.append(epcenter)

    # add choices after epcenter
    for i in reversed(range(epcenter+1, end+1)):
        for n in range(multiplier_end):
            possiblities.append(i)

    return possiblities[randint(0, len(possiblities)-1)]

# ---------------------------------------
# Studio
# ---------------------------------------
canvas_width = 2000
canvas_height = 2000

image = Image.new('RGB',(canvas_width,canvas_height),'white')
draw = ImageDraw.Draw(image)

# for i in range(randint(0, 100)):
#     draw.line(techiniqueLine(canvas_width,canvas_height), fill=0, width=4)

# for i in range(randint(0, 100)):
#     draw.line(techiniqueCurve(canvas_width,canvas_height,1), fill=0, width=2)

for i in range(100):
    x = randomDistribution(0, 2000, .2)
    draw.line([(x, 100),(x+1, 100)], fill=1, width=50)

image.show()