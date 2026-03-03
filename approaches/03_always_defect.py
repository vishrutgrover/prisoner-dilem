"""
Always Defect - Unconditionally defect every round.
Maximizes short-term gain against cooperators; loses in long run.
Source: Test/p2 (commented variant)
"""

from base_agent import BaseAgent


class AlwaysDefect(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)

    def next_move(self, state: dict) -> int:
        return -1
