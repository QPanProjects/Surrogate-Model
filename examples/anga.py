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
