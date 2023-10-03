from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def ft_zoom(path: str, factor: int) -> list:
	'''
	Load image, apply zoom factor, and return list of pixels.
	'''
	try:
		assert isinstance(path, str), "This path is not a string"
		assert isinstance(factor, int), "Factor is not a int"
	except AssertionError as msg:
		print("Assertion Error:", msg)
		exit(0)
	image = Image.open(path)
	image_array = np.array(image)
	zoomed_width = image.width * factor
	zoomed_height = image.height * factor
	zoomed_image = image.resize((zoomed_width, zoomed_height))
	zoomed_image.show()
	
	
