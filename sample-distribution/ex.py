import main
import draw 
from PIL import Image, ImageDraw
import random
import numpy as np
import image_tools

# ---------------------------------------
# Studio
# ---------------------------------------
canvas_width = 1000
canvas_height = 1000

image = Image.new('RGB',(canvas_width,canvas_height),'white')
canvas = ImageDraw.Draw(image)

drawer = draw.CanvasDrawer(canvas)

n = 100
for i in range(n):
	drawer.draw_lines(
		n=random.randint(1,50), 
		x1=random.randint(1,1000),
		y1=random.randint(1,1000),
		sigma1=random.randint(1,60),
		x2=random.randint(1,1000),
		y2=random.randint(1,1000),
		sigma2=random.randint(1,60))

'''
drawer.draw_lines(
		n=100000, 
		x1=500,
		y1=500,
		sigma1=0,
		x2=500,
		y2=500,
		sigma2=80)

'''
gen_image = np.array(image)[:,:,0] 
img = Image.fromarray(gen_image).convert('RGB')
img.save('temp.jpg')



i1 = image_tools.get_resized_image_from_path('/home/josecarranza/Desktop/chaos/circle.jpg')
i2 = image_tools.get_resized_image_from_path('/home/josecarranza/Desktop/chaos/temp.jpg')


print("The difference is: ")
print(image_tools.compute_similarity(i1,i2))


image.show()

