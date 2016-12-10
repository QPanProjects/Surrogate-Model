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


import warnings
warnings.filterwarnings(action="ignore", category=Warning)
# warnings.filterwarnings(action="ignore", category=FutureWarning)
# warnings.filterwarnings(action="ignore", category=ImportWarning)
# warnings.filterwarnings(action="ignore", category=DeprecationWarning)


from surrogate.base import Individual
from surrogate.sampling import samRandom, samBeta
from surrogate.estimator import ANNSurrogate
from surrogate.benchmarks import zdt6


if __name__ == "__main__":
    _INF = 1e-14
    _Ndim = 10


    # Xold_ind = [[0., 0., 0., 0.], [1., 1., 1., 1.], [10., 10., 10., 10.]]
    # # Yold_obj = [0.0, 1.0, 10.0]
    # Yold_obj = [[0., 0.], [1., 1.], [10., 10.]]
    # Xnew_ind = [[5., 5., 5., 5.], [-10., -2., -10., -2.]]

    # def Population(n=10, samStrategry):
    def Population(n=10):
        Individuals = []
        estimator = zdt6
        for i in range(_Ndim):
            variable = samRandom(n=10)
            # variable = samBeta(a=0.1, b=0.1, size=10)
            objective = estimator(variable)
            constraint = []
            fitness = _INF
            Individuals.append(Individual(estimator, variable, objective, constraint))
        return Individuals


    def moeaLoop(surrogate, population):
        Xold_ind = []
        Yold_obj = []
        Xnew_ind = samBeta(a=0.1, b=0.1, size=_Ndim)
        for i in range(_Ndim):
            population[i].objective = population[i].estimator(population[i].variable)

            Xold_ind.append(population[i].variable)
            Yold_obj.append(population[i].objective)
            print str(i) + '.Xold_ind: [' + ', '.join(
                map("{:.5f}".format, population[i].variable)) + ']' + '\tYold_obj: [' + ', '.join(
                map("{:.5f}".format, population[i].objective)) + ']'
        surrogate.fit(Xold_ind, Yold_obj)
        Ynew_obj = surrogate.predict(Xnew_ind)
        # print '  Xnew_ind:\t['+'\t'.join(['{:.5f}'.format(num) for num in Xnew_ind])+']'+'\tYnew_obj:\t['+'\t'.join(['{:.5f}'.format(num) for num in Ynew_obj])+']'
        print 'ANNSurrogate.Xnew_ind:\n\t[' + '\t'.join(map(str, Xnew_ind)) + ']'
        print 'ANNSurrogate.Ynew_obj:\n\t[' + '\t'.join(map(str, Ynew_obj)) + ']'


    population = Population()
    print 'zdt6(samRandom(n=' + str(_Ndim) + ')):\n\t[' + '\t'.join(map(str, zdt6(samRandom(n=_Ndim)))) + ']'
    print 'parentPpopulation[0].estimator(samRandom(n=' + str(_Ndim) + ')):\n\t[' + '\t'.join(
        map(str, population[0].estimator(samRandom(n=_Ndim)))) + ']'
    print
    surrogate = ANNSurrogate(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

    moeaLoop(surrogate, population)

    """Test Block
    """
    # surrogate = ANNSurrogate(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    # surrogate.fit(Xold_ind, Yold_obj)
    # y_pred = surrogate.predict(Xnew_ind)
    # # print surrogate.regressor
    # print 'ANNSurrogate.y_pred: ['+', '.join(map(str,y_pred))+']'


    # from sklearn.neural_network import MLPRegressor
    # regressor = MLPRegressor(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    # regressor.fit(Xold_ind, Yold_obj)
    # y_pred = regressor.predict(Xnew_ind)
    # # print regressor
    # print 'MLPRegressor.y_pred: ['+', '.join(map(str,y_pred))+']'
