import matplotlib.pyplot as plt

from skimage import data, color,io
from skimage.transform import rescale, resize, downscale_local_mean

import numpy as np


def get_resized_image(image):
	image = color.rgb2gray(image)
	image_rescaled = rescale(image, 1.0 / 10.0, anti_aliasing=False)
	image_resized = resize(image, (image.shape[0] / 10, image.shape[1] / 10),
	                       anti_aliasing=True)
	return np.array(image_resized)


def get_resized_image_from_path(path):

	image = io.imread(path)
	return get_resized_image(image)

	

def compute_similarity(i1, i2):
	return np.abs(np.subtract(np.array(i1),np.array(i2))).sum() / i1.size


#i1 = get_resized_image('/home/josecarranza/Desktop/chaos/circle.jpg')
#i2 = get_resized_image('/home/josecarranza/Desktop/chaos/circle_inverted.jpg')
#print(compute_similarity(i1,i2))



'''

image_downscaled = downscale_local_mean(image, (10, 3))

fig, axes = plt.subplots(nrows=2, ncols=2)

ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].set_title("Original image")

ax[1].imshow(image_rescaled, cmap='gray')
ax[1].set_title("Rescaled image (aliasing)")

ax[2].imshow(image_resized, cmap='gray')
ax[2].set_title("Resized image (no aliasing)")

ax[3].imshow(image_downscaled, cmap='gray')
ax[3].set_title("Downscaled image (no aliasing)")

ax[0].set_xlim(0, 1000)
ax[0].set_ylim(1000, 0)
plt.tight_layout()
plt.show()

'''