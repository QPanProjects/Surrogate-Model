import random

"""Shuffle the attributes of the input individual and return the mutant.
The *individual* is expected to be a :term:`sequence`. The *prob* argument is the
probability of each attribute to be moved. Usually this mutation is applied on
vector of indices.

:param individual: Individual to be mutated.
:param prob: Independent probability for each attribute to be exchanged to
              another position.
:returns: A tuple of one individual.

This function uses the :func:`~random.random` and :func:`~random.randint`
functions from the python base :mod:`random` module.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

def mutShuffleIndexes(individual, prob=0.5):
    size = len(individual)
    for i in xrange(size):
        if random.random() < prob:
            swap_indx = random.randint(0, size - 2)
            if swap_indx >= i:
                swap_indx += 1
            individual[i], individual[swap_indx] = \
                individual[swap_indx], individual[i]

    return individual,
