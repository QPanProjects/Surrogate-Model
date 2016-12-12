"""
https://docs.python.org/2/library/functions.html
"""

# super(type[, object-or-type])

import operator
import random


def uniform(low, high, size=None):
    try:
        return [random.uniform(a, b) for a, b in zip(low, high)]
    except TypeError:
        return [random.uniform(a, b) for a, b in zip([low] * size, [high] * size)]


_Ndim = 10
values = uniform(low=0.0, high=1.0, size=_Ndim)
# weights = [-1.0, -1.0]
weights = uniform(low=0.0, high=1.0, size=_Ndim)
result1 = tuple(map(operator.mul, values, weights))
print result1

a = [1, 2, 3, 4]
b = [10, 11, 12, 13]
result2 = list(map(operator.mul, a, b))
print result2
