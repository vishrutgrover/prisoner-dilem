"""
Pavlov / Win-Stay-Lose-Shift (WSLS).
Cooperate if last round was (C,C) or (D,C); defect if (C,D) or (D,D).
Source: Test/p2 (commented variant)
"""

from base_agent import BaseAgent


class PavlovWSLS(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)

    def next_move(self, state: dict) -> int:
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        if itr == 1:
            return 1

        opponent_last_move = state["history"][itr - 1][op_id]
        own_last_move = state["history"][itr - 1][self.id]

        # Lose (we got exploited or mutual defection) -> shift to defect
        if opponent_last_move == -1 and own_last_move == 1:
            return -1
        if opponent_last_move == -1 and own_last_move == -1:
            return -1

        # Win or both cooperated -> stay (cooperate)
        return 1
