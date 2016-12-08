from surrogate.sampling.samFullFact import *

print '\nsampling.samFullFact.samFullFact'
print samFullFact([2, 4, 3])
print '\nsampling.samFullFact.samFF2n'
print samFF2n(3)
print '\nsampling.samFullFact.samFracFact'
print 'a b ab'
print samFracFact("a b ab")
print 'A B AB'
print samFracFact("A B AB")
print 'a b -ab c +abc'
print samFracFact("a b -ab c +abc")
