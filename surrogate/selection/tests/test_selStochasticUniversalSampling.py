from surrogate.selection.tests.test_individuals import Individuals

individuals = Individuals()

from surrogate.selection.selStochasticUniversalSampling import selStochasticUniversalSampling

print '\nTest.selection: selStochasticUniversalSampling'
print '\tInput:  ind=\t' + '\t'.join(map(str, individuals)) + ''
out = selStochasticUniversalSampling(individuals=list(individuals), k=2)
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
