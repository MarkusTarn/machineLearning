# LAB 1
## Solving mazes using Breadth First Search

### Description:
Purpose for this lab was to familiarize with graph-theory and pathfinding algorithms using python.

I wrote an algorithm that would find shortest path from start to treasure on any solvable maze using Breadth First Search.
80% of the code was taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html. I just made a simple implementation
that would use four neighboring tiles to build up the frontier instead of using graphs because tiles don't own weight in these mazes.

This solution is building up a growing frontier by adding four passable neighboring tiles of each current tile to the end of que while going through the que until it reaches treasure. Since every tile has a previous tile saved in array, it is really easy to trace back the path from start to finish after treasure has been found.

### Instructions to run:
1. Copy your maze to the end of file. Maze consists of list of strings. 's' = start, 'D' = treasure, '*' = lava, anything else is walkable terrain.
2. Create Runner Object with given (maze_name, start_row, start_col) as arguments.
3. Use Runner's find_treasure method() to find shortest path to treasure.
        Or use Runner's print_map(shortest_path) to print the shortest path on Runner's map.

### Example:
```
lava_map = [
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

runner = Runner(lava_map, 14, 16)
runner.print_map(runner.find_treasure())
```

### output:
```
     **********************    
   *******   D....**********   
   *******       .             
 ****************.   **********
***********.......   ********  
           .*******************
 ********  . ******************
********   .               ****
*****      .************       
***        .......*********    
*      ******    . ************
*****************.      *******
***      ****   ..       ***** 
                .              
                s  
```