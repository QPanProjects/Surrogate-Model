import math

import numpy as np

"""
Interchanges pairs of randomly chosen elements within randomly
chosen columns of a sampling plan a number of times. If the plan is
a Latin hypercube, the result of this operation will also be a Latin
hypercube.

Inputs:
    X - sampling plan
    PertNum - the number of changes (perturbations) to be made to X.
Output:
    X - perturbed sampling plan

"""


# Authors: Quan Pan <quanpan302@hotmail.com>

def perturb(X, PertNum):
    X_pert = X.copy()
    [n, k] = np.shape(X_pert)

    for pert_count in range(0, PertNum):
        col = math.floor(np.random.rand(1) * k)

        # Choosing two distinct random points
        el1 = 0
        el2 = 0
        while el1 == el2:
            el1 = math.floor(np.random.rand(1) * n)
            el2 = math.floor(np.random.rand(1) * n)

        # swap the two chosen elements
        arrbuffer = X_pert[el1, col]
        X_pert[el1, col] = X_pert[el2, col]
        X_pert[el2, col] = arrbuffer

    return X_pert
