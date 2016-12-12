"""Executes a uniform crossover that modify in place the two
:term:`sequence` individuals. The attributes are swapped accordingto the
*indpb* probability.

:param ind1: The first individual participating in the crossover.
:param ind2: The second individual participating in the crossover.
:param indpb: Independent probabily for each attribute to be exchanged.
:returns: A tuple of two individuals.

This function uses the :func:`~random.random` function from the python base
:mod:`random` module.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

import random


def cxUniform(var1, var2, prob=0.5):
    size = min(len(var1), len(var2))
    # size = min(var1.size, var2.size)
    for i in xrange(size):
        if random.random() < prob:
            var1[i], var2[i] = var2[i], var1[i]

    return var1, var2
