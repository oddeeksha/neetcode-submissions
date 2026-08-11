from collections import deque
INF = 2147483647
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()
        def add_cell(nr, nc):
            if 0<=nr<ROWS and 0<=nc<COLS and (nr, nc) not in visited and grid[nr][nc]!=-1:
                queue.append((nr,nc))
                visited.add((nr,nc))



        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist
                add_cell(r-1,c)
                add_cell(r+1, c)
                add_cell(r,c-1)
                add_cell(r,c+1)
            dist += 1

            
            


       
        