from surrogate.sampling.samRLH import samRLH

print '\nTest.sampling: samRLH'
n = 2
k = 20
print '\tInput:  n=\t' + '\t' + str(n) + ''
print '\tInput:  k=\t' + '\t' + str(k) + ''
X = samRLH(n=n, k=k)
print '\tOutput: X=\t' + '\t'.join(map(str, X)) + ''
