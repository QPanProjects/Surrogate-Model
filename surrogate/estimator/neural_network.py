from sklearn.neural_network import MLPRegressor

from surrogate.base import SurrogateModel


class ANNSurrogate(SurrogateModel):
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

        self.__model = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes,
                                    activation=activation, algorithm=algorithm, alpha=alpha,
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

        print 'fit'
        self.__model.fit(x, y)

    def predict(self, x):
        super(ANNSurrogate, self).predict(x)

        print 'predict'
        y = self.__model.predict(x)
        print y
        return y

    def predict_proba(self, x):
        pass
