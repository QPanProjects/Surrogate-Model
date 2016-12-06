import unittest

from numpy import array, cos, pi

from surrogate.estimator.kriging import KrigingSurrogate
from surrogate.util.test import assert_rel_error


def branin(x):
    y = (x[1] - (5.1 / (4. * pi ** 2.)) * x[0] ** 2. + 5. * x[0] / pi - 6.) ** 2. + 10. * (1. - 1. / (8. * pi)) * cos(
        x[0]) + 10.
    return y


def branin_1d(x):
    return branin(array([x[0], 2.275]))


class TestKrigingSurrogate(unittest.TestCase):
    def test_1d_training(self):
        x = array([[0.0], [2.0], [3.0], [4.0], [6.0]])
        y = array([[branin_1d(case)] for case in x])

        surrogate = KrigingSurrogate()
        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu, sigma = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)
            assert_rel_error(self, sigma, 0, 1e-6)

    def test_2d(self):
        x = array([[-2., 0.], [-0.5, 1.5], [1., 3.], [8.5, 4.5], [-3.5, 6.], [4., 7.5], [-5., 9.], [5.5, 10.5],
                   [10., 12.], [7., 13.5], [2.5, 15.]])
        y = array([[branin(case)] for case in x])

        surrogate = KrigingSurrogate()
        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu, sigma = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)
            assert_rel_error(self, sigma, 0, 1e-6)

        mu, sigma = surrogate.predict([5., 5.])

        assert_rel_error(self, mu, branin([5., 5.]), 1e-1)
        assert_rel_error(self, sigma, 5.79, 1e-2)


if __name__ == "__main__":
    unittest.main()
