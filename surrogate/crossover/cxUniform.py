import random

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

def cxUniform(ind1, ind2, prob=0.5):
    size = min(len(ind1), len(ind2))
    for i in xrange(size):
        if random.random() < prob:
            ind1[i], ind2[i] = ind2[i], ind1[i]

    return ind1, ind2
