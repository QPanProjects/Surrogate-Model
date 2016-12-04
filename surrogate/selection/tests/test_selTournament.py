from surrogate.selection.tests.test_individuals import Individuals

individuals = Individuals()

from surrogate.selection.selTournament import selTournament

print '\nTest.selection: selTournament'
print '\tInput:  ind=\t' + '\t'.join(map(str, individuals)) + ''
out = selTournament(individuals=list(individuals), k=2, tournsize=5)
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
