from .selBest import selBest
from .selDoubleTournament import selDoubleTournament
from .selRandom import selRandom
from .selRoulette import selRoulette
from .selStochasticUniversalSampling import selStochasticUniversalSampling
from .selTournament import selTournament
from .selWorst import selWorst

__all__ = [
    'selRandom',
    'selBest', 'selWorst',
    'selTournament', 'selDoubleTournament',
    'selStochasticUniversalSampling',
    'selRoulette'
]
