import random

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

def cxOnePoint(ind1, ind2):
    size = min(len(ind1), len(ind2))
    cxpoint = random.randint(1, size - 1)
    ind1[cxpoint:], ind2[cxpoint:] = ind2[cxpoint:], ind1[cxpoint:]

    return ind1, ind2
