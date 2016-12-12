"""Executes a one point crossover on :term:`sequence` individual.
The crossover will in most cases change the individuals size. The two
individuals are modified in place.

:param ind1: The first individual participating in the crossover.
:param ind2: The second individual participating in the crossover.
:returns: A tuple of two individuals.

This function uses the :func:`~random.randint` function from the python base
:mod:`random` module.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

import random


def cxMessyOnePoint(var1, var2):
    cxpoint1 = random.randint(0, len(var1))
    cxpoint2 = random.randint(0, len(var2))
    # cxpoint1 = random.randint(0, var1.size)
    # cxpoint2 = random.randint(0, var2.size)
    var1[cxpoint1:], var2[cxpoint2:] = var2[cxpoint2:], var1[cxpoint1:]
    # var1[cxpoint1:], var2[cxpoint1:] = var2[cxpoint1:].copy(), var1[cxpoint1:].copy()

    return var1, var2
