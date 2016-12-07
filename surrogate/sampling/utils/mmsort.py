import numpy as np

from .mm import mm

"""
Ranks sampling plans according to the Morris-Mitchell criterion definition.
Note: similar to phisort, which uses the numerical quality criterion Phiq
as a basis for the ranking.

Inputs:
    X3D - three-dimensional array containing the sampling plans to be ranked.
    p - the distance metric to be used (p=1 rectangular - default, p=2 Euclidean)

Output:
    Index - index array containing the ranking

"""


# Authors: Quan Pan <quanpan302@hotmail.com>

def mmsort(X3D, p=1):
    # Pre-allocate memory
    Index = np.arange(np.size(X3D, axis=2))

    # Bubble-sort
    swap_flag = 1

    while swap_flag == 1:
        swap_flag = 0
        i = 1
        while i <= len(Index) - 2:
            if mm(X3D[:, :, Index[i]], X3D[:, :, Index[i + 1]], p) == 2:
                arrbuffer = Index[i]
                Index[i] = Index[i + 1]
                Index[i + 1] = arrbuffer
                swap_flag = 1
            i = i + 1
        return Index
