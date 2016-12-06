from .kriging import KrigingSurrogate, FloatKrigingSurrogate
from .nearest_neighbor import NearestNeighbor
from .response_surface import ResponseSurface

__all__ = [
    'KrigingSurrogate', 'FloatKrigingSurrogate',
    'ResponseSurface',
    'NearestNeighbor'
]
