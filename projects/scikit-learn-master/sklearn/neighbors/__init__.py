"""
The :mod:`sklearn.neighbors` module implements the k-nearest neighbors
algorithm.
"""

from .approximate import LSHForest
from .classification import KNeighborsClassifier, RadiusNeighborsClassifier
from .graph import kneighbors_graph, radius_neighbors_graph
from .kde import KernelDensity
from .nearest_centroid import NearestCentroid
from .regression import KNeighborsRegressor, RadiusNeighborsRegressor
from .unsupervised import NearestNeighbors

__all__ = ['BallTree',
           'DistanceMetric',
           'KDTree',
           'KNeighborsClassifier',
           'KNeighborsRegressor',
           'NearestCentroid',
           'NearestNeighbors',
           'RadiusNeighborsClassifier',
           'RadiusNeighborsRegressor',
           'kneighbors_graph',
           'radius_neighbors_graph',
           'KernelDensity',
           'LSHForest']
