"""Base classes for all estimators."""

# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02


##############################################################################

class Individual:
    def __init__(self, variable, fitness, constrain):
        self.variable = variable
        self.fitness = fitness
        self.constrain = constrain

    def __repr__(self):
        return repr((self.variable, self.fitness, self.constrain))
