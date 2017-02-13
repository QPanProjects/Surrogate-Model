# MIT License
#
# Copyright (c) 2016 Daily Actie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02

#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

import array
import random

import numpy
from deap import base
from deap import benchmarks

# from deap.benchmarks.tools import hypervolume
from deap import creator
from deap import tools

creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Problem definition
# Functions zdt1, zdt2, zdt3, zdt6 have bounds [0, 1]
BOUND_LOW, BOUND_UP = 0.0, 1.0

# Functions zdt4 has bounds x1 = [0, 1], xn = [-5, 5], with n = 2, ..., 10
# BOUND_LOW, BOUND_UP = [0.0] + [-5.0]*9, [1.0] + [5.0]*9

# Functions zdt1, zdt2, zdt3 have 30 dimensions, zdt4 and zdt6 have 10
NDIM = 10

random.seed(0.5)

def uniform(low, up, size=None):
    try:
        return [random.uniform(a, b) for a, b in zip(low, up)]
    except TypeError:
        return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]


toolbox.register("attr_float", uniform, BOUND_LOW, BOUND_UP, NDIM)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attr_float)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# toolbox.register("evaluate", benchmarks.zdt1)
toolbox.register("evaluate", benchmarks.zdt6)
toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0)
toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0, indpb=1.0 / NDIM)
toolbox.register("select", tools.selNSGA2)


def main(seed=None):
    random.seed(seed)

    NGEN = 10
    MU = 12
    CXPB = 0.9

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    # stats.register("avg", numpy.mean, axis=0)
    # stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    logbook = tools.Logbook()
    logbook.header = "gen", "evals", "std", "min", "avg", "max"

    pop = toolbox.population(n=MU)

    variables = [
        [0.08966, 0.85338, 0.98579, 0.15400, 0.21201, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775],
        [0.50637, 0.21866, 0.05956, 0.14900, 0.27852, 0.14137, 0.42839, 0.75617, 0.14790, 0.08260],
        [0.27840, 0.21768, 0.17810, 0.35452, 0.85922, 0.00088, 0.08544, 0.03811, 0.35325, 0.25055],
        [0.41416, 0.85318, 0.01416, 0.66403, 0.01492, 0.65336, 0.80880, 0.05268, 0.52587, 0.93375],
        [0.23447, 0.99610, 0.36593, 0.38134, 0.42196, 0.83398, 0.12267, 0.95272, 0.86049, 0.46400],
        [0.56176, 0.65177, 0.81456, 0.22058, 0.10519, 0.78797, 0.31508, 0.94056, 0.21079, 0.49574],
        [0.67224, 0.32400, 0.06878, 0.30880, 0.18294, 0.66287, 0.09993, 0.41787, 0.23267, 0.62995],
        [0.79480, 0.49413, 0.19621, 0.85527, 0.51985, 0.28863, 0.28846, 0.81689, 0.81627, 0.05864],
        [0.89941, 0.35737, 0.93038, 0.77133, 0.94898, 0.12099, 0.22275, 0.99442, 0.03623, 0.20604],
        [0.02257, 0.88028, 0.04750, 0.94849, 0.80619, 0.12603, 0.36930, 0.09194, 0.56919, 0.75869],
        [0.16264, 0.65064, 0.09147, 0.80063, 0.07220, 0.20550, 0.44796, 0.71409, 0.82605, 0.81780],
        [0.18315, 0.97412, 0.37952, 0.38988, 0.57634, 0.94170, 0.01935, 0.48783, 0.62966, 0.71127]
    ]
    for i in range(MU):
        for j in range(len(pop[i])):
            pop[i][j] = variables[i][j]

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # This is just to assign the crowding distance to the individuals
    # no actual selection is done
    pop = toolbox.select(pop, len(pop))
    for ipop in pop:
        print '\tpopulation.sel.b' \
              + '\tvar1: [' + ', '.join(map("{:.5f}".format, ipop)) + ']'
    print

    record = stats.compile(pop)
    logbook.record(gen=0, evals=len(invalid_ind), **record)
    # print(logbook.stream)

    # Begin the generational process
    for gen in range(1, NGEN):
        print '\n' + str(gen) + '\tGen:'
        # for ipop in pop:
        #     print '\tpopulation.sel.b'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'\
        #           + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'

        offspring = tools.selTournamentDCD(pop, len(pop))
        # for ipop in offspring:
        #     print '\toffspring.sel.a'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'\
        #           + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'
        # print

        offspring = [toolbox.clone(ind) for ind in offspring]
        # TODO 20161212 pass memeory address instead of values
        # for ipop in pop:
        #     print '\toffspring.cln.a'\
        #           + '\tvar1: [' + ', '.join(map("{:.5f}".format, ipop)) + ']'
        # print

        for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
            if random.random() <= CXPB:
                # print '\toffspring.cx.b'\
                #       + '\tvar1: [' + ', '.join(map("{:.5f}".format, ind1)) + ']'\
                #       + '\tvar2: [' + ', '.join(map("{:.5f}".format, ind2)) + ']'
                toolbox.mate(ind1, ind2)
                # print '\toffspring.cx.a'\
                #       + '\tvar1: [' + ', '.join(map("{:.5f}".format, ind1)) + ']'\
                #       + '\tvar2: [' + ', '.join(map("{:.5f}".format, ind2)) + ']'

            # print '\toffspring.mut.b'\
            #       + '\tvar1: [' + ', '.join(map("{:.5f}".format, ind1)) + ']'\
            #       + '\tvar2: [' + ', '.join(map("{:.5f}".format, ind2)) + ']'
            toolbox.mutate(ind1)
            toolbox.mutate(ind2)
            # print '\toffspring.mut.a'\
            #       + '\tvar1: [' + ', '.join(map("{:.5f}".format, ind1)) + ']'\
            #       + '\tvar2: [' + ', '.join(map("{:.5f}".format, ind2)) + ']'
            # print

            del ind1.fitness.values, ind2.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # print 'Select the next generation population\nAfter cx mut'
        # for ipop in pop:
        #     print '\tpopulation.sel.b'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'\
        #           + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'
        # for ipop in offspring:
        #     print '\toffspring.sel.b'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'
        #           # + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'
        # print
        pop = toolbox.select(pop + offspring, MU)
        record = stats.compile(pop)
        logbook.record(gen=gen, evals=len(invalid_ind), **record)
        # print(logbook.stream)
        for ipop in range(MU):
            print '\tpopulation.sel.a' \
                  + '\tXold_ind: [' + ', '.join(map("{:.5f}".format, pop[ipop])) + ']' \
                  + '\tYold_obj: [' + ', '.join(map("{:.5f}".format, pop[ipop].fitness.values)) + ']' \
                  + '\tcrw: [' + str(pop[ipop].fitness.crowding_dist) + ']'
    # print("Final population hypervolume is %f" % hypervolume(pop, [11.0, 11.0]))

    return pop, logbook


if __name__ == "__main__":
    # with open("pareto_front/zdt1_front.json") as optimal_front_data:
    #     optimal_front = json.load(optimal_front_data)
    # Use 500 of the 1000 points in the json file
    # optimal_front = sorted(optimal_front[i] for i in range(0, len(optimal_front), 2))

    pop, stats = main()
    pop.sort(key=lambda x: x.fitness.values)

    # print(stats)
    # print("Convergence: ", convergence(pop, optimal_front))
    # print("Diversity: ", diversity(pop, optimal_front[0], optimal_front[-1]))

    # import matplotlib.pyplot as plt
    # import numpy

    # front = numpy.array([ind.fitness.values for ind in pop])
    # optimal_front = numpy.array(optimal_front)
    # plt.scatter(optimal_front[:,0], optimal_front[:,1], c="r")
    # plt.scatter(front[:,0], front[:,1], c="b")
    # plt.axis("tight")
    # plt.show()


    """
    /usr/bin/python /Users/quanpan/Documents/mac-Python/SurrogateModel/examples/nsga2.py
        population.sel.b	var1: [0.08966, 0.85338, 0.98579, 0.15400, 0.21201, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775]
        population.sel.b	var1: [0.27840, 0.21768, 0.17810, 0.35452, 0.85922, 0.00088, 0.08544, 0.03811, 0.35325, 0.25055]
        population.sel.b	var1: [0.50637, 0.21866, 0.05956, 0.14900, 0.27852, 0.14137, 0.42839, 0.75617, 0.14790, 0.08260]
        population.sel.b	var1: [0.41416, 0.85318, 0.01416, 0.66403, 0.01492, 0.65336, 0.80880, 0.05268, 0.52587, 0.93375]
        population.sel.b	var1: [0.23447, 0.99610, 0.36593, 0.38134, 0.42196, 0.83398, 0.12267, 0.95272, 0.86049, 0.46400]
        population.sel.b	var1: [0.79480, 0.49413, 0.19621, 0.85527, 0.51985, 0.28863, 0.28846, 0.81689, 0.81627, 0.05864]
        population.sel.b	var1: [0.56176, 0.65177, 0.81456, 0.22058, 0.10519, 0.78797, 0.31508, 0.94056, 0.21079, 0.49574]
        population.sel.b	var1: [0.67224, 0.32400, 0.06878, 0.30880, 0.18294, 0.66287, 0.09993, 0.41787, 0.23267, 0.62995]
        population.sel.b	var1: [0.89941, 0.35737, 0.93038, 0.77133, 0.94898, 0.12099, 0.22275, 0.99442, 0.03623, 0.20604]
        population.sel.b	var1: [0.02257, 0.88028, 0.04750, 0.94849, 0.80619, 0.12603, 0.36930, 0.09194, 0.56919, 0.75869]
        population.sel.b	var1: [0.18315, 0.97412, 0.37952, 0.38988, 0.57634, 0.94170, 0.01935, 0.48783, 0.62966, 0.71127]
        population.sel.b	var1: [0.16264, 0.65064, 0.09147, 0.80063, 0.07220, 0.20550, 0.44796, 0.71409, 0.82605, 0.81780]


    1	Gen:
        population.sel.b	var: [0.08966, 0.85338, 0.98579, 0.15400, 0.21201, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775]	obj: [0.33062, 8.31210]	crw: [inf]
        population.sel.b	var: [0.27840, 0.21768, 0.17810, 0.35452, 0.85922, 0.00088, 0.08544, 0.03811, 0.35325, 0.25055]	obj: [0.86706, 7.32387]	crw: [1.0]
        population.sel.b	var: [0.50637, 0.21866, 0.05956, 0.14900, 0.27852, 0.14137, 0.42839, 0.75617, 0.14790, 0.08260]	obj: [1.00000, 7.23691]	crw: [inf]
        population.sel.b	var: [0.41416, 0.85318, 0.01416, 0.66403, 0.01492, 0.65336, 0.80880, 0.05268, 0.52587, 0.93375]	obj: [0.81050, 8.50019]	crw: [0.554502265619]
        population.sel.b	var: [0.23447, 0.99610, 0.36593, 0.38134, 0.42196, 0.83398, 0.12267, 0.95272, 0.86049, 0.46400]	obj: [0.69842, 8.86603]	crw: [inf]
        population.sel.b	var: [0.79480, 0.49413, 0.19621, 0.85527, 0.51985, 0.28863, 0.28846, 0.81689, 0.81627, 0.05864]	obj: [0.99643, 8.38059]	crw: [0.445497734381]
        population.sel.b	var: [0.56176, 0.65177, 0.81456, 0.22058, 0.10519, 0.78797, 0.31508, 0.94056, 0.21079, 0.49574]	obj: [0.93655, 8.48361]	crw: [0.358208177905]
        population.sel.b	var: [0.67224, 0.32400, 0.06878, 0.30880, 0.18294, 0.66287, 0.09993, 0.41787, 0.23267, 0.62995]	obj: [1.00000, 7.66875]	crw: [inf]
        population.sel.b	var: [0.89941, 0.35737, 0.93038, 0.77133, 0.94898, 0.12099, 0.22275, 0.99442, 0.03623, 0.20604]	obj: [0.98018, 8.49335]	crw: [inf]
        population.sel.b	var: [0.02257, 0.88028, 0.04750, 0.94849, 0.80619, 0.12603, 0.36930, 0.09194, 0.56919, 0.75869]	obj: [0.99548, 8.49366]	crw: [inf]
        population.sel.b	var: [0.18315, 0.97412, 0.37952, 0.38988, 0.57634, 0.94170, 0.01935, 0.48783, 0.62966, 0.71127]	obj: [0.99961, 8.69893]	crw: [inf]
        population.sel.b	var: [0.16264, 0.65064, 0.09147, 0.80063, 0.07220, 0.20550, 0.44796, 0.71409, 0.82605, 0.81780]	obj: [1.00000, 8.50464]	crw: [inf]
        offspring.sel.a	var: [0.02257, 0.88028, 0.04750, 0.94849, 0.80619, 0.12603, 0.36930, 0.09194, 0.56919, 0.75869]	obj: [0.99548, 8.49366]	crw: [inf]
        offspring.sel.a	var: [0.67224, 0.32400, 0.06878, 0.30880, 0.18294, 0.66287, 0.09993, 0.41787, 0.23267, 0.62995]	obj: [1.00000, 7.66875]	crw: [inf]
        offspring.sel.a	var: [0.27840, 0.21768, 0.17810, 0.35452, 0.85922, 0.00088, 0.08544, 0.03811, 0.35325, 0.25055]	obj: [0.86706, 7.32387]	crw: [1.0]
        offspring.sel.a	var: [0.08966, 0.85338, 0.98579, 0.15400, 0.21201, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775]	obj: [0.33062, 8.31210]	crw: [inf]
        offspring.sel.a	var: [0.23447, 0.99610, 0.36593, 0.38134, 0.42196, 0.83398, 0.12267, 0.95272, 0.86049, 0.46400]	obj: [0.69842, 8.86603]	crw: [inf]
        offspring.sel.a	var: [0.27840, 0.21768, 0.17810, 0.35452, 0.85922, 0.00088, 0.08544, 0.03811, 0.35325, 0.25055]	obj: [0.86706, 7.32387]	crw: [1.0]
        offspring.sel.a	var: [0.79480, 0.49413, 0.19621, 0.85527, 0.51985, 0.28863, 0.28846, 0.81689, 0.81627, 0.05864]	obj: [0.99643, 8.38059]	crw: [0.445497734381]
        offspring.sel.a	var: [0.41416, 0.85318, 0.01416, 0.66403, 0.01492, 0.65336, 0.80880, 0.05268, 0.52587, 0.93375]	obj: [0.81050, 8.50019]	crw: [0.554502265619]
        offspring.sel.a	var: [0.50637, 0.21866, 0.05956, 0.14900, 0.27852, 0.14137, 0.42839, 0.75617, 0.14790, 0.08260]	obj: [1.00000, 7.23691]	crw: [inf]
        offspring.sel.a	var: [0.08966, 0.85338, 0.98579, 0.15400, 0.21201, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775]	obj: [0.33062, 8.31210]	crw: [inf]
        offspring.sel.a	var: [0.67224, 0.32400, 0.06878, 0.30880, 0.18294, 0.66287, 0.09993, 0.41787, 0.23267, 0.62995]	obj: [1.00000, 7.66875]	crw: [inf]
        offspring.sel.a	var: [0.50637, 0.21866, 0.05956, 0.14900, 0.27852, 0.14137, 0.42839, 0.75617, 0.14790, 0.08260]	obj: [1.00000, 7.23691]	crw: [inf]

    After cx mut
        population.sel.b	var: [0.08966, 0.85338, 0.98579, 0.15400, 0.21201, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775]	obj: [0.33062, 8.31210]	crw: [inf]
        population.sel.b	var: [0.27840, 0.21768, 0.17810, 0.35452, 0.85922, 0.00088, 0.08544, 0.03811, 0.35325, 0.25055]	obj: [0.86706, 7.32387]	crw: [1.0]
        population.sel.b	var: [0.50637, 0.21866, 0.05956, 0.14900, 0.27852, 0.14137, 0.42839, 0.75617, 0.14790, 0.08260]	obj: [1.00000, 7.23691]	crw: [inf]
        population.sel.b	var: [0.41416, 0.85318, 0.01416, 0.66403, 0.01492, 0.65336, 0.80880, 0.05268, 0.52587, 0.93375]	obj: [0.81050, 8.50019]	crw: [0.554502265619]
        population.sel.b	var: [0.23447, 0.99610, 0.36593, 0.38134, 0.42196, 0.83398, 0.12267, 0.95272, 0.86049, 0.46400]	obj: [0.69842, 8.86603]	crw: [inf]
        population.sel.b	var: [0.79480, 0.49413, 0.19621, 0.85527, 0.51985, 0.28863, 0.28846, 0.81689, 0.81627, 0.05864]	obj: [0.99643, 8.38059]	crw: [0.445497734381]
        population.sel.b	var: [0.56176, 0.65177, 0.81456, 0.22058, 0.10519, 0.78797, 0.31508, 0.94056, 0.21079, 0.49574]	obj: [0.93655, 8.48361]	crw: [0.358208177905]
        population.sel.b	var: [0.67224, 0.32400, 0.06878, 0.30880, 0.18294, 0.66287, 0.09993, 0.41787, 0.23267, 0.62995]	obj: [1.00000, 7.66875]	crw: [inf]
        population.sel.b	var: [0.89941, 0.35737, 0.93038, 0.77133, 0.94898, 0.12099, 0.22275, 0.99442, 0.03623, 0.20604]	obj: [0.98018, 8.49335]	crw: [inf]
        population.sel.b	var: [0.02257, 0.88028, 0.04750, 0.94849, 0.80619, 0.12603, 0.36930, 0.09194, 0.56919, 0.75869]	obj: [0.99548, 8.49366]	crw: [inf]
        population.sel.b	var: [0.18315, 0.97412, 0.37952, 0.38988, 0.57634, 0.94170, 0.01935, 0.48783, 0.62966, 0.71127]	obj: [0.99961, 8.69893]	crw: [inf]
        population.sel.b	var: [0.16264, 0.65064, 0.09147, 0.80063, 0.07220, 0.20550, 0.44796, 0.71409, 0.82605, 0.81780]	obj: [1.00000, 8.50464]	crw: [inf]
        offspring.sel.b	var: [0.02257, 0.88028, 0.04845, 0.31086, 0.80619, 0.12603, 0.36272, 0.41711, 0.56133, 0.62994]	obj: [0.99548, 8.29546]
        offspring.sel.b	var: [0.67224, 0.32400, 0.06783, 0.94610, 0.18574, 0.66287, 0.10651, 0.09270, 0.23267, 0.75870]	obj: [1.00000, 7.91966]
        offspring.sel.b	var: [0.27840, 0.81229, 0.17810, 0.39612, 0.23169, 0.00088, 0.21058, 0.03811, 0.35325, 0.25055]	obj: [0.86706, 7.41513]
        offspring.sel.b	var: [0.08966, 0.23939, 0.98579, 0.15400, 0.83953, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775]	obj: [0.33062, 8.31837]
        offspring.sel.b	var: [0.23376, 0.99610, 0.36593, 0.38229, 0.85715, 0.83398, 0.08504, 0.06297, 0.86049, 0.46400]	obj: [0.70494, 8.67715]
        offspring.sel.b	var: [0.27911, 0.21768, 0.17810, 0.35357, 0.42403, 0.02061, 0.12360, 0.92853, 0.35325, 0.06050]	obj: [0.87366, 7.53590]
        offspring.sel.b	var: [0.79586, 0.83937, 0.19621, 0.85527, 0.51985, 0.65662, 0.28153, 0.81417, 0.81627, 0.06239]	obj: [0.99690, 8.67309]
        offspring.sel.b	var: [0.41310, 0.50794, 0.00023, 0.66403, 0.01492, 0.29686, 0.68836, 0.05601, 0.52587, 0.93020]	obj: [0.81099, 8.11882]
        offspring.sel.b	var: [0.51502, 0.21866, 0.75035, 0.14877, 0.27852, 0.13938, 0.43060, 0.75893, 0.14790, 0.57157]	obj: [0.99994, 7.95519]
        offspring.sel.b	var: [0.08102, 0.85338, 0.10533, 0.15423, 0.21297, 0.39199, 0.24394, 0.52021, 0.02758, 0.06884]	obj: [0.28092, 7.57409]
        offspring.sel.b	var: [0.48086, 0.21365, 0.05907, 0.14827, 0.18294, 0.62110, 0.46264, 0.76065, 0.23267, 0.61779]	obj: [0.99972, 7.87789]
        offspring.sel.b	var: [0.68114, 0.32901, 0.06927, 0.30953, 0.27852, 0.18314, 0.06571, 0.41339, 0.13699, 0.09478]	obj: [0.99997, 6.94358]

        population.sel.a	Xold_ind: [0.27840, 0.21768, 0.17810, 0.35452, 0.85922, 0.00088, 0.08544, 0.03811, 0.35325, 0.25055]	Yold_obj: [0.86706, 7.32387]	crw: [1.0]
        population.sel.a	Xold_ind: [0.68114, 0.32901, 0.06927, 0.30953, 0.27852, 0.18314, 0.06571, 0.41339, 0.13699, 0.09478]	Yold_obj: [0.99997, 6.94358]	crw: [inf]
        population.sel.a	Xold_ind: [0.08102, 0.85338, 0.10533, 0.15423, 0.21297, 0.39199, 0.24394, 0.52021, 0.02758, 0.06884]	Yold_obj: [0.28092, 7.57409]	crw: [inf]
        population.sel.a	Xold_ind: [0.27840, 0.81229, 0.17810, 0.39612, 0.23169, 0.00088, 0.21058, 0.03811, 0.35325, 0.25055]	Yold_obj: [0.86706, 7.41513]	crw: [0.551301322491]
        population.sel.a	Xold_ind: [0.50637, 0.21866, 0.05956, 0.14900, 0.27852, 0.14137, 0.42839, 0.75617, 0.14790, 0.08260]	Yold_obj: [1.00000, 7.23691]	crw: [inf]
        population.sel.a	Xold_ind: [0.08966, 0.85338, 0.98579, 0.15400, 0.21201, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775]	Yold_obj: [0.33062, 8.31210]	crw: [inf]
        population.sel.a	Xold_ind: [0.41310, 0.50794, 0.00023, 0.66403, 0.01492, 0.29686, 0.68836, 0.05601, 0.52587, 0.93020]	Yold_obj: [0.81099, 8.11882]	crw: [0.817818013965]
        population.sel.a	Xold_ind: [0.27911, 0.21768, 0.17810, 0.35357, 0.42403, 0.02061, 0.12360, 0.92853, 0.35325, 0.06050]	Yold_obj: [0.87366, 7.53590]	crw: [inf]
        population.sel.a	Xold_ind: [0.08966, 0.23939, 0.98579, 0.15400, 0.83953, 0.39000, 0.24615, 0.52297, 0.02758, 0.55775]	Yold_obj: [0.33062, 8.31837]	crw: [inf]
        population.sel.a	Xold_ind: [0.67224, 0.32400, 0.06878, 0.30880, 0.18294, 0.66287, 0.09993, 0.41787, 0.23267, 0.62995]	Yold_obj: [1.00000, 7.66875]	crw: [inf]
        population.sel.a	Xold_ind: [0.23447, 0.99610, 0.36593, 0.38134, 0.42196, 0.83398, 0.12267, 0.95272, 0.86049, 0.46400]	Yold_obj: [0.69842, 8.86603]	crw: [inf]
        population.sel.a	Xold_ind: [0.41416, 0.85318, 0.01416, 0.66403, 0.01492, 0.65336, 0.80880, 0.05268, 0.52587, 0.93375]	Yold_obj: [0.81050, 8.50019]	crw: [0.464815535044]

    Process finished with exit code 0

    """
