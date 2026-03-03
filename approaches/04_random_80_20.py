"""
Random 80-20 - 80% cooperate, 20% defect (random).
Used for testing against unpredictable opponents.
Source: Test/p2 (commented variant)
"""

from base_agent import BaseAgent
from random import randint


class Random8020(BaseAgent):
    def __init__(self, id: int):
        super().__init__(id=id)

    def next_move(self, state: dict) -> int:
        return 1 if randint(1, 100) <= 80 else -1
