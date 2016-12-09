from .kriging import KrigingSurrogate, FloatKrigingSurrogate
from .nearest_neighbor import NNeighborSurrogate
from .neural_network import ANNSurrogate
from .response_surface import RSurfaceSurrogate

__all__ = [
    'KrigingSurrogate', 'FloatKrigingSurrogate',
    'RSurfaceSurrogate',
    'NNeighborSurrogate',
    'ANNSurrogate'
]
