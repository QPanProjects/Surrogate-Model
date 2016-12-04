from surrogate.base import Individual


def Individuals(n=10):
    return [
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=10.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=9.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=8.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=7.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=6.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=5.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=4.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=3.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=2.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=1.0, constrain=[])
    ]
