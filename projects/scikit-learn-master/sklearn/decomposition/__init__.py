"""
The :mod:`sklearn.decomposition` module includes matrix decomposition
algorithms, including among others PCA, NMF or ICA. Most of the algorithms of
this module can be regarded as dimensionality reduction techniques.
"""

from .dict_learning import (dict_learning, dict_learning_online, sparse_encode,
                            DictionaryLearning, MiniBatchDictionaryLearning,
                            SparseCoder)
from .factor_analysis import FactorAnalysis
from .fastica_ import FastICA, fastica
from .incremental_pca import IncrementalPCA
from .kernel_pca import KernelPCA
from .nmf import NMF, ProjectedGradientNMF, non_negative_factorization
from .online_lda import LatentDirichletAllocation
from .pca import PCA, RandomizedPCA
from .sparse_pca import SparsePCA, MiniBatchSparsePCA
from .truncated_svd import TruncatedSVD
from ..utils.extmath import randomized_svd

__all__ = ['DictionaryLearning',
           'FastICA',
           'IncrementalPCA',
           'KernelPCA',
           'MiniBatchDictionaryLearning',
           'MiniBatchSparsePCA',
           'NMF',
           'PCA',
           'ProjectedGradientNMF',
           'RandomizedPCA',
           'SparseCoder',
           'SparsePCA',
           'dict_learning',
           'dict_learning_online',
           'fastica',
           'non_negative_factorization',
           'randomized_svd',
           'sparse_encode',
           'FactorAnalysis',
           'TruncatedSVD',
           'LatentDirichletAllocation']
