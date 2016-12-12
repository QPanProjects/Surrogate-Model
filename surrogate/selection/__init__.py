from .selBest import selBest
from .selDoubleTournament import selDoubleTournament
from .selNSGA2 import selNSGA2
from .selRandom import selRandom
from .selRoulette import selRoulette
from .selSPEA2 import selSPEA2
from .selStochasticUniversalSampling import selStochasticUniversalSampling
from .selTournament import selTournament
from .selTournamentDCD import selTournamentDCD
from .selWorst import selWorst

__all__ = [
    'selRandom',
    'selBest', 'selWorst',
    'selTournament', 'selDoubleTournament', 'selTournamentDCD',
    'selStochasticUniversalSampling',
    'selRoulette',
    'selNSGA2', 'selSPEA2'
]
