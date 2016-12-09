from surrogate.sampling import *

print '\nTest sampling.samFullFact: samFullFact'
print samFullFact([2, 4, 3])
print '\nTest sampling.samFullFact: samFF2n'
print samFF2n(3)
print '\nTest sampling.samFullFact: samFracFact'
print 'a b ab'
print samFracFact("a b ab")
print 'A B AB'
print samFracFact("A B AB")
print 'a b -ab c +abc'
print samFracFact("a b -ab c +abc")
