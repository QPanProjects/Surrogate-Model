from surrogate.mutation import mutShuffleIndexes

print '\nTest.mutation.mutShuffleIndexes: mutShuffleIndexes'
ind = [x / 10.0 for x in range(0, 10, 1)]
print '\tInput:  ind=\t' + '\t'.join(map(str, ind)) + ''
out = mutShuffleIndexes(individual=list(ind))
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
