"""Algorithm for placing queens on chessboard so that no two queens share line of sight.

Instructions:
    1. Create Position object with (Number of tiles in row) as argument.
    2. Run the hill_climbing method with Position object as argument.

Ideal solution/value would be 0. This means that there are no conflicts. (+1 for each conflict)

Author: Markus Tarn
Used sources: http://lambda.ee/wiki/Iti0210lab42
"""
from random import randint
import time

def hill_climbing(pos):
    curr_value = pos.get_value(pos.queens)
    tries = 100

    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            if new_value == curr_value and new_value != 0 and tries > 0:
                # use one try to generate random mutation
                tries -= 1
                pos.queens.append((randint(1, pos.N - 1), pos.queens.pop()[1]))
                move, new_value = pos.best_move()
            else:
                # finish
                return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)

class NQPosition:
    def __init__(self, N):
        self.N = N
        self.queens = self.add_queens()
        self.print_board()

    def get_value(self, queens):
        # calculate number of conflicts (queens that can capture each other)
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

    def make_move(self, move):
        # actually execute a move (change the board)
        self.queens = move

    def best_move(self):
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
start = time.time()
pos = NQPosition(20) # test with the tiny 4x4 board first
print("Number of queens", pos.N)
print("Initial position value", pos.get_value(pos.queens))
best_pos, best_value = hill_climbing(pos)
print("Final value", best_value)
# print("Final map")
# pos.print_board()
end = time.time()
print(end - start)
# if best_value is 0, we solved the problem