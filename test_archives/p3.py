from agent import BaseAgent
import random

class p3(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.testing_schedule = [1, 0, 1, 1]
        self.game_length = 0
        self.shall_i_exploit = False

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        choice = None
        
        if self.game_length < 4:  # We're still in the initial testing stage.
            choice = self.testing_schedule[self.game_length]
        elif self.game_length == 4:  # Time to analyze the testing stage and decide what to do based on what the opponent did in that time!
            opponents_actions = [move[op_id] for move in state["history"]]
            if opponents_actions.count(1) == 4:  # The opponent cooperated all 4 turns! Never defected!
                self.shall_i_exploit = True  # Let's exploit forever.
            else:
                self.shall_i_exploit = False  # Let's switch to Tit For Tat.

        if self.game_length >= 4:
            if self.shall_i_exploit:
                choice = 0
            else:
                choice = state["history"][-1][op_id]  # Do Tit for Tat

        self.game_length += 1
        return choice
