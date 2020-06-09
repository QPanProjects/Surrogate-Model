# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# pylint: disable=unused-import,g-bad-import-order
"""Classes and functions for building TensorFlow graphs.

## Core graph data structures

@@Graph
@@Operation
@@Tensor

## Tensor types

@@DType
@@as_dtype

## Utility functions

@@device
@@name_scope
@@control_dependencies
@@convert_to_tensor
@@convert_to_tensor_or_indexed_slices
@@get_default_graph
@@reset_default_graph
@@import_graph_def
@@load_op_library

## Graph collections

@@add_to_collection
@@get_collection
@@GraphKeys

## Defining new operations

@@RegisterGradient
@@NoGradient
@@RegisterShape
@@TensorShape
@@Dimension
@@op_scope
@@get_seed

## For libraries building on TensorFlow

@@register_tensor_conversion_function
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Classes used when building a Graph.

# Utilities used when building a Graph.

# Needed when you defined a new Op in C++.

# Needed when interfacing tensorflow to new array libraries

# pylint: disable=wildcard-import

# Load a TensorFlow plugin
# pylint: enable=wildcard-import
