import numpy as np

from surrogate.mutation import mutUniformInt

print '\nTest.mutation.mutUniformInt: mutUniformInt'
ind = np.array([x / 10.0 for x in range(0, 10, 1)])
print '\tInput:  ind=\t' + '\t'.join(map(str, ind)) + ''
out = mutUniformInt(variable=ind.tolist())
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
