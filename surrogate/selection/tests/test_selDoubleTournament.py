from surrogate.selection.tests.test_individuals import Individuals

individuals = Individuals()

from surrogate.selection.selDoubleTournament import selDoubleTournament

print '\nTest.selection: selDoubleTournament'
print '\tInput:  ind=\t' + '\t'.join(map(str, individuals)) + ''
out = selDoubleTournament(individuals=list(individuals), k=2, fitness_first=True)
# out = selDoubleTournament(individuals=list(individuals), k=2, fitness_first=False)
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
