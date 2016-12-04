from operator import attrgetter

"""Select the *k* best individuals among the input *individuals*. The
list returned contains references to the input *individuals*.

:param individuals: A list of individuals to select from.
:param k: The number of individuals to select.
:returns: A list containing the k best individuals.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

def selBest(individuals, k=1):
    return sorted(individuals, key=attrgetter("fitness"), reverse=True)[:k]
