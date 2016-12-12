"""Executes a blend crossover that modify in-place the input individuals.
The blend crossover expects :term:`sequence` individuals of floating point
numbers.

:param ind1: The first individual participating in the crossover.
:param ind2: The second individual participating in the crossover.
:param alpha: Extent of the interval in which the new values can be drawn
              for each attribute on both side of the parents' attributes.
:returns: A tuple of two individuals.

This function uses the :func:`~random.random` function from the python base
:mod:`random` module.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

import random


def cxBlend(var1, var2, alpha=0.5):
    for i, (x1, x2) in enumerate(zip(var1, var2)):
        gamma = (1. + 2. * alpha) * random.random() - alpha
        var1[i] = (1. - gamma) * x1 + gamma * x2
        var2[i] = gamma * x1 + (1. - gamma) * x2

    return var1, var2
