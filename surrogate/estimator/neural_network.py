from sklearn.neural_network import MLPRegressor

from surrogate.base import SurrogateModel


class ANNSurrogate(SurrogateModel):
    """Multi-layer Perceptron regressor.

    This algorithm optimizes the squared-loss using l-bfgs or gradient descent.

    Parameters
    ----------
    hidden_layer_sizes : tuple, length = n_layers - 2, default (100,)
        The ith element represents the number of neurons in the ith
        hidden layer.

    activation : {'logistic', 'tanh', 'relu'}, default 'relu'
        Activation function for the hidden layer.

        - 'logistic', the logistic sigmoid function,
          returns f(x) = 1 / (1 + exp(-x)).

        - 'tanh', the hyperbolic tan function,
          returns f(x) = tanh(x).

        - 'relu', the rectified linear unit function,
          returns f(x) = max(0, x)

    algorithm : {'l-bfgs', 'sgd', 'adam'}, default 'adam'
        The algorithm for weight optimization.

        - 'l-bfgs' is an optimization algorithm in the family of
          quasi-Newton methods.

        - 'sgd' refers to stochastic gradient descent.

        - 'adam' refers to a stochastic gradient-based optimization algorithm
          proposed by Kingma, Diederik, and Jimmy Ba

        Note: The default algorithm 'adam' works pretty well on relatively
        large datasets (with thousands of training samples or more) in terms of
        both training time and validation score.
        For small datasets, however, 'l-bfgs' can converge faster and perform
        better.

    alpha : float, optional, default 0.0001
        L2 penalty (regularization term) parameter.

    batch_size : int, optional, default 200
        Size of minibatches for stochastic optimizers.
        If the algorithm is 'l-bfgs', the classifier will not use minibatch.

    learning_rate : {'constant', 'invscaling', 'adaptive'}, default 'constant'
        Learning rate schedule for weight updates.

        -'constant', is a constant learning rate given by
         'learning_rate_init'.

        -'invscaling' gradually decreases the learning rate ``learning_rate_`` at
          each time step 't' using an inverse scaling exponent of 'power_t'.
          effective_learning_rate = learning_rate_init / pow(t, power_t)

        -'adaptive', keeps the learning rate constant to
         'learning_rate_init' as long as training loss keeps decreasing.
         Each time two consecutive epochs fail to decrease training loss by at
         least tol, or fail to increase validation score by at least tol if
         'early_stopping' is on, the current learning rate is divided by 5.

         Only used when algorithm='sgd'.

    max_iter : int, optional, default 200
        Maximum number of iterations. The algorithm iterates until convergence
        (determined by 'tol') or this number of iterations.

    random_state : int or RandomState, optional, default None
        State or seed for random number generator.

    shuffle : bool, optional, default True
        Whether to shuffle samples in each iteration. Only used when
        algorithm='sgd' or 'adam'.

    tol : float, optional, default 1e-4
        Tolerance for the optimization. When the loss or score is not improving
        by at least tol for two consecutive iterations, unless `learning_rate`
        is set to 'adaptive', convergence is considered to be reached and
        training stops.

    learning_rate_init : double, optional, default 0.001
        The initial learning rate used. It controls the step-size
        in updating the weights. Only used when algorithm='sgd' or 'adam'.

    power_t : double, optional, default 0.5
        The exponent for inverse scaling learning rate.
        It is used in updating effective learning rate when the learning_rate
        is set to 'invscaling'. Only used when algorithm='sgd'.

    verbose : bool, optional, default False
        Whether to print progress messages to stdout.

    warm_start : bool, optional, default False
        When set to True, reuse the solution of the previous
        call to fit as initialization, otherwise, just erase the
        previous solution.

    momentum : float, default 0.9
        Momentum for gradient descent update.  Should be between 0 and 1. Only
        used when algorithm='sgd'.

    nesterovs_momentum : boolean, default True
        Whether to use Nesterov's momentum. Only used when algorithm='sgd' and
        momentum > 0.

    early_stopping : bool, default False
        Whether to use early stopping to terminate training when validation
        score is not improving. If set to true, it will automatically set
        aside 10% of training data as validation and terminate training when
        validation score is not improving by at least tol for two consecutive
        epochs.
        Only effective when algorithm='sgd' or 'adam'

    validation_fraction : float, optional, default 0.1
        The proportion of training data to set aside as validation set for
        early stopping. Must be between 0 and 1.
        Only used if early_stopping is True

    beta_1 : float, optional, default 0.9
        Exponential decay rate for estimates of first moment vector in adam,
        should be in [0, 1). Only used when algorithm='adam'

    beta_2 : float, optional, default 0.999
        Exponential decay rate for estimates of second moment vector in adam,
        should be in [0, 1). Only used when algorithm='adam'

    epsilon : float, optional, default 1e-8
        Value for numerical stability in adam. Only used when algorithm='adam'

    Attributes
    ----------
    `loss_` : float
        The current loss computed with the loss function.

    `coefs_` : list, length n_layers - 1
        The ith element in the list represents the weight matrix corresponding
        to layer i.

    `intercepts_` : list, length n_layers - 1
        The ith element in the list represents the bias vector corresponding to
        layer i + 1.

    n_iter_ : int,
        The number of iterations the algorithm has ran.

    n_layers_ : int
        Number of layers.

    `n_outputs_` : int
        Number of outputs.

    `out_activation_` : string
        Name of the output activation function.

    Notes
    -----
    MLPRegressor trains iteratively since at each time step
    the partial derivatives of the loss function with respect to the model
    parameters are computed to update the parameters.

    It can also have a regularization term added to the loss function
    that shrinks model parameters to prevent overfitting.

    This implementation works with data represented as dense and sparse numpy
    arrays of floating point values.

    References
    ----------
    Hinton, Geoffrey E.
        "Connectionist learning procedures." Artificial intelligence 40.1
        (1989): 185-234.

    Glorot, Xavier, and Yoshua Bengio. "Understanding the difficulty of
        training deep feedforward neural networks." International Conference
        on Artificial Intelligence and Statistics. 2010.

    He, Kaiming, et al. "Delving deep into rectifiers: Surpassing human-level
        performance on imagenet classification." arXiv preprint
        arXiv:1502.01852 (2015).

    Kingma, Diederik, and Jimmy Ba. "Adam: A method for stochastic
        optimization." arXiv preprint arXiv:1412.6980 (2014).
    """
    def __init__(self, hidden_layer_sizes=(100,),
                 activation="relu", algorithm='adam', alpha=0.0001,
                 batch_size=200, learning_rate="constant",
                 learning_rate_init=0.001, power_t=0.5,
                 max_iter=200, shuffle=True,
                 random_state=None, tol=1e-4, verbose=False,
                 warm_start=False, momentum=0.9,
                 nesterovs_momentum=True, early_stopping=False,
                 validation_fraction=0.1,
                 beta_1=0.9, beta_2=0.999, epsilon=1e-8):
        super(ANNSurrogate, self).__init__()

        # self.hidden_layer_sizes=(100,)
        # self.activation="relu"
        # self.algorithm='adam'
        # self.alpha=0.0001
        # self.batch_size=200
        # self.learning_rate="constant"
        # self.learning_rate_init=0.001
        # self.power_t=0.5
        # self.max_iter=200
        # self.shuffle=True
        # self.random_state=None
        # self.tol=1e-4
        # self.verbose=False
        # self.warm_start=False
        # self.momentum=0.9
        # self.nesterovs_momentum=True
        # self.early_stopping=False
        # self.validation_fraction=0.1
        # self.beta_1=0.9
        # self.beta_2=0.999
        # self.epsilon=1e-8

        # self.x = None
        # self.y = None

        # algorithm => solver
        self.__model = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes,
                                    activation=activation, solver=algorithm, alpha=alpha,
                                    batch_size=batch_size, learning_rate=learning_rate,
                                    learning_rate_init=learning_rate_init, power_t=power_t,
                                    max_iter=max_iter, shuffle=shuffle,
                                    random_state=random_state, tol=tol, verbose=verbose,
                                    warm_start=warm_start, momentum=momentum,
                                    nesterovs_momentum=nesterovs_momentum,
                                    early_stopping=early_stopping,
                                    validation_fraction=validation_fraction,
                                    beta_1=beta_1, beta_2=beta_2, epsilon=epsilon)

    def fit(self, x, y):
        super(ANNSurrogate, self).fit(x, y)

        # print 'fit'
        self.__model.fit(x, y)

    def predict(self, x):
        super(ANNSurrogate, self).predict(x)

        # print 'predict'
        y = self.__model.predict(x)
        return y

    def predict_proba(self, x):
        pass
