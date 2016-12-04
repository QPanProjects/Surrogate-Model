import random
from collections import Sequence
from itertools import repeat

"""Mutate an individual by replacing attributes, with probability *prob*,
by a integer uniformly drawn between *low* and *up* inclusively.

:param individual: :term:`Sequence <sequence>` individual to be mutated.
:param low: The lower bound or a :term:`python:sequence` of
            of lower bounds of the range from wich to draw the new
            integer.
:param up: The upper bound or a :term:`python:sequence` of
           of upper bounds of the range from wich to draw the new
           integer.
:param prob: Independent probability for each attribute to be mutated.
:returns: A tuple of one individual.
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

def mutUniformInt(individual, low=0.0, up=1.0, prob=0.5):
    size = len(individual)
    if not isinstance(low, Sequence):
        low = repeat(low, size)
    elif len(low) < size:
        raise IndexError("low must be at least the size of individual: %d < %d" % (len(low), size))
    if not isinstance(up, Sequence):
        up = repeat(up, size)
    elif len(up) < size:
        raise IndexError("up must be at least the size of individual: %d < %d" % (len(up), size))

    for i, xl, xu in zip(xrange(size), low, up):
        if random.random() < prob:
            individual[i] = random.randint(xl, xu)

    return individual,
