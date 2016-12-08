from surrogate.sampling.samRandom import *

print '\nsampling.samRandom.samRandom'
print samRandom(3, 2)

print '\nsampling.samRandom.samBeta'
a, b, size = 0.1, 0.5, 10
print samBeta(a, b, size)

print '\nsampling.samRandom.samBinomial'
n, p, size = 10, 0.5, 10
print samBinomial(n, p, size)

print '\nsampling.samRandom.samChiSquare'
df, size = 2, 10
print samChiSquare(df, size)

print '\nsampling.samRandom.samExponential'
scale, size = 0.2, 10
print samExponential(scale, size)
