from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def zoom(path: str, factor: int | float):
    '''
    Load image, apply zoom factor, and return list of pixels.
    '''
    try:
        assert isinstance(path, str), "Path is not a str"
        assert isinstance(factor, (int, float)), "Factor is not a number"
        assert factor > 0 and factor < 1, \
            "Zoom number is between > 0 and <= 1"
    except AssertionError as msg:
        print("Assertion Error", msg)
        exit(0)
    image = Image.open(path)
    image_arr = np.array(image)
    # print(image_arr)
    x1 = int((image_arr.shape[0] * (1 - factor)) / 2)
    y1 = int((image_arr.shape[1] * (1 + factor)) / 2)
    x2 = int(image_arr.shape[0] - x1)
    y2 = int(image_arr.shape[1] - y1)
    image_slicing = image_arr[x1:x2, y1:y2]
    gray_image = np.dot(image_slicing[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    gray_image = Image.fromarray(gray_image)
    plt.imshow(gray_image)
    plt.show()
    gray_image

def main():
    zoom("animal.jpeg", 0.6)

if __name__ == "__main__":
    main()
