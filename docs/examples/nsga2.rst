NSGA2
=====

nsga2.Population
----------------
.. py:function:: examples.nsga2.Population(numPop=4, numVar=10, estimator=benchmarks.zdt6, weights=(-1.0, -1.0))

    Population

    :param numPop:
    :param numVar:
    :param estimator:
    :param weights:
    :return:

nsga2.moeaLoop
--------------
.. py:function:: examples.nsga2.moeaLoop()

    moeaLoop

    :param _Ngen:
    :param _Ndim:
    :param _Npop:
    :param _Nobj:
    :param _Ncon:
    :param fileName:
    :param CXPB:

.. literalinclude:: /../examples/nsga2.py
    :language: python
    :emphasize-lines: 1-3,12

:lines: 34-35

    The main function includes
