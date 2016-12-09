from surrogate.sampling import samOptimalLHC

print '\nTest sampling.samOptimalLHC: samOptimalLHC'
n = 3
k = 3
print '\tInput:  n=\t' + '\t' + str(n) + ''
print '\tInput:  k=\t' + '\t' + str(k) + ''
X = samOptimalLHC(n=n, k=k, population=30, iterations=30, generation=False)
print '\tOutput: X=\t' + '\t'.join(map(str, X)) + ''
