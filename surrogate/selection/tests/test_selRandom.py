from surrogate.selection.selRandom import selRandom

print '\nTest.selection: mutFlselRandomipBit'
ind = [x / 10.0 for x in range(0, 10, 1)]
print '\tInput:  ind=\t' + '\t'.join(map(str, ind)) + ''
out = selRandom(individuals=list(ind), k=5)
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
