import numpy as np

from surrogate.mutation import mutPolynomialBounded

print '\nTest.mutation.mutPolynomialBounded: mutPolynomialBounded'
ind = np.array([x / 10.0 for x in range(0, 10, 1)])
print '\tInput:  ind=\t' + '\t'.join(map(str, ind)) + ''
out = mutPolynomialBounded(variable=ind.tolist())
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
