from surrogate.mutation import mutFlipBit

print '\nTest.mutation.mutFlipBit: mutFlipBit'
ind = [x / 10.0 for x in range(0, 10, 1)]
print '\tInput:  ind=\t' + '\t'.join(map(str, ind)) + ''
out = mutFlipBit(individual=list(ind))
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
