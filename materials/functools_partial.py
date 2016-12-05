# https://www.pydanny.com/python-partials-are-fun.html

# this duplicates Python's built-in pow() function, but our version has the very nice addition of keyword arguments.
def power(base, exponent):
    return base ** exponent


def square(base):
    return power(base, 2)


def cube(base):
    return power(base, 3)


# Let's rewrite our square and cube functions using partials
from functools import partial

square = partial(power, exponent=2)
cube = partial(power, exponent=3)


def test_partials():
    assert square(2) == 4
    assert cube(2) == 8
