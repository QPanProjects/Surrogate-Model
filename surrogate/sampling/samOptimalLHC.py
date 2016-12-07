"""
Generates an optimized Latin hypercube by optimizing the Morris-Mitchell
criterion for a range of exponents and plots the first two dimensions of
the current hypercube throughout the optimization process.

Inputs:
    n - number of points required
    Population - number of individuals in the evolutionary operation
                 optimizer
    Iterations - number of generations the evolutionary operation
                 optimizer is run for
    Note: high values for the two inputs above will ensure high quality
    hypercubes, but the search will take longer.
    generation - if set to True, the LHC will be generated. If 'False,' the algorithm will check for an existing plan before generating.

Output:
    X - optimized Latin hypercube
"""


# Authors: Quan Pan <quanpan302@hotmail.com>

import os
import pickle

import numpy as np

from .samRLH import samRLH
from .utils import mmlhs, mmsort


# from surrogate.sampling.samRLH import samRLH
# from surrogate.sampling.utils import mmlhs, mmsort

def samOptimalLHC(n=2, k=2, population=30, iterations=30, generation=False):
    PATH = os.path.dirname(os.path.abspath(__file__)) + '/sampling_plans/'
    # print PATH

    if not generation:
        # Check for existing LHC sampling plans
        if os.path.isfile('{0}lhc_{1}_{2}.pkl'.format(PATH, k, n)):
            X = pickle.load(open('{0}lhc_{1}_{2}.pkl'.format(PATH, k, n), 'r'))
            return X
        else:
            print PATH + '\nSampling Plans not found on disk, generating it now.'

    # list of qs to optimise Phi_q for
    q = [1, 2, 5, 10, 20, 50, 100]

    # Set the distance norm to rectangular for a faster search. This can be
    # changed to p=2 if the Euclidean norm is required.
    p = 1

    # we start with a random Latin hypercube
    XStart = samRLH(n=n, k=k)

    X3D = np.zeros((n, k, len(q)))
    # for each q optimize Phi_q
    for i in xrange(len(q)):
        print ('Now_optimizing_for_q = %d' % q[i])

        X3D[:, :, i] = mmlhs(XStart, population, iterations, q[i])

    # sort according to the Morris-Mitchell criterion
    Index = mmsort(X3D, p)
    print ('Best_lh_found_using_q = %d' % q[Index[1]])

    # and the Latin hypercube with the best space-filling properties is

    X = X3D[:, :, Index[1]]
    pickle.dump(X, open('{0}lhc_{1}_{2}.pkl'.format(PATH, k, n), 'wb'))

    return X
