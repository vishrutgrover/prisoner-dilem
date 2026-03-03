"""
Tit for Tat - Classic strategy that won Axelrod's tournaments.
Cooperate on first move, then copy opponent's last move.
Source: Test/player1, Test 2/p1, IteratedPrisonersDilemma/player1
"""

from base_agent import BaseAgent


class TitForTat(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)

    def next_move(self, state: dict) -> int:
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr == 1:
            return 1  # Cooperate first
        return state["history"][itr - 1][op_id]
