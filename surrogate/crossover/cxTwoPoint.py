"""Executes a two-point crossover on the input :term:`sequence`
individuals. The two individuals are modified in place and both keep
their original length.

:param ind1: The first individual participating in the crossover.
:param ind2: The second individual participating in the crossover.
:returns: A tuple of two individuals.

This function uses the :func:`~random.randint` function from the Python
base :mod:`random` module.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

import random


def cxTwoPoint(var1, var2):
    size = min(len(var1), len(var2))
    # size = min(var1.size, var2.size)
    cxpoint1 = random.randint(1, size)
    cxpoint2 = random.randint(1, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    var1[cxpoint1:cxpoint2], var2[cxpoint1:cxpoint2] = var2[cxpoint1:cxpoint2], var1[cxpoint1:cxpoint2]
    # var1[cxpoint1:cxpoint2], var2[cxpoint1:cxpoint2] = var2[cxpoint1:cxpoint2].copy(), var1[cxpoint1:cxpoint2].copy()

    return var1, var2
