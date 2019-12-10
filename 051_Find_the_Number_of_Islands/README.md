# Find the Number of Islands
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present in the grid. The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
Assume all edges outside of the grid are water.

Example:
```
Input: 
10001
11000
10110
00000

Output: 3
```
Here's your starting point:
```
class Solution(object):
  def inRange(self, grid, r, c):
    numRow, numCol = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= numRow or c >= numCol:
      return False
    return True

  def numIslands(self, grid):
    # Fill this in.

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3
```