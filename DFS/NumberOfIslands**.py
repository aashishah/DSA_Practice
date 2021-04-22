'''
QUESTION
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

'''

#CODE:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        def sink(i, j):
            if i < 0 or j < 0 or (i >= n) or (j >= m) or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            sink(i, j + 1)
            sink(i + 1, j)
            sink(i - 1, j)
            sink(i, j - 1)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    sink(i, j)
                    count += 1
                
        return count
