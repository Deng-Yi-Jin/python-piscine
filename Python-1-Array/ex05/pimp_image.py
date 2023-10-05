import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array) -> list:
    '''
    invert colour
    '''
    try:
        assert isinstance(array, np.ndarray), "This array is not a numpy array"
        assert array.ndim == 3, "This array is not a 3D array"
    except AssertionError as msg:
        print("Assertion Error:", msg)
        exit(0)
    else:
        invert_color = 255 - array
        plt.imshow(invert_color)
        plt.show()
        return invert_color


def ft_blue(array) -> list:
    '''
    change image to red
    '''
    try:
        assert isinstance(array, np.ndarray), "This array is not a numpy array"
        assert array.ndim == 3, "This array is not a 3D array"
    except AssertionError as msg:
        print("Assertion Error:", msg)
        exit(0)
    else:
        blue = np.copy(array)
        blue[:, :, 0] = 0
        blue[:, :, 1] = 0
        plt.imshow(blue)
        plt.show()
        return blue


def ft_green(array) -> list:
    '''
    change image to green
    '''
    try:
        assert isinstance(array, np.ndarray), "This array is not a numpy array"
        assert array.ndim == 3, "This array is not a 3D array"
    except AssertionError as msg:
        print("Assertion Error:", msg)
        exit(0)
    else:
        green = np.copy(array)
        green[:, :, 0] = 0
        green[:, :, 2] = 0
        plt.imshow(green)
        plt.show()
        return green


def ft_red(array) -> list:
    '''
    change image to red
    '''
    try:
        assert isinstance(array, np.ndarray), "This array is not a numpy array"
        assert array.ndim == 3, "This array is not a 3D array"
    except AssertionError as msg:
        print("Assertion Error:", msg)
        exit(0)
    else:
        red = np.copy(array)
        red[:, :, 1] = 0
        red[:, :, 2] = 0
        plt.imshow(red)
        plt.show()
        return red


def ft_grey(array) -> list:
    '''
    change image to grey
    '''
    try:
        assert isinstance(array, np.ndarray), "This array is not a numpy array"
        assert array.ndim == 3, "This array is not a 3D array"
    except AssertionError as msg:
        print("Assertion Error:", msg)
        exit(0)
    else:
        grey = np.copy(array)
        grey = grey[:, :, 1]
        plt.imshow(grey, cmap="gray")
        plt.show()
        return grey
