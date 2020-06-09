"""
The :mod:`sklearn.ensemble` module includes ensemble-based methods for
classification, regression and anomaly detection.
"""

from . import bagging
from . import forest
from . import gradient_boosting
from . import partial_dependence
from . import weight_boosting
from .bagging import BaggingClassifier
from .bagging import BaggingRegressor
from .base import BaseEnsemble
from .forest import ExtraTreesClassifier
from .forest import ExtraTreesRegressor
from .forest import RandomForestClassifier
from .forest import RandomForestRegressor
from .forest import RandomTreesEmbedding
from .gradient_boosting import GradientBoostingClassifier
from .gradient_boosting import GradientBoostingRegressor
from .iforest import IsolationForest
from .voting_classifier import VotingClassifier
from .weight_boosting import AdaBoostClassifier
from .weight_boosting import AdaBoostRegressor

__all__ = ["BaseEnsemble",
           "RandomForestClassifier", "RandomForestRegressor",
           "RandomTreesEmbedding", "ExtraTreesClassifier",
           "ExtraTreesRegressor", "BaggingClassifier",
           "BaggingRegressor", "IsolationForest", "GradientBoostingClassifier",
           "GradientBoostingRegressor", "AdaBoostClassifier",
           "AdaBoostRegressor", "VotingClassifier",
           "bagging", "forest", "gradient_boosting",
           "partial_dependence", "weight_boosting"]
