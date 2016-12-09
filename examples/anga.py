""" Adaptive Neural Network Genetic Algorithm (ANGA)
Components:
    Genetic Algorithm
    Artificial Neural Networks
    Caching
Implementation:
    Fitness Sampling
        Sampling Rate: Sampling rate determines how many individuals should be sampled from a population in each generation
        Sampling Selection Strategy: Sampling selection strategy determines which individuals should be sampled from a population, given the current sampling rate.
            random sampling, best sampling, tournament sampling, combined tournament+best sampling
    ANN Training and Retraining
        InitialTrainingGenerations: Alloftheindividualsin the first several generations of ANGA must be evaluated by the simulation models to generate the ANN training set.
        Retraining Set Management: As more and more sampled solutions are generated from simulation model evaluations, the retraining set must be managed.
            growing set approach, fixed set approach
        Retraining Method: When the ANNs need to be retrained, the training algorithm can either load the previ- ously trained weights and continue the training episodes on the new training set, or it can re-initialize the ANN weights to random values and completely retrain the ANNs.
        Retraining Frequency: Retraining frequency deter- mines when the ANNs should be updated during an ANGA run. Retraining frequency should decrease in later gener- ations as the search progresses into relatively smoother local regions.
"""

import warnings

from sklearn.neural_network import MLPRegressor

from surrogate.estimator.neural_network import ANNSurrogate

warnings.filterwarnings(action="ignore", category=Warning)

if __name__ == "__main__":
    Xpool_ind = [[0., 0.], [1., 1.], [10., 10.]]
    Ypool_obj = [0.0, 1.0, 10.0]
    x_pred = [[5., 5.], [-10., -2.]]

    surrogate = ANNSurrogate(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    surrogate.fit(Xpool_ind, Ypool_obj)
    y_pred = surrogate.predict(Xpool_ind)
    # print surrogate.regressor
    print y_pred

    regressor = MLPRegressor(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    regressor.fit(Xpool_ind, Ypool_obj)
    y_pred = regressor.predict(Xpool_ind)
    # print regressor
    print y_pred

# from surrogate.base import SurrogateModel
# class ANGA(object):
# class ANGA(SurrogateModel):
#     def __init__(self, x, y):
#         super(ANGA, self).__init__()
#
#         self.x = x
#         self.y = y
#
#     def predict_proba(self, x):
#         super(ANGA, self).predict_proba(x)
#         pass
#
#
# if __name__ == "__main__":
#     from sklearn import datasets
#
#     iris = datasets.load_iris()
#     X, y = iris.data, iris.target
#
#     # def branin(x):
#     #     y = (x[1] - (5.1 / (4. * pi ** 2.)) * x[0] ** 2. + 5. * x[0] / pi - 6.) ** 2. + 10. * (
#     #     1. - 1. / (8. * pi)) * cos(
#     #         x[0]) + 10.
#     #     return y
#     # def branin_1d(x):
#     #     return branin(array([x[0], 2.275]))
#     # X = array([[0.0], [2.0], [3.0], [4.0], [6.0]])
#     # y = array([[branin_1d(case)] for case in X])
#
#     anga = ANGA(X, y)
#     anga.fit(X, y)
#     anga.predict_proba(X)
