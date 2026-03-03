"""
Final Strategy - 2nd Prize winner at APOGEE'24 IEEE Event (by another participant).
Generosity factor with exponential decay based on streak.
Balances trust and noise tolerance in dynamic payoff environment.
Source: IteratedPrisonersDilemma/final_strategy.py, included for reference.
"""

from base_agent import BaseAgent
import random
import math


class FinalStrategy(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)

    def next_move(self, state: dict) -> int:
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        # Early rounds: detect patterns for forgiveness
        if itr >= 4:
            if (
                state["history"][itr - 3][op_id] == 1
                and state["history"][itr - 2][self.id] == -1
                and state["history"][itr - 2][op_id] == 1
            ):
                return 1
            if (
                state["history"][itr - 3][op_id] == 1
                and state["history"][itr - 2][op_id] == 1
            ):
                return 1

        # Generosity: exponentially decaying forgiveness based on streak
        streak = state.get("streak", 0)
        generosity = 0.25 / math.exp(streak * 0.07)
        if random.random() < generosity:
            return 1
        return state["history"][itr - 1][op_id] if itr != 1 else 1
