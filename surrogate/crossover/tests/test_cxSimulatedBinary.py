from surrogate.crossover import cxSimulatedBinary

print '\nTest.crossover.cxSimulatedBinary: cxSimulatedBinary'
ind1 = range(0, 10)
ind2 = range(9, -1, -1)
# ind1 = np.array(range(0, 10))
# # ind2 = np.array(range(10, 20))
# ind2 = np.array(range(9, -1, -1))
print '\tInput:  ind1_desVar=\t' + '\t'.join(map(str, ind1)) + ''
print '\tInput:  ind2_desVar=\t' + '\t'.join(map(str, ind2)) + ''
[out1, out2] = cxSimulatedBinary(var1=ind1, var2=ind2)
print '\tOutput: out1_desVar=\t' + '\t'.join(map(str, out1)) + ''
print '\tOutput: out2_desVar=\t' + '\t'.join(map(str, out2)) + ''
