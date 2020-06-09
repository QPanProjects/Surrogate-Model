# -*- coding: utf-8 -*-

# Author: Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
#         Vincent Dubourg <vincent.dubourg@gmail.com>
#         (mostly translation, see implementation details)
# Licence: BSD 3 clause

"""
The :mod:`sklearn.gaussian_process` module implements Gaussian Process
based regression and classification.
"""

from . import correlation_models
from . import kernels
from . import regression_models
from .gaussian_process import GaussianProcess
from .gpc import GaussianProcessClassifier
from .gpr import GaussianProcessRegressor

__all__ = ['GaussianProcess', 'correlation_models', 'regression_models',
           'GaussianProcessRegressor', 'GaussianProcessClassifier',
           'kernels']
