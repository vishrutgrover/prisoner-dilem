"""
Streak-Based (Relaxed) - Same as StreakBased but with lower thresholds (3).
More forgiving variant; used in TestNew/finalsubmission.
Source: TestNew/finalsubmission
"""

from base_agent import BaseAgent


class StreakBasedRelaxed(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)
        self.defect_threshold = 3
        self.coop_threshold = 3

    def next_move(self, state: dict) -> int:
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        if not hasattr(self, "defect_streak"):
            self.defect_streak = 0
        if not hasattr(self, "cooperate_streak"):
            self.cooperate_streak = 0

        if itr == 1:
            return 1

        opponent_last_move = state["history"][itr - 1][op_id]
        own_last_move = state["history"][itr - 1][self.id]

        if opponent_last_move == -1:
            self.defect_streak += 1
            self.cooperate_streak = 0
        else:
            self.cooperate_streak += 1
            self.defect_streak = 0

        if (
            self.defect_streak >= self.defect_threshold
            and opponent_last_move == 1
            and self.cooperate_streak == 1
        ):
            return 1
        if self.cooperate_streak >= self.coop_threshold and opponent_last_move == -1:
            return 1
        if opponent_last_move == -1 and own_last_move == 1:
            return -1
        if opponent_last_move == -1 and own_last_move == -1:
            return -1
        if opponent_last_move == 1 and own_last_move == 1:
            return 1
        return 1
