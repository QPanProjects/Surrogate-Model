from surrogate.selection.tests.test_individuals import Individuals

individuals = Individuals()

from surrogate.selection import selWorst

print '\nTest selection.selWorst: selWorst'
print '\tInput:  ind=\t' + '\t'.join(map(str, individuals)) + ''
out = selWorst(individuals=list(individuals), k=2)
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
