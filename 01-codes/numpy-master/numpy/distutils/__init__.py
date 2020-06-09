from __future__ import division, absolute_import, print_function

# Must import local ccompiler ASAP in order to get
# customized CCompiler.spawn effective.

# If numpy is installed, add distutils.test()
try:
    from . import __config__
    # Normally numpy is installed if the above import works, but an interrupted
    # in-place build could also have left a __config__.py.  In that case the
    # next import may still fail, so keep it inside the try block.
    from numpy.testing.nosetester import _numpy_tester

    test = _numpy_tester().test
except ImportError:
    pass
