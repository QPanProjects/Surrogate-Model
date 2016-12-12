import random

from ._partition import _partition


def _randomizedPartition(array, begin, end):
    i = random.randint(begin, end)
    array[begin], array[i] = array[i], array[begin]
    return _partition(array, begin, end)
