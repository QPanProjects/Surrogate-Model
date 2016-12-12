"""Executes a simulated binary crossover that modify in-place the input
individuals. The simulated binary crossover expects :term:`sequence`
individuals of floating point numbers.

:param ind1: The first individual participating in the crossover.
:param ind2: The second individual participating in the crossover.
:param eta: Crowding degree of the crossover. A high eta will produce
            children resembling to their parents, while a small eta will
            produce solutions much more different.
:param low: A value or a :term:`python:sequence` of values that is the lower
            bound of the search space.
:param up: A value or a :term:`python:sequence` of values that is the upper
           bound of the search space.
:returns: A tuple of two individuals.

This function uses the :func:`~random.random` function from the python base
:mod:`random` module.

.. note::
   This implementation is similar to the one implemented in the
   original NSGA-II C code presented by Deb.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

import random
from collections import Sequence
from itertools import repeat


def cxSimulatedBinaryBounded(var1, var2, eta=15, low=0.0, up=1.0):
    size = min(len(var1), len(var2))
    # size = min(var1.size, var2.size)
    if not isinstance(low, Sequence):
        low = repeat(low, size)
    elif len(low) < size:
        raise IndexError("low must be at least the size of the shorter individual: %d < %d" % (len(low), size))
    if not isinstance(up, Sequence):
        up = repeat(up, size)
    elif len(up) < size:
        raise IndexError("up must be at least the size of the shorter individual: %d < %d" % (len(up), size))

    for i, xl, xu in zip(xrange(size), low, up):
        if random.random() <= 0.5:
            # This epsilon should probably be changed for 0 since
            # floating point arithmetic in Python is safer
            if abs(var1[i] - var2[i]) > 1e-14:
                x1 = min(var1[i], var2[i])
                x2 = max(var1[i], var2[i])
                rand = random.random()

                beta = 1.0 + (2.0 * (x1 - xl) / (x2 - x1))
                alpha = 2.0 - beta ** -(eta + 1)
                if rand <= 1.0 / alpha:
                    beta_q = (rand * alpha) ** (1.0 / (eta + 1))
                else:
                    beta_q = (1.0 / (2.0 - rand * alpha)) ** (1.0 / (eta + 1))

                c1 = 0.5 * (x1 + x2 - beta_q * (x2 - x1))

                beta = 1.0 + (2.0 * (xu - x2) / (x2 - x1))
                alpha = 2.0 - beta ** -(eta + 1)
                if rand <= 1.0 / alpha:
                    beta_q = (rand * alpha) ** (1.0 / (eta + 1))
                else:
                    beta_q = (1.0 / (2.0 - rand * alpha)) ** (1.0 / (eta + 1))
                c2 = 0.5 * (x1 + x2 + beta_q * (x2 - x1))

                c1 = min(max(c1, xl), xu)
                c2 = min(max(c2, xl), xu)

                if random.random() <= 0.5:
                    var1[i] = c2
                    var2[i] = c1
                else:
                    var1[i] = c1
                    var2[i] = c2

    return var1, var2
