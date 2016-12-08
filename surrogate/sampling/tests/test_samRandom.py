from surrogate.sampling.samRandom import *

print '\nsampling.samRandom.samRandom'
d0, d1 = 3, 2
print samRandom(d0, d1)

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

print '\nsampling.samRandom.samF'
dfnum, dfden, size = 1, 48, 10
print samF(dfnum, dfden, size)

print '\nsampling.samRandom.samGamma'
shape, scale, size = 2.0, 2.0, 10
print samGamma(shape, scale, size)

print '\nsampling.samRandom.samGumbel'
# mu, beta = 0, 0.1
loc, scale, size = 0, 0.1, 10
print samGumbel(loc, scale, size)

print '\nsampling.samRandom.samLaplace'
loc, scale, size = 0.0, 1.0, 10
print samLaplace(loc, scale, size)

print '\nsampling.samRandom.samLogistic'
loc, scale, size = 10, 1, 10
print samLogistic(loc, scale, size)

print '\nsampling.samRandom.samLognormal'
mean, sigma, size = 3.0, 1.0, 10
print samLognormal(mean, sigma, size)

print '\nsampling.samRandom.samNormal'
# mu, sigma = 0, 0.1
loc, scale, size = 0, 0.1, 10
print samNormal(loc, scale, size)

print '\nsampling.samRandom.samPareto'
a, size = 3.0, 10
print samPareto(a, size)

print '\nsampling.samRandom.samPoisson'
lam, size = 3.0, 10
print samPoisson(lam, size)

print '\nsampling.samRandom.samPower'
a, size = 3.0, 10
print samPower(a, size)

print '\nsampling.samRandom.samRayleigh'
scale, size = 3.0, 10
print samRayleigh(scale, size)

print '\nsampling.samRandom.samTriangular'
left, mode, right, size = -3, 0, 8, 10
print samTriangular(left, mode, right, size)

print '\nsampling.samRandom.samUniform'
low, high, size = 0.0, 1.0, 10
print samUniform(low, high, size)

print '\nsampling.samRandom.samVonmises'
mu, kappa, size = 0.0, 4.0, 10
print samVonmises(mu, kappa, size)

print '\nsampling.samRandom.samWald'
mean, scale, size = 3, 2, 10
print samWald(mean, scale, size)

print '\nsampling.samRandom.samWeibull'
a, size = 5.0, 10
print samWeibull(a, size)

print '\nsampling.samRandom.samZipf'
a, size = 2.0, 10
print samZipf(a, size)

print '\nnumpy.random'
import numpy as np

print np.random.f(dfnum=1, dfden=48, size=10)
print np.random.pareto(3.0, 10)
print np.random.triangular(-3, 0, 8, 10)
