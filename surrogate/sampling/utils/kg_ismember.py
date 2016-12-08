# Authors: Quan Pan <quanpan302@hotmail.com>

import numpy as np

def ismember(A, B):
    return [np.sum(a == B) for a in A]
