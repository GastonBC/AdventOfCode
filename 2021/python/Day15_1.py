import numpy as np
import Inputs

maze = Inputs.Day15()

rows, cols = maze.shape

maze_sum = np.zeros_like(maze)
maze_sum[0, :] += np.cumsum(maze[0, :])
maze_sum[:, 0] += np.cumsum(maze[:, 0])
maze_sum[0, 0] -= 1

for row in range(1, rows):
    for col in range(1, cols):
        maze_sum[row, col] = min(maze_sum[row - 1, col] + maze[row, col],
                                 maze_sum[row, col - 1] + maze[row, col])
        
print(maze_sum[rows - 1, cols - 1] - maze[0, 0])