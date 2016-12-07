"""
The :mod:`sklearn.neural_network` module includes models based on neural
networks.
"""

# Licence: BSD 3 clause

from .multilayer_perceptron import MLPClassifier
from .multilayer_perceptron import MLPRegressor
from .rbm import BernoulliRBM

__all__ = ["BernoulliRBM",
           "MLPClassifier",
           "MLPRegressor"]
