"""Code for finding shortest path from start ('s') to treasure ('D') on given maze (ASCII-art) using Breadth First Search.

Instructions:
    1. Copy your maze to the end of file.
    2. Create Runner Object with given (maze_name, start_row, start_col) as arguments.
    3. Use Runner's find_treasure method() to find shortest path to treasure.
        Or use Runner's print_map(shortest_path) to print the shortest path on Runner's map.

Author: Markus Tarn
Used sources: https://www.redblobgames.com/pathfinding/a-star/introduction.html
"""
from queue import Queue


class Runner:
    """Maze runner for finding shortest path to treasure.

    Args:
            maze (list of str): Maze represented as list of strings. NB! 'D' = treasure and '*' = lava.
            start_row (int): Row index for 's' (start) on maze.
            start_col (int): Character index for 's' (start) in starting row.
    """

    def __init__(self, maze, start_row, start_col):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = (start_row, start_col)

    def find_treasure(self):
        frontier = Queue()
        frontier.put(self.start)
        came_from = {}
        came_from[self.start] = None

        while not frontier.empty():
            current = frontier.get()
            if self.maze[current[0]][current[1]] == 'D':
                break

            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                if neighbor not in came_from:
                    frontier.put(neighbor)
                    came_from[neighbor] = current
        path = []
        while came_from[current] != self.start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def print_maze(self, path):
        for step in path:
            self.maze[step[0]] = self.maze[step[0]][:step[1]] + \
                '.' + self.maze[step[0]][step[1] + 1:]
        for row in range(self.rows):
            print(self.maze[row])

    def get_neighbors(self, current):
        neighbors = []
        # N
        if current[0] - 1 >= 0 and self.not_lava(current[0] - 1, current[1]):  # N
            neighbors.append((current[0] - 1, current[1]))
        # E
        if current[1] + 1 < self.cols and self.not_lava(current[0], current[1] + 1):
            neighbors.append((current[0], current[1] + 1))
        # S
        if current[0] + 1 < self.rows and self.not_lava(current[0] + 1, current[1]):
            neighbors.append((current[0] + 1, current[1]))
        # W
        if current[1] - 1 >= 0 and self.not_lava(current[0], current[1] - 1):
            neighbors.append((current[0], current[1] - 1))
        return neighbors

    def not_lava(self, x, y):
        return self.maze[x][y] != "*"


""" ...................................... Add your mazes here ................................. """
lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]

lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]

runner = Runner(lava_map1, 14, 16)
runner.print_maze(runner.find_treasure())
