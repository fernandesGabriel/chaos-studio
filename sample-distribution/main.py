import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random

import matplotlib.lines as mlines

def plot(mu, sigma, points=1000):
	s = np.random.normal(mu, sigma, points)
	return s 

	count, bins, ignored = plt.hist(s, 30, density=True)
	plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
	               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
	         linewidth=2, color='r')
	plt.show()



def getRandomCoordinates(n, conf):
	x = plot(mu=conf['x'], sigma=conf['std_deviation'], points=n)
	y = plot(mu=conf['y'], sigma=conf['std_deviation'], points=n)
	response = []
	for i in range(n):
		response += [[x[random.randint(0,n-1)], y[random.randint(0,n-1)]]]
	return np.array(response)




def get_coordinates(n, conf_1, conf_2):
	points_1 = getRandomCoordinates(n,conf_1)
	points_2 = getRandomCoordinates(n,conf_2)
	segs = np.zeros((n,2, 2))
	segs[:,0] = points_1
	segs[:,1] = points_2
	return segs