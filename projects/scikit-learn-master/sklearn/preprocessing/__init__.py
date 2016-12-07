"""
The :mod:`sklearn.preprocessing` module includes scaling, centering,
normalization, binarization and imputation methods.
"""

from ._function_transformer import FunctionTransformer
from .data import Binarizer
from .data import KernelCenterer
from .data import MaxAbsScaler
from .data import MinMaxScaler
from .data import Normalizer
from .data import OneHotEncoder
from .data import PolynomialFeatures
from .data import RobustScaler
from .data import StandardScaler
from .data import add_dummy_feature
from .data import binarize
from .data import maxabs_scale
from .data import minmax_scale
from .data import normalize
from .data import robust_scale
from .data import scale
from .imputation import Imputer
from .label import LabelBinarizer
from .label import LabelEncoder
from .label import MultiLabelBinarizer
from .label import label_binarize

__all__ = [
    'Binarizer',
    'FunctionTransformer',
    'Imputer',
    'KernelCenterer',
    'LabelBinarizer',
    'LabelEncoder',
    'MultiLabelBinarizer',
    'MinMaxScaler',
    'MaxAbsScaler',
    'Normalizer',
    'OneHotEncoder',
    'RobustScaler',
    'StandardScaler',
    'add_dummy_feature',
    'PolynomialFeatures',
    'binarize',
    'normalize',
    'scale',
    'robust_scale',
    'maxabs_scale',
    'minmax_scale',
    'label_binarize',
]
