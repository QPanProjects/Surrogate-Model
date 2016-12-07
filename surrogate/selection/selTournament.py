"""Select *k* individuals from the input *individuals* using *k*
tournaments of *tournsize* individuals. The list returned contains
references to the input *individuals*.

:param individuals: A list of individuals to select from.
:param k: The number of individuals to select.
:param tournsize: The number of individuals participating in each tournament.
:returns: A list of selected individuals.

This function uses the :func:`~random.choice` function from the python base
:mod:`random` module.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

from operator import attrgetter

from .selRandom import selRandom

def selTournament(individuals, k=1, tournsize=1):
    chosen = []
    for i in xrange(k):
        aspirants = selRandom(individuals, tournsize)
        chosen.append(max(aspirants, key=attrgetter("fitness")))
    return chosen
