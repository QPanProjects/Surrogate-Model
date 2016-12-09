# import itertools
# import unittest
#
# from numpy import array, linspace, sin, cos, pi

from sklearn.neural_network import MLPRegressor

from surrogate.estimator import ANNSurrogate

if __name__ == "__main__":
    X = [[0., 0.], [1., 1.], [10., 10.]]
    y = [0.0, 1.0, 10.0]
    x_pred = [[5., 5.], [-10., -2.]]

    surrogate = ANNSurrogate(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    surrogate.fit(X, y)
    y_pred = surrogate.predict(X)
    # print surrogate.regressor
    # print y_pred

    regressor = MLPRegressor(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    regressor.fit(X, y)
    y_pred = regressor.predict(X)
    print regressor
    print y_pred
