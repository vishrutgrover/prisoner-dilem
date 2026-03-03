from agent import BaseAgent
import random

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        """
        Your agent's logic goes here.
        You can use the state["history"] object to access the history of the game.
        The history is a list of all the moves made by both players in the game.
        The last move is state["history"][-1].
        The second last move is state["history"][-2] and so on.
        state["history"][-1][1] gives the last move of the opponent if you are player 1.
        state["history"][-1][2] gives the last move of the opponent if you are player 2.
        state["current_iter"] gives the current iteration number.
        You can only import random and math modules.
        Direct imports of other modules are not allowed.
        """
