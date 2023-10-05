from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    '''
    Load image from path
    '''
    try:
        assert isinstance(path, str), "This path input is not a string"
    except AssertionError as msg:
        print("Assertion Error", msg)
        exit(0)
    else:
        img = Image.open(path)
        img_array = np.array(img)
        return img_array
        