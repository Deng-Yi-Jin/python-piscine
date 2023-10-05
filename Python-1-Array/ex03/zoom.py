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
        assert factor >= 0 and factor < 0.5, \
            "Zoom number is between > 0 and <= 1"
    except AssertionError as msg:
        print("Assertion Error", msg)
        exit(0)
    image = Image.open(path)
    image_arr = np.array(image)
    x1 = int((image_arr.shape[0] * factor))
    y1 = int((image_arr.shape[1] * factor))
    x2 = int(image_arr.shape[0] - x1)
    y2 = int(image_arr.shape[1] - y1)
    image_slicing = image_arr[x1:x2, y1:y2]

    gray_image = np.dot(image_slicing[..., :3], [0.2989, 0.5870, 0.1140])
    gray_image_axis = gray_image[:, :, np.newaxis]

    print("New shape after Transpose: ", gray_image.shape)
    print(np.round(gray_image_axis).astype(int))

    plt.imshow(Image.fromarray(gray_image))
    plt.show()


def main():
    print(ft_load("animal.jpeg"))
    zoom("animal.jpeg", 0.2)
    print()


if __name__ == "__main__":
    main()
