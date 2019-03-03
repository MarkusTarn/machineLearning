"""Algorithm for placing queens on chessboard so that no two queens share line of sight.

Instructions:
    1. Create Position object with (Number of tiles in row) as argument.
    2. Run the hill_climbing method with Position object as argument.

Default number of possible mutations is 100, if you want to change it, then enter it
as second optional argument for hill_climbing(queens, mutations).

Ideal solution/value would be 0. This means that there are no conflicts. (+1 for each conflict)

Author: Markus Tarn
Used sources: http://lambda.ee/wiki/Iti0210lab42
"""
from random import randint
import time

def hill_climbing(position, tries = 100):
    # Use hill climing method to clime towards better position
    start = time.time()
    current_value = position.get_value(position.queens)

    while True:
        move, new_value = position.best_move()
        if new_value == current_value and new_value != 0 and tries > 0:
            tries -= 1
            position.queens.append((randint(1, position.N - 1), position.queens.pop()[1]))
            move, new_value = position.best_move()
        elif new_value >= current_value:
            print("Time spent:", round(time.time() - start), "seconds")
            return current_value
        else:
            current_value = new_value
            position.queens = move

class NQPosition:
    def __init__(self, N):
        self.N = N
        self.queens = self.add_queens()
        print("Number of queens:", N)
        print("Initial position value:", self.get_value(self.queens))

    def get_value(self, queens):
        # Calculate number of conflicts (queens that can capture each other)
        conflicts = set()
        for queen in queens:
            for other_queen in queens:
                if queen != other_queen:
                    if queen[0] == other_queen[0]:
                        if queen[1] > other_queen[1]:
                            conflicts.add((queen, other_queen))
                        else:
                            conflicts.add((other_queen, queen))
                    if queen[1] == other_queen[1] or abs(queen[0] - other_queen[0]) == abs(queen[1] - other_queen[1]):
                        if queen[0] > other_queen[0]:
                            conflicts.add((queen, other_queen))
                        else:
                            conflicts.add((other_queen, queen))
        self.conflicts = conflicts
        return len(conflicts)

    def best_move(self):
        # See which queen you can move to get new best value
        queens = self.queens.copy()
        best_value = self.get_value(queens)
        best_queen = queens[0]
        for queen in self.queens.copy():
            queens.remove(queen)
            for row in range(self.N):
                if queen[0] != row:
                    new_queen = (row, queen[1])
                    queens.append(new_queen)
                    new_value = self.get_value(queens)
                    if new_value < best_value:
                        best_queen = new_queen
                        best_value = new_value

                    queens.remove(new_queen)

            queens.append(queen)

        queens = self.queens
        for queen in self.queens:
            if queen[1] == best_queen[1]:
                queens.remove(queen)
                queens.append(best_queen)

        return queens, self.get_value(queens)

    def add_queens(self):
        # Add queens for every column on random row
        queens = []
        for column in range(self.N):
            queens.append((randint(1, self.N - 1), column))
        return queens

    def print_board(self):
        # Print gameboard
        board = [[0] * self.N for i in range(self.N)]
        for queen in self.queens:
            board[queen[0]][queen[1]] = 1
        for row in board:
            print(row)


""" ...................................... Initialize positions here ................................. """
position = NQPosition(10)
print("Final value:", hill_climbing(position))
print("Final board:")
position.print_board()
