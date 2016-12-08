from surrogate.sampling.samRandomLHC import samRandomLHC

print '\nTest.sampling: samRandomLHC'
n = 3
k = 3
print '\tInput:  n=\t' + '\t' + str(n) + ''
print '\tInput:  k=\t' + '\t' + str(k) + ''
X = samRandomLHC(n=n, k=k)
print '\tOutput: X=\t' + '\t'.join(map(str, X)) + ''
