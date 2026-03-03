"""
Streak-Based - Tracks defect/cooperate streaks for adaptive forgiveness.
If opponent cooperates after 5 defections, cooperate twice. If we cooperated 5x
and opponent defects, forgive once. Otherwise Tit for Tat logic.
Source: Test/bestagent, Test 2/p2, TestNew/finalsubmission
"""

from base_agent import BaseAgent


class StreakBased(BaseAgent):
    def __init__(self, id: int, defect_threshold: int = 5, coop_threshold: int = 5):
        super().__init__(id=id)
        self.defect_threshold = defect_threshold
        self.coop_threshold = coop_threshold

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

        # Opponent cooperates after long defect streak -> forgive
        if (
            self.defect_streak >= self.defect_threshold
            and opponent_last_move == 1
            and self.cooperate_streak == 1
        ):
            return 1

        # We cooperated a lot, opponent defected -> forgive once
        if self.cooperate_streak >= self.coop_threshold and opponent_last_move == -1:
            return 1

        if opponent_last_move == -1 and own_last_move == 1:
            return -1
        if opponent_last_move == -1 and own_last_move == -1:
            return -1
        if opponent_last_move == 1 and own_last_move == 1:
            return 1

        return 1
