
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
           
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        number = 0
        def dfs(row, col):
            for r, c in [(row-1,col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0<= r < ROWS and 0<=c < COLS and grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    dfs(r,c)

            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row,col)
                    number += 1
        return number     
