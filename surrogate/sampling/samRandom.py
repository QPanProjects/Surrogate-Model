"""
encoding: utf-8
module numpy.random.mtrand
from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/random/mtrand.so
by generator 1.138
no doc

Links:
    https://docs.scipy.org/doc/numpy/reference/routines.random.html

"""

import numpy.random as rand


def samRandom(n=2, k=2):
    return rand.rand(n, k)


def samBeta(a=0.1, b=0.1, size=None):  # real signature unknown; restored from __doc__
    """
    beta(a, b, size=None)

            Draw samples from a Beta distribution.

            The Beta distribution is a special case of the Dirichlet distribution,
            and is related to the Gamma distribution.  It has the probability
            distribution function

            .. math:: f(x; a,b) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}
                                                             (1 - x)^{\beta - 1},

            where the normalisation, B, is the beta function,

            .. math:: B(\alpha, \beta) = \int_0^1 t^{\alpha - 1}
                                         (1 - t)^{\beta - 1} dt.

            It is often seen in Bayesian inference and order statistics.

            Parameters
            ----------
            a : float
                Alpha, non-negative.
            b : float
                Beta, non-negative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.

            Returns
            -------
            out : ndarray
                Array of the given shape, containing values drawn from a
                Beta distribution.
    """
    return rand.beta(a=a, b=b, size=size)


def samBinomial(n=0.1, p=0.5, size=None):  # real signature unknown; restored from __doc__
    """
    binomial(n, p, size=None)

            Draw samples from a binomial distribution.

            Samples are drawn from a binomial distribution with specified
            parameters, n trials and p probability of success where
            n an integer >= 0 and p is in the interval [0,1]. (n may be
            input as a float, but it is truncated to an integer in use)

            Parameters
            ----------
            n : float (but truncated to an integer)
                    parameter, >= 0.
            p : float
                    parameter, >= 0 and <=1.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.

            Returns
            -------
            samples : ndarray or scalar
                      where the values are all integers in  [0, n].

            See Also
            --------
            scipy.stats.distributions.binom : probability density function,
                distribution or cumulative density function, etc.

            Notes
            -----
            The probability density for the binomial distribution is

            .. math:: P(N) = \binom{n}{N}p^N(1-p)^{n-N},

            where :math:`n` is the number of trials, :math:`p` is the probability
            of success, and :math:`N` is the number of successes.

            When estimating the standard error of a proportion in a population by
            using a random sample, the normal distribution works well unless the
            product p*n <=5, where p = population proportion estimate, and n =
            number of samples, in which case the binomial distribution is used
            instead. For example, a sample of 15 people shows 4 who are left
            handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27*15 = 4,
            so the binomial distribution should be used in this case.

            References
            ----------
            .. [1] Dalgaard, Peter, "Introductory Statistics with R",
                   Springer-Verlag, 2002.
            .. [2] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
                   Fifth Edition, 2002.
            .. [3] Lentner, Marvin, "Elementary Applied Statistics", Bogden
                   and Quigley, 1972.
            .. [4] Weisstein, Eric W. "Binomial Distribution." From MathWorld--A
                   Wolfram Web Resource.
                   http://mathworld.wolfram.com/BinomialDistribution.html
            .. [5] Wikipedia, "Binomial-distribution",
                   http://en.wikipedia.org/wiki/Binomial_distribution

            Examples
            --------
            Draw samples from the distribution:

            >>> n, p = 10, .5  # number of trials, probability of each trial
            >>> s = np.random.binomial(n, p, 1000)
            # result of flipping a coin 10 times, tested 1000 times.

            A real world example. A company drills 9 wild-cat oil exploration
            wells, each with an estimated probability of success of 0.1. All nine
            wells fail. What is the probability of that happening?

            Let's do 20,000 trials of the model, and count the number that
            generate zero positive results.

            >>> sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.
            # answer = 0.38885, or 38%.
    """
    return rand.binomial(n=n, p=p, size=size)


def samChiSquare(df=2, size=None):  # real signature unknown; restored from __doc__
    """
    chisquare(df, size=None)

            Draw samples from a chi-square distribution.

            When `df` independent random variables, each with standard normal
            distributions (mean 0, variance 1), are squared and summed, the
            resulting distribution is chi-square (see Notes).  This distribution
            is often used in hypothesis testing.

            Parameters
            ----------
            df : int
                 Number of degrees of freedom.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.

            Returns
            -------
            output : ndarray
                Samples drawn from the distribution, packed in a `size`-shaped
                array.

            Raises
            ------
            ValueError
                When `df` <= 0 or when an inappropriate `size` (e.g. ``size=-1``)
                is given.

            Notes
            -----
            The variable obtained by summing the squares of `df` independent,
            standard normally distributed random variables:

            .. math:: Q = \sum_{i=0}^{\mathtt{df}} X^2_i

            is chi-square distributed, denoted

            .. math:: Q \sim \chi^2_k.

            The probability density function of the chi-squared distribution is

            .. math:: p(x) = \frac{(1/2)^{k/2}}{\Gamma(k/2)}
                             x^{k/2 - 1} e^{-x/2},

            where :math:`\Gamma` is the gamma function,

            .. math:: \Gamma(x) = \int_0^{-\infty} t^{x - 1} e^{-t} dt.

            References
            ----------
            .. [1] NIST "Engineering Statistics Handbook"
                   http://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm

            Examples
            --------
            >>> np.random.chisquare(2,4)
            array([ 1.89920014,  9.00867716,  3.13710533,  5.62318272])
    """
    return rand.chisquare(df=df, size=size)


def samExponential(scale=1.0, size=None):  # real signature unknown; restored from __doc__
    """
    exponential(scale=1.0, size=None)

            Draw samples from an exponential distribution.

            Its probability density function is

            .. math:: f(x; \frac{1}{\beta}) = \frac{1}{\beta} \exp(-\frac{x}{\beta}),

            for ``x > 0`` and 0 elsewhere. :math:`\beta` is the scale parameter,
            which is the inverse of the rate parameter :math:`\lambda = 1/\beta`.
            The rate parameter is an alternative, widely used parameterization
            of the exponential distribution [3]_.

            The exponential distribution is a continuous analogue of the
            geometric distribution.  It describes many common situations, such as
            the size of raindrops measured over many rainstorms [1]_, or the time
            between page requests to Wikipedia [2]_.

            Parameters
            ----------
            scale : float
                The scale parameter, :math:`\beta = 1/\lambda`.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.

            References
            ----------
            .. [1] Peyton Z. Peebles Jr., "Probability, Random Variables and
                   Random Signal Principles", 4th ed, 2001, p. 57.
            .. [2] "Poisson Process", Wikipedia,
                   http://en.wikipedia.org/wiki/Poisson_process
            .. [3] "Exponential Distribution, Wikipedia,
                   http://en.wikipedia.org/wiki/Exponential_distribution
    """
    return rand.exponential(scale=scale, size=size)
