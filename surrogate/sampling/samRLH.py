import numpy as np

"""
Generates a random latin hypercube within the [0,1]^k hypercube

Inputs:
    n-desired number of points
    k-number of design variables (dimensions)
    Edges-if Edges=1 the extreme bins will have their centers on the edges of the domain

Outputs:
    Latin hypercube sampling plan of n points in k dimensions
 """


# Authors: Quan Pan <quanpan302@hotmail.com>

def samRLH(n=2, k=2, Edges=0):
    # pre-allocate memory
    X = np.zeros((n, k))

    # exclude 0

    for i in xrange(0, k):
        X[:, i] = np.transpose(np.random.permutation(np.arange(1, n + 1, 1)))

    if Edges == 1:
        X = (X - 1) / (n - 1)
    else:
        X = (X - 0.5) / n

    return X
