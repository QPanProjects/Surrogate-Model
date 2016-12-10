"""Base classes for all estimators."""

# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02


##############################################################################
"""
Class definition for Individual, the base class for all surrogate models.
"""


# class Individual:
class Individual(object):
    def __init__(self, estimator, variable=None, objective=None, constraint=None, *args, **kwargs):
        """
        Optimization Problem Class Individual

        *Arguments:
        - opt_func -> FUNC: Objective function

        **Keyword arguments:
        - var_set -> INST: Variable set, *Default* = None
        - obj_set -> INST: Objective set, *Default* = None
        - con_set -> INST: Constraints set, *Default* = None

        def ObjFunction(fun, *args, **kwargs):
            return fun(*args, **kwargs)
        """

        # needed
        self.estimator = estimator

        if variable is None:
            self.variable = {}
        else:
            self.variable = variable

        if objective is None:
            self.objective = {}
        else:
            self.objective = objective

        if constraint is None:
            self.constraint = {}
        else:
            self.constraint = constraint

        self.solution = {}

        # not yet decided
        # self.fitness = None
        # self.rank = None
        # self.distance = None
        # self.strategy = set()
        # self.solution = set()
        # self.feature = None
        # self.dominate = None

    def getVar(self, i):
        if not (isinstance(i, int) and i >= 0):
            raise ValueError("Variable index must be an integer >= 0 .")
        return self._variables[i]

    # def __len__(self):
    #     return len(self.variable)
        # def __repr__(self):
        #     return repr((self.variable, self.objective, self.constraint, self.fitness))


##############################################################################
"""
Class definition for SurrogateModel, the base class for all surrogate models.
"""


class SurrogateModel(object):
    """
    Base class for surrogate models.
    """

    def __init__(self):
        self.trained = False

    def fit(self, x, y):
        self.trained = True

    def predict(self, x):
        if not self.trained:
            msg = "{0} has not been trained, so no prediction can be made." \
                .format(type(self).__name__)
            raise RuntimeError(msg)

    def predict_proba(self, x):
        if not self.trained:
            msg = "{0} has not been trained, so no prediction can be made." \
                .format(type(self).__name__)
            raise RuntimeError(msg)
            # raise NotImplementedError('predict_proba not implemented.')

    def linearize(self, x):
        msg = "{0} has not defined a jacobian method." \
            .format(type(self).__name__)
        raise RuntimeError(msg)


class MultiFiSurrogateModel(SurrogateModel):
    """
    Base class for surrogate models using multi-fiddelity training data
    """

    def fit(self, x, y):
        super(MultiFiSurrogateModel, self).train(x, y)
        self.train_multifi([x], [y])

    def train_multifi(self, x, y):
        """Trains the surrogate model, based on the given
        multi-fidelity training data.

        x: list of (m samples, n inputs) ndarrays
            Values representing the multi-fidelity training case inputs.
        y: list of ndarray
            output training values which corresponds to the multi-fidelity
            training case input given by x.
        """
