"""
Testing Schedule - Probe opponent first, then exploit or Tit for Tat.
Plays C, D, C, C in first 4 rounds. If opponent always cooperated, defect forever.
Otherwise switch to Tit for Tat.
Source: Test/p3
"""

from base_agent import BaseAgent


class TestingSchedule(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)
        self.testing_schedule = [1, -1, 1, 1]  # C, D, C, C (fixed: -1 for defect)
        self.game_length = 0
        self.shall_i_exploit = False

    def next_move(self, state: dict) -> int:
        op_id = 1 if self.id == 2 else 2
        choice = None

        if self.game_length < 4:
            choice = self.testing_schedule[self.game_length]
        elif self.game_length == 4:
            opponents_actions = [
                state["history"][i][op_id]
                for i in range(1, 5)
                if i in state["history"]
            ]
            if opponents_actions.count(1) == 4:
                self.shall_i_exploit = True
            else:
                self.shall_i_exploit = False

        if self.game_length >= 4:
            if self.shall_i_exploit:
                choice = -1  # Exploit: defect forever
            else:
                # Tit for Tat: copy opponent's last move (last round = game_length)
                last_round = self.game_length
                choice = state["history"][last_round][op_id]

        self.game_length += 1
        return choice
