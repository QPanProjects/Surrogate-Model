from ..cxOnePoint import cxOnePoint

print '\nTest.crossover: cxOnePoint'
ind1_desVar = range(0, 10)
ind2_desVar = range(10, 20)
# ind2_desVar = range(9,-1,-1)
print '\tInput:  ind1_desVar=\t' + '\t'.join(map(str, ind1_desVar)) + ''
print '\tInput:  ind2_desVar=\t' + '\t'.join(map(str, ind2_desVar)) + ''
[out1_desVar, out2_desVar] = cxOnePoint(ind1=list(ind1_desVar), ind2=list(ind2_desVar), parameter=param)
print '\tOutput: out1_desVar=\t' + '\t'.join(map(str, out1_desVar)) + ''
print '\tOutput: out2_desVar=\t' + '\t'.join(map(str, out2_desVar)) + ''
