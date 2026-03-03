"""
Always Cooperate - Unconditionally cooperate every round.
Simple baseline; vulnerable to exploitation.
Source: Test/p1 (modified), Test/p2
"""

from base_agent import BaseAgent


class AlwaysCooperate(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)

    def next_move(self, state: dict) -> int:
        return 1
