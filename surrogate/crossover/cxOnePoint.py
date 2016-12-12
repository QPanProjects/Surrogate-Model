"""Executes a one point crossover on the input :term:`sequence` individuals.
The two individuals are modified in place. The resulting individuals will
respectively have the length of the other.

:param ind1: The first individual participating in the crossover.
:param ind2: The second individual participating in the crossover.
:returns: A tuple of two individuals.

This function uses the :func:`~random.randint` function from the
python base :mod:`random` module.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>
import numpy as np


def cxOnePoint(var1, var2):
    size = min(len(var1), len(var2))
    # size = min(var1.size, var2.size)
    cxpoint = np.random.randint(1, size - 1)
    var1[cxpoint:], var2[cxpoint:] = var2[cxpoint:], var1[cxpoint:]
    # var1[cxpoint:], var2[cxpoint:] = var2[cxpoint:].copy(), var1[cxpoint:].copy()

    return var1, var2
