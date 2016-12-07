import numpy as np


# Authors: Quan Pan <quanpan302@hotmail.com>

def ismember(A, B):
    return [np.sum(a == B) for a in A]
