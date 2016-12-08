"""Sampling Strategy, Experimental Design
Links:
    https://www.google.nl/search?sclient=psy-ab&client=safari&rls=en&q=github+sampling+python&oq=github+sampling+python&gs_l=serp.3..0i22i30k1l2.2824.3846.0.4517.7.7.0.0.0.0.91.551.7.7.0....0...1c.1.64.psy-ab..0.7.538...33i160k1.G42G3jxX1XY&pbx=1&biw=1680&bih=961&dpr=2&cad=cbv&bvch=u&sei=-e5HWNLGHsrNgAbDjruoAg#q=github+sampling+strategy+python

    https://en.wikipedia.org/wiki/Sampling_(statistics)

    https://en.wikipedia.org/wiki/Latin_hypercube_sampling

    https://docs.scipy.org/doc/numpy/reference/routines.random.html
"""


from .samOptimalLHC import samOptimalLHC
from .samRLH import samRLH

__all__ = [
    'samRLH',
    'samOptimalLHC'
]
