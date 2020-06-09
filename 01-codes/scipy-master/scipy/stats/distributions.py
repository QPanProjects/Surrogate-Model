#
# Author:  Travis Oliphant  2002-2011 with contributions from
#          SciPy Developers 2004-2011
#
# NOTE: To look at history using `git blame`, use `git blame -M -C -C`
#       instead of `git blame -Lxxx,+x`.
#
from __future__ import division, print_function, absolute_import

from . import _continuous_distns
from . import _discrete_distns

# For backwards compatibility e.g. pymc expects distributions.__all__.
__all__ = ['entropy', 'rv_discrete', 'rv_continuous']

# Add only the distribution names, not the *_gen names.
__all__ += _continuous_distns._distn_names
__all__ += _discrete_distns._distn_names
