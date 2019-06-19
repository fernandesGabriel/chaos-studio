import main
import draw 
from PIL import Image, ImageDraw

# ---------------------------------------
# Studio
# ---------------------------------------
canvas_width = 1000
canvas_height = 1000

image = Image.new('RGB',(canvas_width,canvas_height),'white')
canvas = ImageDraw.Draw(image)

drawer = draw.CanvasDrawer(canvas)



drawer.draw_lines(n=10, x1=500, y1=500, sigma1=100, x2=0, y2=0, sigma2=0)

drawer.draw_lines(n=20, x1=1000, y1=1000, sigma1=100, x2=500, y2=500, sigma2=10)

image.show()

