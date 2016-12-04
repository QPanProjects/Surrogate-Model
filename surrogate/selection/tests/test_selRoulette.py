from surrogate.selection.tests.test_individuals import Individuals

individuals = Individuals()

from surrogate.selection.selRoulette import selRoulette

print '\nTest.selection: selRoulette'
print '\tInput:  ind=\t' + '\t'.join(map(str, individuals)) + ''
out = selRoulette(individuals=list(individuals), k=2)
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
