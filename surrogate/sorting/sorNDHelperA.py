from operator import itemgetter

from .sorNDHelperB import sorNDHelperB
from .utils import isDominated, sweepA, splitA


def sorNDHelperA(fitnesses, obj, front):
    """Create a non-dominated sorting of S on the first M objectives"""
    if len(fitnesses) < 2:
        return
    elif len(fitnesses) == 2:
        # Only two individuals, compare them and adjust front number
        s1, s2 = fitnesses[0], fitnesses[1]
        if isDominated(s2[:obj + 1], s1[:obj + 1]):
            front[s2] = max(front[s2], front[s1] + 1)
    elif obj == 1:
        sweepA(fitnesses, front)
    elif len(frozenset(map(itemgetter(obj), fitnesses))) == 1:
        # All individuals for objective M are equal: go to objective M-1
        sorNDHelperA(fitnesses, obj - 1, front)
    else:
        # More than two individuals, split list and then apply recursion
        best, worst = splitA(fitnesses, obj)
        sorNDHelperA(best, obj, front)
        sorNDHelperB(best, worst, obj - 1, front)
        sorNDHelperA(worst, obj, front)
