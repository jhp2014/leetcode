class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1] 
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        
        return grid[n-1][m-1]