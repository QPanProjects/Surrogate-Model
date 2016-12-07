import math

import numpy as np

from .mmphi import mmphi
from .perturb import perturb

"""
Evolutionary operation search for the most space filling Latin hypercube
of a certain size and dimensionality. There is no need to call this
directly - use bestlh.m

"""


# Authors: Quan Pan <quanpan302@hotmail.com>

def mmlhs(X_start, population, iterations, q):
    X_s = X_start.copy()

    n = np.size(X_s, 0)

    X_best = X_s

    Phi_best = mmphi(X_best)

    leveloff = math.floor(0.85 * iterations)

    for it in range(0, iterations):
        if it < leveloff:
            mutations = int(round(1 + (0.5 * n - 1) * (leveloff - it) / (leveloff - 1)))
        else:
            mutations = 1

        X_improved = X_best
        Phi_improved = Phi_best

        for offspring in range(0, population):
            X_try = perturb(X_best, mutations)
            Phi_try = mmphi(X_try, q)

            if Phi_try < Phi_improved:
                X_improved = X_try
                Phi_improved = Phi_try

        if Phi_improved < Phi_best:
            X_best = X_improved
            Phi_best = Phi_improved

    return X_best
