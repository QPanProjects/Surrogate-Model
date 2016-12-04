import random

"""Select *k* individuals at random from the input *individuals* with
replacement. The list returned contains references to the input
*individuals*.

:param individuals: A list of individuals to select from.
:param k: The number of individuals to select.
:returns: A list of selected individuals.

This function uses the :func:`~random.choice` function from the
python base :mod:`random` module.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

def selRandom(individuals, k):
    return [random.choice(individuals) for i in xrange(k)]
