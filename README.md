# Maze Generator and Solver

This project creates and solves a random maze using Python and Tkinter.

The maze is built using a stack-based Depth First Search (DFS) method.

An invisible mouse starts in one cell and moves to random neighbor cells.  
When it moves, it removes walls between cells.  
If the mouse reaches a dead end, it goes back using the stack.

This continues until all cells are visited.

After creating the maze, another mouse solves the maze.

- Red dot = current path
- Blue dot = dead end / backtracking

## Files

- maze.py

## How to Run

python maze.py