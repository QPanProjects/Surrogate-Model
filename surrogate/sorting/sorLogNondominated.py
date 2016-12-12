from collections import defaultdict

from .sorNDHelperA import sorNDHelperA


def sorLogNondominated(individuals, k, first_front_only=False):
    """Sort *individuals* in pareto non-dominated fronts using the Generalized
    Reduced Run-Time Complexity Non-Dominated Sorting Algorithm presented by
    Fortin et al. (2013).

    :param individuals: A list of individuals to select from.
    :returns: A list of Pareto fronts (lists), with the first list being the
              true Pareto front.
    """
    if k == 0:
        return []

    # Separate individuals according to unique fitnesses
    unique_fits = defaultdict(list)
    for i, ind in enumerate(individuals):
        unique_fits[ind.fitness.wvalues].append(ind)

    # Launch the sorting algorithm
    obj = len(individuals[0].fitness.wvalues) - 1
    fitnesses = unique_fits.keys()
    front = dict.fromkeys(fitnesses, 0)

    # Sort the fitnesses lexicographically.
    fitnesses.sort(reverse=True)
    sorNDHelperA(fitnesses, obj, front)

    # Extract individuals from front list here
    nbfronts = max(front.values()) + 1
    pareto_fronts = [[] for i in range(nbfronts)]
    for fit in fitnesses:
        index = front[fit]
        pareto_fronts[index].extend(unique_fits[fit])

    # Keep only the fronts required to have k individuals.
    if not first_front_only:
        count = 0
        for i, front in enumerate(pareto_fronts):
            count += len(front)
            if count >= k:
                return pareto_fronts[:i + 1]
        return pareto_fronts
    else:
        return pareto_fronts[0]
