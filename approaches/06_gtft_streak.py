"""
GTFT with Streak - Generous Tit for Tat adapted for dynamic payoff & noise.
Accounts for cooperation streak, handles misinterpretation (1% noise).
Used for APOGEE'24 variant with evolving payoffs.
Source: IteratedPrisonersDilemma/agent.py (GTFT class)
"""

from base_agent import BaseAgent
import random


class GTFTStreak(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)

    def next_move(self, state: dict) -> int:
        op_id = 1 if self.id == 2 else 2
        coop_streak = 0

        # Calculate cooperation streak (every 5 consecutive coops = +1 to N)
        itr = state["current_iter"]
        for i in range(itr - 1, 0, -1):
            if i in state["history"]:
                moves = state["history"][i]
                if moves.get(1) == 1 and moves.get(2) == 1:
                    coop_streak += 1
                else:
                    break

        coop_streak = (coop_streak + 4) // 5

        if itr == 1:
            return 1

        opponent_last_move = state["history"][itr - 1][op_id]
        own_last_move = state["history"][itr - 1][self.id]

        if opponent_last_move == -1:
            return -1
        elif opponent_last_move == 1 and own_last_move == -1:
            return -1
        elif random.random() < 0.01:  # Noise: misinterpret coop as defect
            return -1
        elif own_last_move == 1 and opponent_last_move == 1:
            return 1
        elif own_last_move == 1 and opponent_last_move == -1:
            return -1
        elif own_last_move == -1 and opponent_last_move == 1:
            return 1
        else:
            return -1
