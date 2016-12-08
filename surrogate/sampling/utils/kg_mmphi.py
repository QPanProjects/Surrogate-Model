"""
Calculates the sampling plan quality criterion of Morris and Mitchell

Inputs:
    X - Sampling plan
    q - exponent used in the calculation of the metric (default = 2)
    p - the distance metric to be used (p=1 rectangular - default , p=2 Euclidean)

Output:
    Phiq - sampling plan 'space-fillingness' metric
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

import numpy as np

from .kg_jd import jd

def mmphi(X, q=2, p=1):
    # calculate the distances between all pairs of
    # points (using the p-norm) and build multiplicity array J
    J, d = jd(X, p)
    # the sampling plan quality criterion
    Phiq = (np.sum(J * (d ** (-q)))) ** (1.0 / q)
    return Phiq
