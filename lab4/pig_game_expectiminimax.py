"""Pig game with option to play against expectiminimax algorithm.
Check out rules for Pig Dice Game here: https://www.dicegamedepot.com/dice-n-games-blog/pig-dice-game-rules/

Instructions:
    1. Run the pig_game() method with AI function as argument.

You can choose from three AI-s:
* dummy_ai - Simple AI that plays by game theory
* minimax_ai - More advanced AI that uses expectiminimax for better endgame
* human_ai - If you want to play against other person

You can also use second optional argument for player two if you want to mach computer AI-s against each other.


Author: Markus Tarn
Used sources: http://lambda.ee/wiki/Iti0210lab62
"""
import random

PLAYER_ONE = 1
PLAYER_TWO = -1

ROLL = 0
PASS = 1


def human_ai(turn, pot, player_two_bank, player_one_bank):
    if pot > 0:
        s = input("Do you want to keep rolling (Y/n)? ")
        return PASS if len(s) > 0 and s[0].lower() == "n" else ROLL
    else:
        return ROLL


def dummy_ai(turn, pot, player_two_bank, player_one_bank):
    return ROLL if pot < 21 else PASS


def minimax_ai(turn, pot, player_two_bank, player_one_bank):
    # Returns the move with highest minimax estimate.
    depth = 10
    ai_bank = player_two_bank if turn == PLAYER_TWO else player_one_bank
    opponent_bank = player_one_bank if turn == PLAYER_TWO else player_two_bank
    roll_state = exp_minimax(turn, 1, pot, ai_bank, opponent_bank, depth, turn)
    pass_state = exp_minimax(-turn, 0, 0, ai_bank + pot, opponent_bank, depth, turn)
    return ROLL if roll_state > pass_state or pass_state == roll_state and pot < 21 else PASS


def exp_minimax(turn, chance, pot, ai_bank, opponent_bank, depth, player):
    depth = depth - 1

    # Case 1: Somebody won or out of depth
    if ai_bank >= 100:
        return 1
    elif opponent_bank >= 100:
        return -1
    elif depth < 1:
        return 0

    # Case 2: Chance node
    if chance:
        success = exp_minimax(turn, 0, pot + 4, ai_bank, opponent_bank, depth, player)
        failure = exp_minimax(-turn, 0, 0, ai_bank, opponent_bank, depth, player)
        return success if success > failure else failure
    # Case 3: AI's turn and NOT a chance node (return min value)
    elif turn == player:
        roll_state = exp_minimax(turn, 1, pot, ai_bank, opponent_bank, depth, player)
        pass_state = exp_minimax(-turn, 0, 0, ai_bank + pot, opponent_bank, depth, player)
        return roll_state if roll_state > pass_state else pass_state
    # Case 4: Opponent's turn and NOT a chance node (return min value)
    else:
        roll_state = exp_minimax(turn, 1, pot, ai_bank, opponent_bank, depth, player)
        pass_state = exp_minimax(-turn, 0, 0, ai_bank, opponent_bank + pot, depth, player)
        return roll_state if roll_state < pass_state else pass_state


def pig_game(ai_function, opponent_function = human_ai):
    player_one_bank = player_two_bank = rolled = 0
    turn = PLAYER_TWO

    while player_one_bank < 100 and player_two_bank < 100:
        print("Player one points", player_one_bank, "player two points", player_two_bank, "holding", rolled)
        if turn == PLAYER_ONE:
            decision = ai_function(turn, rolled, player_two_bank, player_one_bank)
        else:
            decision = opponent_function(turn, rolled, player_two_bank, player_one_bank)

        if decision == PASS:
            rolled = 0
            turn = -turn
        else:
            dieroll = random.randint(1, 6)
            if dieroll == 1:
                if turn == PLAYER_ONE:
                    player_one_bank -= rolled
                else:
                    player_two_bank -= rolled
                rolled = 0
                turn = -turn
            else:
                rolled += dieroll
                if turn == PLAYER_ONE:
                    player_one_bank += dieroll
                else:
                    player_two_bank += dieroll

    if player_one_bank >= 100:
        return 1
    elif player_two_bank >= 100:
        return 0


""" ...................................... Initialize positions here ................................. """
ai = dummy = 0
for i in range(10000):
    if pig_game(dummy_ai, minimax_ai):
        dummy += 1
    else:
        ai += 1

print('Minimax: ', ai)
print('Dummy: ', dummy)

