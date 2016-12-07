"""
Test for single criteria EI example.
"""
import logging
import os.path
import random
import unittest

from numpy import pi
from openmdao.examples.expected_improvement.single_objective_ei import Analysis
from openmdao.main.api import set_as_top
from pyevolve import Selectors


class SingleObjectiveEITest(unittest.TestCase):
    """Test to make sure the EI sample problem works as it should"""

    def tearDown(self):
        if os.path.exists('adapt.csv'):
            os.remove('adapt.csv')

    def test_EI(self):

        random.seed(0)

        # pyevolve does some caching that causes failures during our
        # complete unit tests due to stale values in the cache attributes
        # below, so reset them here
        Selectors.GRankSelector.cachePopID = None
        Selectors.GRankSelector.cacheCount = None
        Selectors.GRouletteWheel.cachePopID = None
        Selectors.GRouletteWheel.cacheWheel = None

        analysis = Analysis()
        set_as_top(analysis)
        # analysis.DOE_trainer.DOEgenerator = FullFactorial(num_levels=10)

        analysis.run()
        # This test looks for the presence of at least one point close to
        # each optimum.

        print analysis.ei.EI
        print analysis.meta.x
        print analysis.meta.y

        points = [(-pi, 12.275, .39789), (pi, 2.275, .39789), (9.42478, 2.745, .39789)]
        errors = []
        for x, y, z in points:
            analysis.meta.x = x
            analysis.meta.y = y
            analysis.meta.execute()

            errors.append(abs((analysis.meta.f_xy.mu - z) / z * 100))
        avg_error = sum(errors) / float(len(errors))
        logging.info('#errors %s, sum(errors) %s, avg_error %s',
                     len(errors), sum(errors), avg_error)
        self.assertTrue(avg_error <= 35)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
