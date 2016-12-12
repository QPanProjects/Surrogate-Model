# import sys
# sys.path.append("..")
# from cxBlend import cxBlend
import numpy as np

from surrogate.crossover import cxBlend

print '\nTest.crossover.cxBlend: cxBlend'
ind1 = np.array(range(0, 10))
ind2 = np.array(range(10, 20))
# ind2 = range(9,-1,-1)
print '\tInput:  ind1_desVar=\t' + '\t'.join(map(str, ind1)) + ''
print '\tInput:  ind2_desVar=\t' + '\t'.join(map(str, ind2)) + ''
[out1, out2] = cxBlend(var1=ind1.tolist(), var2=ind2.tolist())
print '\tOutput: out1_desVar=\t' + '\t'.join(map(str, out1)) + ''
print '\tOutput: out2_desVar=\t' + '\t'.join(map(str, out2)) + ''
