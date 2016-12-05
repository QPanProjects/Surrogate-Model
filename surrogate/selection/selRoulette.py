import random
from operator import attrgetter

"""Select *k* individuals from the input *individuals* using *k*
spins of a roulette. The selection is made by looking only at the first
objective of each individual. The list returned contains references to
the input *individuals*.

:param individuals: A list of individuals to select from.
:param k: The number of individuals to select.
:returns: A list of selected individuals.

This function uses the :func:`~random.random` function from the python base
:mod:`random` module.

.. warning::
   The roulette selection by definition cannot be used for minimization
   or when the fitness can be smaller or equal to 0.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

def selRoulette(individuals, k=1):
    s_inds = sorted(individuals, key=attrgetter("fitness"), reverse=True)
    # TODO 20161204 individual property fitness.values[]
    # sum_fits = sum(ind.fitness.values[0] for ind in individuals)
    sum_fits = sum(ind.fitness for ind in individuals)

    chosen = []
    for i in xrange(k):
        u = random.random() * sum_fits
        sum_ = 0
        for ind in s_inds:
            # sum_ += ind.fitness.values[0]
            sum_ += ind.fitness
            if sum_ > u:
                chosen.append(ind)
                break

    return chosen
