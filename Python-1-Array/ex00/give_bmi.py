import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    '''
    This function takes two lists of equal
    length as input and returns a list of
    the corresponding BMI values.
    The BMI is calculated as weight divided by
    '''
    try:
        assert len(height) == len(weight), "lists are not the same length"
        assert type(height) is list, "arguments are not lists"
        assert type(weight) is list, "arguments are not lists"
        assert all(isinstance(x, (int, float)) for x in height), \
            "height list contains non-int or non-float"
        assert all(isinstance(x, (int, float)) for x in weight), \
            "weight list contains non-int or non-float"
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(0)
    else:
        mass = np.array(weight)
        tall = np.array(height)
        bmi = mass / (tall * tall)
        return list(bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    This function takes a list of BMI values and a limit value as input and
    returns a list of booleans indicating whether the corresponding BMI value
    '''
    try:
        assert type(bmi) is list, "bmi is not a list"
        assert type(limit) is int, "limit is not an integer"
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(0)
    else:
        BodyMassIndex = np.array(bmi)
        return list(BodyMassIndex > limit)
