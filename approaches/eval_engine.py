"""
Evaluation engine for Iterated Prisoner's Dilemma strategies.
Run from the approaches/ directory: python eval_engine.py

Configure player1 and player2 below to test different strategy matchups.
"""

import time
import threading
import random
import math
import json
import copy
import sys
import os

# Add script directory for imports when running as script
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from base_agent import BaseAgent

# ============ CONFIGURE STRATEGIES HERE ============
# Uncomment and modify to test different matchups:
# from base_agent import BaseAgent  # (already imported above)

# Default: Tit for Tat vs Final Strategy (run from approaches/: python eval_engine.py)
from importlib import import_module

_tft = import_module("01_tit_for_tat")
_fs = import_module("07_final_strategy")
player1 = _tft.TitForTat(1)
player2 = _fs.FinalStrategy(2)

players = [player1, player2]

# ============ GAME PARAMETERS ============
COOP = 1
DEFECT = -1

coop_win = lambda x: 20 + 5 * (x // 5)
betrayal_win = lambda x: 50
betrayal_lose = lambda x: -10 * (x // 5)
defect = lambda x: -5 * (x // 5)
payoff_matrix = [
    [coop_win, coop_win],
    [betrayal_win, betrayal_lose],
    [defect, defect],
]

error = 0.05
time_limit = 0.01
rounds = 100

move_queue = [0, 0]
streak = 0
history = {}
iteration = 1
score = {1: 0, 2: 0}


def threaded_player_call(player, streak_val, iteration_val):
    global move_queue
    state = {
        "current_iter": iteration_val,
        "history": history,
        "streak": streak_val,
    }
    state = copy.deepcopy(state)
    move = players[player].next_move(state)
    if iteration_val not in history:
        move_queue[player] = move


def event_loop():
    global iteration, streak, score, move_queue, history
    while iteration <= rounds:
        threading.Thread(
            target=threaded_player_call, args=(0, streak, iteration)
        ).start()
        threading.Thread(
            target=threaded_player_call, args=(1, streak, iteration)
        ).start()
        time.sleep(time_limit)

        if not move_queue[0] or move_queue[0] not in [COOP, DEFECT]:
            move_queue[0] = (
                random.choice([COOP, DEFECT])
                if iteration == 1
                else history[iteration - 1][1]
            )
        if not move_queue[1] or move_queue[1] not in [COOP, DEFECT]:
            move_queue[1] = (
                random.choice([COOP, DEFECT])
                if iteration == 1
                else history[iteration - 1][2]
            )

        is_err1 = random.random() < error
        is_err2 = random.random() < error
        if is_err1:
            move_queue[0] = -move_queue[0]
        if is_err2:
            move_queue[1] = -move_queue[1]

        if move_queue[0] == COOP and move_queue[1] == COOP:
            score[1] += payoff_matrix[0][0](streak)
            score[2] += payoff_matrix[0][1](streak)
            streak += 1
        elif move_queue[0] == DEFECT and move_queue[1] == COOP:
            score[1] += payoff_matrix[1][0](streak)
            score[2] += payoff_matrix[1][1](streak)
            streak = math.ceil(streak / 2) if (is_err1 or is_err2) else 0
        elif move_queue[0] == COOP and move_queue[1] == DEFECT:
            score[1] += payoff_matrix[1][1](streak)
            score[2] += payoff_matrix[1][0](streak)
            streak = math.ceil(streak / 2) if (is_err1 or is_err2) else 0
        else:
            score[1] += payoff_matrix[2][0](streak)
            score[2] += payoff_matrix[2][1](streak)
            streak = math.ceil(streak / 2) if (is_err1 and is_err2) else 0

        history[iteration] = {
            1: move_queue[0],
            2: move_queue[1],
            "score": copy.deepcopy(score),
        }
        move_queue = [0, 0]
        iteration += 1


if __name__ == "__main__":
    event_loop()
    print(json.dumps(history, indent=2))
