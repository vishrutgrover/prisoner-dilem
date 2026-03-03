"""
Base class for all Prisoner's Dilemma strategies.
APOGEE'24 & APOGEE'25 - Iterated Prisoner's Dilemma Challenge
"""


class BaseAgent:
    def __init__(self, id):
        self.id = id

    def next_move(self, state):
        """
        Return 1 for cooperate, -1 for defect.
        state contains: current_iter, history, streak
        """
        return 0
