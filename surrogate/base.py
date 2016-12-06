"""Base classes for all estimators."""

# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02


##############################################################################
"""
Class definition for Individual, the base class for all surrogate models.
"""

class Individual:
    def __init__(self, variable, fitness, constrain):
        self.variable = variable
        self.fitness = fitness
        self.constrain = constrain

        self.rank = None
        self.distance = None
        self.strategy = set()
        self.solution = set()
        self.feature = None
        self.objective = None
        self.dominate = None


    # def __len__(self):
    #     return len(self.variable)

    def __repr__(self):
        return repr((self.variable, self.fitness, self.constrain))


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
        raise NotImplementedError()

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
