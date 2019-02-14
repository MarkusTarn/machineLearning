"""Code for finding shortest path from start ('s') to treasure ('D') on given maze (ASCII-art).

Instructions:
    1. Add your mazes to the 'mazes' folder
    2. Create Maze object with given (file_name, start_row, start_col, goal_row, goal_col) as arguments.
    3. Create Runner object with given (maze_name) as argument.
    4. Use Runner's find_bfs() || find_greedy() || find_astar() method to find shortest path to treasure.
        Or use Runner's print_map(shortest_path) to print the shortest path on Runner's map in 'solutions' folder.

Author: Markus Tarn
Used sources: https://www.redblobgames.com/pathfinding/a-star/introduction.html
"""
from queue import Queue, PriorityQueue


class Runner:
    def __init__(self, maze):
        self.maze = maze

    def find_bfs(self):
        frontier = Queue()
        frontier.put(self.maze.start)
        came_from = {}
        came_from[self.maze.start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == self.maze.goal:
                break

            neighbors = self.get_neighbors(self.maze, current)

            for neighbor in neighbors:
                if neighbor not in came_from:
                    frontier.put(neighbor)
                    came_from[neighbor] = current

        return self.reverse_path(came_from)

    def find_greedy(self):
        frontier = PriorityQueue()
        frontier.put(self.maze.start, 0)
        came_from = {}
        came_from[self.maze.start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == self.maze.goal:
                break

            neighbors = self.get_neighbors(self.maze, current)

            for next in neighbors:
                if next not in came_from:
                    priority = self.maze.heuristic_advanced(next)
                    frontier.put(next, priority)
                    came_from[next] = current
                    
        return self.reverse_path(came_from)   

    def find_astar(self):
        frontier = PriorityQueue()
        frontier.put(self.maze.start, 0)
        came_from = {}
        came_from[self.maze.start] = None
        cost_so_far = {}
        cost_so_far[self.maze.start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == self.maze.goal:
                break

            neighbors = self.get_neighbors(self.maze, current)

            for next in neighbors:
                new_cost = cost_so_far[current] + 1

                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.maze.heuristic_advanced(next)
                    frontier.put(next, priority)
                    came_from[next] = current
                    
        return self.reverse_path(came_from)

    def get_neighbors(self, maze, current):
        neighbors = []
        # N
        if current[0] - 1 >= 0 and self.not_lava(current[0] - 1, current[1]):
            neighbors.append((current[0] - 1, current[1]))
        # NE
        if current[0] - 1 >= 0 and current[1] + 1 < maze.cols and self.not_lava(current[0] - 1, current[1] + 1):
            neighbors.append((current[0] - 1, current[1] + 1))
        # E
        if current[1] + 1 < maze.cols and self.not_lava(current[0], current[1] + 1):
            neighbors.append((current[0], current[1] + 1))
        # SE
        if current[0] + 1 < maze.rows and current[1] + 1 < maze.cols and self.not_lava(current[0] + 1, current[1] + 1):
            neighbors.append((current[0] + 1, current[1] + 1))
        # S
        if current[0] + 1 < maze.rows and self.not_lava(current[0] + 1, current[1]):
            neighbors.append((current[0] + 1, current[1]))
        # SW
        if current[0] + 1 < maze.rows and current[1] - 1 >= 0 and self.not_lava(current[0] + 1, current[1] - 1):
            neighbors.append((current[0] + 1, current[1] - 1))
        # W
        if current[1] - 1 >= 0 and self.not_lava(current[0], current[1] - 1):
            neighbors.append((current[0], current[1] - 1))
        # NW
        if current[0] - 1 >= 0 and current[1] - 1 >= 0 and self.not_lava(current[0] - 1, current[1] - 1):
            neighbors.append((current[0] - 1, current[1] - 1))
        return neighbors

    def not_lava(self, x, y):
        return self.maze.map[x][y] != "*"

    def reverse_path(self, came_from):
        path = []
        current = self.maze.goal

        while came_from[current] != self.maze.start:
            current = came_from[current]
            path.append(current)

        path.reverse()
        print("Number of steps: " + str(len(path)))
        return path

class Maze:
    def __init__(self, file, start_row, start_col, goal_row, goal_col):
        self.file = file
        self.map = self.get_map()
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        self.start = (start_row, start_col)
        self.goal = (goal_row, goal_col)

    def heuristic(self, current):
        return abs(self.goal[0] - current[0]) + abs(self.goal[1] - current[1])

    def heuristic_advanced(self, current):
        return max(abs(self.goal[0] - current[0]), abs(self.goal[1] - current[1]))

    def get_map(self):
        with open("lab2/mazes/" + self.file) as f:
            map_data = [l.strip() for l in f.readlines() if len(l) > 1]
        return map_data

    def print_map(self, path):
        for step in path:
            self.map[step[0]] = self.map[step[0]][:step[1]] + \
                '.' + self.map[step[0]][step[1] + 1:]
        with open("lab2/solutions/" + self.file, "w") as f:
            for row in self.map:
                f.write(row + "\n")
            print("Map printed to solutions/" + self.file)


""" ...................................... Add your mazes here ................................. """

maze_small = Maze("cave300x300", 2, 2, 295, 257)
# maze_medium = Maze("cave600x600", 2, 2, 598, 595)
# maze_big = Maze("cave900x900", 2, 2, 898, 895)

runner = Runner(maze_small)
runner.maze.print_map(runner.find_bfs())
