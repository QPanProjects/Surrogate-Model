import numpy as np

from surrogate.mutation import mutGaussian

print '\nTest.mutation.mutGaussian: mutGaussian'
ind = np.array([x / 10.0 for x in range(0, 10, 1)])
print '\tInput:  ind=\t' + '\t'.join(map(str, ind)) + ''
out = mutGaussian(variable=ind)
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
