def square(x: int | float) -> int | float:
    """Square"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Power"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Local Variable"""
    count = 0

    def inner() -> float:
        """Inner"""
        nonlocal count
        if (count == 0):
            count = function(x)
        else:
            count = function(count)
        return count
    return inner
