# LAB 2
## Solving mazes using heuristic search algorithms

### Description:
Purpose for this lab was to familiarize with pathfinding algorithms using python.

I wrote an algorithm that would find shortest path from start to treasure on any solvable maze using `Breadth First Search`, `Greedy Search` and `A* Search`.

80% of the code was taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html. I just made a simple implementation
that would use four neighboring tiles to build up the frontier instead of using graphs because tiles don't own weight in these mazes.

* BFS solution is building up a growing frontier by adding four passable neighboring tiles of each current tile to the end of que while going through the que until it reaches treasure. Since every tile has a previous tile saved in array, it is really easy to trace back the path from start to finish after treasure has been found.

* Greedy solution is building up the frontier by always moving towards the general direction of goal (`D`). This is done by prioritizing neighboring tiles by distance from goal using simple calculation: `max(abs(self.goal[0] - current[0]), abs(self.goal[1] - current[1]))`. Also, as a frontier, PriorityQue is used instead of Que to easily get the next tile with shortest distance.

* AStar solution is really similar to Greedy one. It's also moving in the general direction of the goal and the main difference with greedy solution is, that for every visited tile it also saved the cost of getting to that tile so far (+1 for each previous tile). If algorithm finds its way to a tile that is already visited, but with a shorter path, then it will overwrite the cost-so-far for that tile and thus neglect the longer route. This will result AStar algorithm always taking the shortest route to goal even in situations where it gets stuck to dead-end and has to travel back to find a reroute.

There are two different heuristic searches `heuristic()` and `heuristic_advanced()` for distance. Both have similar performance.
I also added diagonal travelling, this shortened the shortest path by `32%` on average.

### Instructions to run:
1. Add your mazes to the 'mazes' folder or use any existing ones.
2. Create Maze object with given (file_name, start_row, start_col, goal_row, goal_col) as arguments.
3. Create Runner object with given (maze_name) as argument.
4. Use Runner's find_bfs() || find_greedy() || find_astar() method to find shortest path to treasure.
    Or use Runner's print_map(shortest_path) to print the shortest path on Runner's map in 'solutions' folder.

### Example:
```
maze_small = Maze("cave300x300", 2, 2, 295, 257)
maze_medium = Maze("cave600x600", 2, 2, 598, 595)
maze_big = Maze("cave900x900", 2, 2, 898, 895)

runner = Runner(maze_small)
runner.maze.print_map(runner.find_bfs())
runner.maze.print_map(runner.find_greedy())
runner.maze.print_map(runner.find_astar())
```

### output:
```
Number of steps: 373
Map printed to solutions/cave300x300
Number of steps: 770
Map printed to solutions/cave300x300
Number of steps: 373
Map printed to solutions/cave300x300
```