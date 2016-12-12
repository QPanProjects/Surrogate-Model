"""Executes a partially matched crossover (PMX) on the input individuals.
The two individuals are modified in place. This crossover expects
:term:`sequence` individuals of indices, the result for any other type of
individuals is unpredictable.

:param ind1: The first individual participating in the crossover.
:param ind2: The second individual participating in the crossover.
:returns: A tuple of two individuals.

Moreover, this crossover generates two children by matching
pairs of values in a certain range of the two parents and swapping the values
of those indexes. For more details see [Goldberg1985]_.

This function uses the :func:`~random.randint` function from the python base
:mod:`random` module.

.. [Goldberg1985] Goldberg and Lingel, "Alleles, loci, and the traveling
   salesman problem", 1985.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

import random


def cxPartialyMatch(var1, var2):
    size = min(len(var1), len(var2))
    # size = min(var1.size, var2.size)
    p1, p2 = [0] * size, [0] * size

    # Initialize the position of each indices in the individuals
    for i in xrange(size):
        p1[var1[i]] = i
        p2[var2[i]] = i
    # Choose crossover points
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    # Apply crossover between cx points
    for i in xrange(cxpoint1, cxpoint2):
        # Keep track of the selected values
        temp1 = var1[i]
        temp2 = var2[i]
        # Swap the matched value
        var1[i], var1[p1[temp2]] = temp2, temp1
        var2[i], var2[p2[temp1]] = temp1, temp2
        # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return var1, var2
