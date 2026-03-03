"""
Generous Tit for Tat - Tit for Tat with forgiveness.
When opponent defects after we cooperated, forgive with ~20-30% probability.
Source: Test/p1 (commented variants)
"""

from base_agent import BaseAgent
import random


class GenerousTitForTat(BaseAgent):
    def __init__(self, id: int, forgiveness: float = 0.25):
        super().__init__(id=id)
        self.forgiveness = forgiveness

    def next_move(self, state: dict) -> int:
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        if itr == 1:
            return 1

        opponent_last_move = state["history"][itr - 1][op_id]
        own_last_move = state["history"][itr - 1][self.id]

        # Forgive: when opponent defected and we cooperated, sometimes cooperate anyway
        if opponent_last_move == -1 and own_last_move == 1:
            if random.random() < self.forgiveness:
                return 1
            return -1

        return opponent_last_move
