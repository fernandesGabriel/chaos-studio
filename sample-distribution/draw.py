import math
import main
from random import randint

# ---------------------------------------
# Functions
# ---------------------------------------

class CanvasDrawer:
	def __init__(self, canvas):
		self.canvas = canvas

	def draw_lines(self, n, x1, y1, sigma1, x2, y2, sigma2 ):
		conf_1 = {
			'x': x1,
			'y': y1,
			'std_deviation':sigma1 
		}
		conf_2 = {
			'x': x2,
			'y': y2,
			'std_deviation':sigma2
		}
		coordinates = main.get_coordinates(n, conf_1, conf_2)

		
		print(coordinates)
		print('--------')

		for i in range(n):
			self.canvas.line(self.get_line_coordinates(coordinates[i,0],coordinates[i,1]), fill=0, width=1)

	def get_line_coordinates(self, point_1, point_2):
		return [(point_1[0],point_1[1]), (point_2[0],point_2[1])]
