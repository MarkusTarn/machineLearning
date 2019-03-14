# LAB 4
## Pig game with Expectiminimax algorithm.

### Description:
Purpose for this lab was to familiarize with expectiminimax algorithm.

Game theory suggests, that if you have rolled 20 points, then ratio of next roll's lose to gain 
is 20 : 4 -> `5 : 1` (4 is average of all positive rolls).  
The chance of rolling a good roll is also `5 : 1`.  
This means that as long as you haven't rolled more than 20 points, it's cheaper to roll again.

This is the theory on which dummy_ai is built upon. It just rolls until it has more than 20 points.

It works well in most cases, but it can't handle end-game so well. If Opponent has 98 points and it
has rolled 92 points from 70, then it will hand over the turn even though it is cheaper to take the risk.

For this purpose there is a bit more sophisticated algorithm, expectiminimax. It uses minimax algoritm to look some moves ahead to see if any player is about to win and makes the best decision based on that.
Only difference between expectiminimax and minimax is that first one also uses change nodes in between player and opponent move to handle the uncertainty of dice roll.

In this case it was easy to implement because all rolls have the same probability (20%).

### Instructions to run:
1. Run the pig_game(`AI function`, [`optional AI as player two`]) method with desired AI function.

You can choose from three AI-s:
* dummy_ai - Simple AI that plays by game theory
* minimax_ai - More advanced AI that uses expectiminimax for better endgame
* human_ai - If you want to play against another person

Use second optional argument for player two if you want to match computer AI-s against each other.

### Example:
```
ai = dummy = 0
for i in range(10000):
    if pig_game(dummy_ai, minimax_ai):
        dummy += 1
    else:
        ai += 1

print('Minimax: ', ai)
print('Dummy: ', dummy)
```

### output:
```
Minimax:  5374
Dummy:  4626
```