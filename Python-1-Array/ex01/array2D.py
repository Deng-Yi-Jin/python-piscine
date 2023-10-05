import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Slice the 2D array and return a new 2D array
    '''
    try:
        assert type(family) is list, "This is not a list"
        assert all(isinstance(i, list) for i in family), "family is not in 2D"
        family_array = np.array(family)
        assert len(family_array.shape) == 2, "This is not a 2D array"
        assert type(start) is int, "Not an integer"
        assert type(end) is int, "Not an integer"
    except AssertionError as msg:
        print("Assertion Error", msg)
        exit(0)
    else:
        print("My Shape is {}".format(family_array))
        new_shape = family_array[start:end]
        print("My new shape is {}".format(new_shape))
        return [list(i) for i in new_shape]
